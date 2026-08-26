"""Fig 6/7/8（原 Fig 6 的三个面板）· 两条降解路径与酯水解的能量图（示意），拆成三张
独立的图，各自有完整图注和独立图号，不再挤在一张图的三个子面板里。

(a) → 独立输出 fig6a_polyester_hydrolysis：聚酯主链酯键水解，产物含羧基端，羧基降低
    局部 pH 反过来加速水解——自催化，因此厚制品从内部先坏，表现为本体侵蚀而不是表面侵蚀。
(b) → 独立输出 fig6b_enzymatic_degradation：多糖与蛋白的酶解，酶只能接触无定形区，
    结晶区把酶挡在外面，所以结晶度直接设定降解速率——同一个结晶度既给强度、又挡水、
    也挡降解。
(c) → 独立输出 fig6c_hydrolysis_barriers：酯水解三种条件的能垒次序（示意图，不含
    计算值）：碱催化 < 酸催化 < 中性水，用线型区分路径、颜色沿用聚酯的橙色。

图内注释压到最短——正文 §5.4 已经把这三段机理讲清楚了，图上只留一句话当标签，
不重复解释，避免图文冗余。三张图各自的正文图号在 report.md / report_zh.md 里赋值，
本脚本内部仍按 a/b/c 组织便于维护，但绘图函数名保留、只是分别单独 save()。
"""

import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
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

NOTE_A = "Acid end product autocatalyses further hydrolysis — bulk erosion."
NOTE_B = "Enzymes reach only amorphous regions — crystallinity sets the rate."
NOTE_C = "Ordering only — no calculated values implied."


def title(ax, text, colour):
    ax.text(0.0, 1.06, text, transform=ax.transAxes, fontsize=7.5,
            weight="bold", color=colour, ha="left", va="bottom")


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
    title(ax, "Polyesters: backbone hydrolysis", C_POLYESTER)
    ax.text(0.0, -0.06, NOTE_A, transform=ax.transAxes, fontsize=6.5,
            color=INK, ha="left", va="top", linespacing=1.5)


def panel_b(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 / PANEL_ASPECT)
    ax.axis("off")
    title(ax, "Polysaccharides and proteins: enzymatic attack", C_POLYSACCHARIDE)

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

    ax.text(0.0, -0.10, NOTE_B, transform=ax.transAxes, fontsize=6.5,
            color=INK, ha="left", va="top", linespacing=1.5)


def profile(barrier):
    x = np.linspace(0, 1, 400)
    return x, barrier * np.exp(-((x - 0.5) ** 2) / 0.012) - 0.55 * x


def panel_c(ax):
    title(ax, "Relative barriers for ester hydrolysis (schematic)", C_POLYESTER)

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

    ax.text(0.0, -0.16, NOTE_C, transform=ax.transAxes, fontsize=6.3,
            color=INK_SECONDARY, ha="left", va="top", linespacing=1.5)


def main():
    apply_style()

    fig_a = plt.figure(figsize=(100 * MM, 44 * MM))
    panel_a(fig_a.add_subplot(1, 1, 1))
    fig_a.subplots_adjust(top=0.80, bottom=0.30, left=0.02, right=0.98)
    save(fig_a, "fig6a_polyester_hydrolysis", OUT)

    fig_b = plt.figure(figsize=(100 * MM, 44 * MM))
    panel_b(fig_b.add_subplot(1, 1, 1))
    fig_b.subplots_adjust(top=0.80, bottom=0.30, left=0.02, right=0.98)
    save(fig_b, "fig6b_enzymatic_degradation", OUT)

    fig_c = plt.figure(figsize=(120 * MM, 78 * MM))
    panel_c(fig_c.add_subplot(1, 1, 1))
    fig_c.subplots_adjust(top=0.88, bottom=0.20)
    save(fig_c, "fig6c_hydrolysis_barriers", OUT)


if __name__ == "__main__":
    main()
