"""图形统一样式 + 共用画布 / 分子绘制工具。

所有正文和附录图共用一套规格，解决"画幅不统一、字号忽大忽小"的问题：

- **固定通栏宽度 170 mm**（= build_docx.py 的嵌入宽度）。每个脚本不再各自设宽度，
  一律用 `new_fig(height_mm, ...)`，宽度锁死 FIG_W。
- **save() 不再用 bbox_inches="tight"**：导出尺寸 == figsize，Word 里所有图同一比例、
  同一字号（图内 8 pt 就是最终 8 pt，不会随裁剪缩放漂移）。配合 constrained layout
  保证标签不被裁掉。
- **图内不写大标题、不写整句说明**——这些一律放 Word 图注（report.md / report_zh.md）。
  图上只留面板标签和 ≤5 词的短标注。
- **分子式统一走 draw_mol()**：同一线宽、同一字号、同一画布像素，跨图分子大小一致。

配色沿用已过色盲校验的类别色（颜色跟主链化学类别走，超过五类折进灰色，不新增色相）。
"""

import io

import matplotlib as mpl
import matplotlib.pyplot as plt

MM = 1 / 25.4  # mm -> inch

# ── 通栏宽度：所有图统一 170 mm ─────────────────────────────────────────────
FIG_W_MM = 170.0
FIG_W = FIG_W_MM * MM

# 高度三档建议值（mm）——和 build_docx.py 的 FIGURE_HEIGHT_S/M/L 嵌入高度对齐。
# 结构真的需要更高的图（分类树、因果链、分散度）可以自己传更大的 height_mm。
H_S = 34.0
H_M = 52.0
H_L = 64.0

# ── 统一字号（图内 ax.text 用，pt）────────────────────────────────────────
FS_PANEL_TITLE = 8.0   # 面板标签   (a) Cellulose
FS_PANEL_SUB = 6.3     # 面板标签下的化学名 / 副标题
FS_ANNOT = 6.5         # 图内短标注（≤5 词）
FS_TAG = 6.0           # 极小标签（来源 E/M/S、单位角标等）

# ── 主链化学类别配色（已过色盲 all-pairs 校验）────────────────────────────
C_POLYSACCHARIDE = "#2a78d6"  # 蓝
C_POLYESTER = "#eb6834"       # 橙
C_PROTEIN = "#1baf7a"         # 绿（对白底对比度偏低 → 必须配直接标注）
C_PETRO = "#4a3aa7"           # 紫，仅用于石油基对照
C_OTHER = "#8a8a85"           # 灰：木质素、天然橡胶、核酸等

CLASS_COLOR = {
    "polysaccharide": C_POLYSACCHARIDE,
    "polyester": C_POLYESTER,
    "protein": C_PROTEIN,
    "petro": C_PETRO,
    "other": C_OTHER,
}

INK = "#1a1a19"
INK_SECONDARY = "#52514e"
INK_MUTED = "#8a8a85"
SURFACE = "#ffffff"

# 正式论文排版：图内文字 Arial 8 pt，最小 6 pt
FONT_STACK = ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"]


def apply_style():
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": FONT_STACK,
        "font.size": 8,
        "axes.labelsize": 8,
        "axes.titlesize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": INK_SECONDARY,
        "xtick.color": INK_SECONDARY,
        "ytick.color": INK_SECONDARY,
        "axes.linewidth": 0.6,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "lines.linewidth": 1.4,
        "grid.color": "#e2e2de",
        "grid.linewidth": 0.5,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        # SVG 里保留可编辑文字，Word 插入后用系统 Arial 渲染
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
    })


def new_fig(height_mm, nrows=1, ncols=1, constrained=True, **subplot_kw):
    """建一张固定 170 mm 宽的图。height_mm 决定高度（用 H_S/H_M/H_L 或自定义）。

    默认开 constrained layout，配合 save() 的 bbox_inches=None，保证导出尺寸精确、
    标签不被裁。手工用 data 坐标摆放元素的图（分类树、流程图那种）传 constrained=False，
    再自己 ax.set_axis_off() + ax.set_xlim/ylim。
    """
    apply_style()
    layout = "constrained" if constrained else None
    fig, axes = plt.subplots(nrows, ncols, figsize=(FIG_W, height_mm * MM),
                             layout=layout, **subplot_kw)
    return fig, axes


# ── 共用分子绘制 ─────────────────────────────────────────────────────────────
# 之前 5 个 fig_*.py 各自抄了一份 render()，参数略有出入。统一到这里：
# 同一线宽、同一字号、同一画布像素 → 跨图分子视觉大小一致。
_MOL_PX_W = 760
_MOL_PX_H = 520
_MOL_BOND_WIDTH = 3
_MOL_FONT = 38


def _trim_white(arr, pad_px=8):
    """裁掉分子图四周的纯白边——RDKit 输出留白很多，不裁的话 imshow 里分子又小、
    周围一圈空白，正是"画幅乱"的一个来源。"""
    import numpy as np
    mask = np.any(arr[..., :3] < 0.97, axis=-1)
    if not mask.any():
        return arr
    rows, cols = np.any(mask, axis=1), np.any(mask, axis=0)
    r0, r1 = np.where(rows)[0][[0, -1]]
    c0, c1 = np.where(cols)[0][[0, -1]]
    r0, c0 = max(0, r0 - pad_px), max(0, c0 - pad_px)
    r1, c1 = min(arr.shape[0] - 1, r1 + pad_px), min(arr.shape[1] - 1, c1 + pad_px)
    return arr[r0:r1 + 1, c0:c1 + 1]


def draw_mol(smiles, annotate_cip=False, px_w=_MOL_PX_W, px_h=_MOL_PX_H, trim=True):
    """SMILES -> RGBA ndarray（给 ax.imshow）。所有单体图统一调这个。

    annotate_cip=True 只在"立体化学本身就是这张图的重点"时开（多糖 C1/C5、聚酯 R/S）；
    其余图关掉，避免 (R)/(S) 到处飘。trim=True 裁掉 RDKit 的白边，让分子占满面板。
    """
    from rdkit import Chem
    from rdkit.Chem import rdDepictor
    from rdkit.Chem.Draw import rdMolDraw2D
    import matplotlib.image as mpimg

    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DCairo(px_w, px_h)
    opts = drawer.drawOptions()
    opts.dummiesAreAttachments = True
    opts.addStereoAnnotation = annotate_cip
    opts.bondLineWidth = _MOL_BOND_WIDTH
    opts.fixedFontSize = _MOL_FONT
    opts.padding = 0.06
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    arr = mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png")
    return _trim_white(arr) if trim else arr


def panel_title(ax, tag, name, colour, sub=None):
    """统一的面板标签，用 ax.set_title（constrained layout 会自动为它留白，不会被裁）。

    sub（化学名等）默认不画——放 Word 图注里。只有极少数图确实需要在图上标出时才传。
    """
    label = f"({tag}) {name}"
    if sub:
        label += f"\n{sub}"
    ax.set_title(label, fontsize=FS_PANEL_TITLE, fontweight="bold",
                 color=colour, loc="left", pad=3.0, linespacing=1.3)
    # imshow 面板在 constrained cell 里默认居中、上下留白 → 顶对齐，标题才和邻格齐平
    ax.set_anchor("N")


def save(fig, stem, outdir):
    """同时导出 SVG（进 Word）和 600 dpi PNG（校对用）。

    关键：bbox_inches=None —— 导出尺寸严格等于 figsize，不再按内容裁剪。所有图因此
    在 Word 里同宽（170 mm）、同字号。标签不被裁靠的是 constrained layout（见 new_fig）。
    """
    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / f"{stem}.svg", bbox_inches=None, pad_inches=0.0)
    fig.savefig(outdir / f"{stem}.png", dpi=600, bbox_inches=None, pad_inches=0.0)
    plt.close(fig)
    print(f"  wrote {stem}.svg + {stem}.png")
