"""Fig 6 · 两条降解路径与酯水解的能量图（示意）。

(a) 聚酯：主链酯键水解，产物含羧基端，羧基降低局部 pH 反过来加速水解——自催化，
    因此厚制品从内部先坏，表现为本体侵蚀而不是表面侵蚀。
(b) 多糖与蛋白：酶解，酶只能接触无定形区，结晶区把酶挡在外面，
    所以结晶度直接设定降解速率——同一个结晶度既给强度、又挡水、也挡降解。
(c) 酯水解三种条件的能垒次序（示意图，不含计算值）：碱催化 < 酸催化 < 中性水。

(c) 用线型区分路径、颜色沿用聚酯的橙色，黑白打印也能区分。
(a) 和 (b) 的画布长宽比刻意做成一致，标题才能对齐。
"""

import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle
from rdkit.Chem import rdChemReactions
from rdkit.Chem.Draw import rdMolDraw2D

from style import (C_POLYESTER, C_POLYSACCHARIDE, INK, INK_MUTED, INK_SECONDARY,
                   MM, apply_style, save)

OUT = Path(__file__).parent / "output"

HYDROLYSIS = "*C(=O)O[C@@H](C)*.O>>*C(=O)O.O[C@@H](C)*"

PANEL_ASPECT = 2.0          # 两个上方面板共用的长宽比
PX_W = 1200
PX_H = int(PX_W / PANEL_ASPECT)

NOTE_A = (
    "Chain scission gives one carboxyl and one hydroxyl end. The\n"
    "carboxyl end lowers the local pH and accelerates further\n"
    "hydrolysis (autocatalysis), so thick parts degrade from the\n"
    "inside out — bulk erosion rather than surface erosion."
)
NOTE_B = (
    "Enzymes are large and hydrolyse only segments they can reach,\n"
    "so scission is confined to accessible disordered regions.\n"
    "Crystallinity sets the rate: the same order that provides\n"
    "strength and moisture resistance also blocks degradation."
)
NOTE_C = (
    "Ordering only; no calculated values are implied. Quantitative barriers for the three regimes, and for the "
    "autocatalytic route in (a),\nare obtained from DFT with an implicit solvation model."
)


def title(ax, tag, text, colour):
    ax.text(0.0, 1.06, f"({tag}) {text}", transform=ax.transAxes, fontsize=7.5,
            weight="bold", color=colour, ha="left", va="bottom")


def note(ax, text):
    ax.axis("off")
    ax.text(0.0, 1.0, text, transform=ax.transAxes, fontsize=6.3, color=INK,
            ha="left", va="top", linespacing=1.7)


def panel_a(ax):
    rxn = rdChemReactions.ReactionFromSmarts(HYDROLYSIS, useSmiles=True)
    drawer = rdMolDraw2D.MolDraw2DCairo(PX_W, PX_H)
    opts = drawer.drawOptions()
    opts.dummiesAreAttachments = True
    opts.bondLineWidth = 3
    opts.fixedFontSize = 30
    drawer.DrawReaction(rxn)
    drawer.FinishDrawing()
    ax.imshow(mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png"))
    ax.axis("off")
    title(ax, "a", "Polyesters: backbone hydrolysis", C_POLYESTER)


def panel_b(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 / PANEL_ASPECT)
    ax.axis("off")
    title(ax, "b", "Polysaccharides and proteins: enzymatic attack", C_POLYSACCHARIDE)

    blocks = [("crystalline", 18), ("amorphous", 10), ("crystalline", 22),
              ("amorphous", 10), ("crystalline", 16)]
    x, y, h = 6.0, 17.0, 8.0
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

    ax.plot([29.0, 29.0], [y - 3.4, y - 0.4], color=C_POLYSACCHARIDE, lw=0.6, zorder=3)
    ax.text(29.0, y - 4.0, "amorphous", fontsize=6.0, color=C_POLYSACCHARIDE,
            ha="center", va="top")

    for cx, accessible in ((29.0, True), (61.0, True), (15.0, False), (84.0, False)):
        ey = y + h + 8.0
        colour = INK if accessible else INK_MUTED
        ax.add_patch(plt.Circle((cx, ey), 2.6, facecolor="#f4f4f1",
                                edgecolor=colour, linewidth=0.9, zorder=4))
        ax.text(cx, ey, "E", fontsize=6.0, color=colour, ha="center",
                va="center", zorder=5)
        if accessible:
            ax.annotate("", xy=(cx, y + h + 0.5), xytext=(cx, ey - 3.0),
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9,
                                        mutation_scale=6), zorder=4)
        else:
            ax.plot([cx], [ey - 4.2], marker="x", markersize=4.4,
                    markeredgewidth=1.1, color=INK_MUTED, zorder=5)


def profile(barrier):
    x = np.linspace(0, 1, 400)
    return x, barrier * np.exp(-((x - 0.5) ** 2) / 0.012) - 0.55 * x


def panel_c(ax):
    title(ax, "c", "Relative barriers for ester hydrolysis (schematic)", C_POLYESTER)

    routes = [
        ("neutral water", 1.00, (0, ()), 0.50),
        ("acid-catalysed", 0.72, (0, (4, 2)), 0.41),
        ("base-catalysed", 0.48, (0, (1.5, 1.5)), 0.34),
    ]
    for label, barrier, dash, label_x in routes:
        x, y = profile(barrier)
        ax.plot(x, y, color=C_POLYESTER, linewidth=1.4, linestyle=dash, zorder=3)
        peak = barrier - 0.55 * 0.5
        ax.text(label_x, peak + 0.05, label, fontsize=6.5, color=C_POLYESTER,
                ha="right" if label_x < 0.5 else "center", va="bottom", zorder=4)

    ax.annotate("", xy=(0.66, 1.00 - 0.275), xytext=(0.66, 0.48 - 0.275),
                arrowprops=dict(arrowstyle="<->", color=INK_SECONDARY, lw=0.7),
                zorder=2)
    ax.text(0.69, 0.46, "catalysis lowers\nthe barrier", fontsize=6.3,
            color=INK_SECONDARY, ha="left", va="center", linespacing=1.5)

    ax.set_xlabel("Reaction coordinate")
    ax.set_ylabel("Relative free energy")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.70, 1.05)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    ax.text(0.0, -0.30, NOTE_C, transform=ax.transAxes, fontsize=6.3,
            color=INK_SECONDARY, ha="left", va="top", linespacing=1.5)


def main():
    apply_style()
    fig = plt.figure(figsize=(170 * MM, 132 * MM))
    gs = GridSpec(3, 2, figure=fig, height_ratios=[1.0, 0.40, 1.05],
                  hspace=0.28, wspace=0.16)

    panel_a(fig.add_subplot(gs[0, 0]))
    panel_b(fig.add_subplot(gs[0, 1]))
    note(fig.add_subplot(gs[1, 0]), NOTE_A)
    note(fig.add_subplot(gs[1, 1]), NOTE_B)
    panel_c(fig.add_subplot(gs[2, :]))

    save(fig, "fig6_degradation", OUT)


if __name__ == "__main__":
    main()
