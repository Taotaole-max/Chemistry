"""=== Word Figure 13 ===  §5.4 两条降解路径，一张两面板图。

(a) 聚酯主链酯键水解：产物含羧基端，羧基降低局部 pH 反过来加速水解——自催化，
    厚制品从内部先坏（本体侵蚀，不是表面侵蚀）。RDKit 画反应式。
(b) 多糖 / 蛋白的酶解：酶只能接触无定形区，结晶区把酶挡在外面，所以结晶度直接
    设定降解速率——同一个结晶度既给强度、又挡水、也挡降解。

上一版把这两个面板 + 一张"酯水解能垒示意曲线"拆成三张独立的图（原 Fig 13/14/15），
放在一起显得零碎。现在合回一张两面板图；能垒示意曲线（本来就"仅示意、不含计算值"
的计算旁支）删掉，正文 §5.4 一句话带过。图内不再写大标题和整段说明——都进 Word 图注。
"""

import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from rdkit.Chem import rdChemReactions
from rdkit.Chem.Draw import rdMolDraw2D

from style import (C_POLYSACCHARIDE, FIG_W, FS_PANEL_TITLE, INK, INK_MUTED,
                   C_POLYESTER, _trim_white, apply_style, save)

OUT = Path(__file__).parent / "output"

HYDROLYSIS = "*C(=O)O[C@@H](C)*.O>>*C(=O)O.O[C@@H](C)*"
PX_W, PX_H = 1200, 560


def panel_a(ax):
    rxn = rdChemReactions.ReactionFromSmarts(HYDROLYSIS, useSmiles=True)
    drawer = rdMolDraw2D.MolDraw2DCairo(PX_W, PX_H)
    opts = drawer.drawOptions()
    opts.dummiesAreAttachments = True
    opts.bondLineWidth = 3
    opts.fixedFontSize = 32
    drawer.DrawReaction(rxn)
    drawer.FinishDrawing()
    img = _trim_white(mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png"))
    ax.imshow(img)
    ax.axis("off")
    ax.set_anchor("N")
    ax.set_title("(a) Polyester: backbone hydrolysis", fontsize=FS_PANEL_TITLE,
                 fontweight="bold", color=C_POLYESTER, loc="left", pad=3.0)


def panel_b(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 46)
    ax.axis("off")
    ax.set_anchor("N")
    ax.set_title("(b) Polysaccharide / protein: enzymatic attack",
                 fontsize=FS_PANEL_TITLE, fontweight="bold",
                 color=C_POLYSACCHARIDE, loc="left", pad=3.0)

    blocks = [("crystalline", 18), ("amorphous", 10), ("crystalline", 22),
              ("amorphous", 10), ("crystalline", 16)]
    x, y, h = 6.0, 20.0, 10.0
    for kind, w in blocks:
        if kind == "crystalline":
            ax.add_patch(Rectangle((x, y), w, h, facecolor=C_POLYSACCHARIDE,
                                   edgecolor=C_POLYSACCHARIDE, zorder=3))
            ax.text(x + w / 2, y + h / 2, "crystalline", fontsize=6.0,
                    color="#ffffff", ha="center", va="center", zorder=4)
        else:
            ax.add_patch(Rectangle((x, y), w, h, facecolor="#ffffff",
                                   edgecolor=C_POLYSACCHARIDE, hatch="////",
                                   linewidth=0.8, zorder=3))
        x += w

    ax.plot([29.0, 29.0], [y - 4.0, y - 0.6], color=C_POLYSACCHARIDE, lw=0.6, zorder=3)
    ax.text(29.0, y - 4.8, "amorphous", fontsize=6.0, color=C_POLYSACCHARIDE,
            ha="center", va="top")

    for cx, accessible in ((29.0, True), (61.0, True), (15.0, False), (84.0, False)):
        ey = y + h + 8.0
        colour = INK if accessible else INK_MUTED
        # 用 marker 而不是 Circle：坐标轴不是等比的，Circle 会被压成椭圆
        ax.plot([cx], [ey], marker="o", markersize=13, markerfacecolor="#f4f4f1",
                markeredgecolor=colour, markeredgewidth=0.9, zorder=4)
        ax.text(cx, ey, "E", fontsize=6.0, color=colour, ha="center",
                va="center", zorder=5)
        if accessible:
            ax.annotate("", xy=(cx, y + h + 0.6), xytext=(cx, ey - 3.0),
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9,
                                        mutation_scale=6), zorder=4)
        else:
            ax.plot([cx], [ey - 4.4], marker="x", markersize=4.4,
                    markeredgewidth=1.1, color=INK_MUTED, zorder=5)


def main():
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W, 40 / 25.4),
                             layout="constrained",
                             gridspec_kw={"width_ratios": [1.15, 1.0]})
    panel_a(axes[0])
    panel_b(axes[1])
    save(fig, "fig_degradation", OUT)


if __name__ == "__main__":
    main()
