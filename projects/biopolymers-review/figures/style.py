"""图形统一样式。

配色取自已通过色盲安全校验的四色（all-pairs 模式，最差色盲对 ΔE 9.2，
最差常视力对 ΔE 16.3）。颜色跟着**主链化学类别**走，全套图保持一致，
超过四类的一律折进灰色 "other"，不再新增色相——这是配色校验的硬性约束。
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

MM = 1 / 25.4  # mm -> inch

# 主链化学类别配色
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

# 正式论文排版：图内文字 Arial 8 pt，最小 7 pt
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


def save(fig, stem, outdir):
    """同时导出 SVG（进 Word）和 600 dpi PNG（校对用）。"""
    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / f"{stem}.svg", bbox_inches="tight", pad_inches=0.02)
    fig.savefig(outdir / f"{stem}.png", dpi=600, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(f"  wrote {stem}.svg + {stem}.png")
