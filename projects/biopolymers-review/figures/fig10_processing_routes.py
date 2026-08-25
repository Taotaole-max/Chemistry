"""Fig 10 · 加工路线决策图（§6 的配图）。

§6 原来是一整段密文字：有没有熔融窗口决定走熔融加工还是溶液加工，具体材料举例，
再加一句"拓宽窗口"的通用对策。改成一张判定流程图之后，正文只保留判定逻辑本身
说不清楚、图上放不下的那一句话（多数所谓性能不足其实是加工窗口不足）。
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from style import CLASS_COLOR, INK, INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"


def box(ax, x, y, w, h, text, facecolor, edgecolor, textcolor, fontsize=7.2, weight="normal"):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0,rounding_size=1.4",
        linewidth=0.8, facecolor=facecolor, edgecolor=edgecolor, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize,
            color=textcolor, weight=weight, zorder=3, linespacing=1.25)


def varrow(ax, x, y0, y1, colour=INK_SECONDARY, lw=0.9):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=lw,
                                 shrinkA=0, shrinkB=0), zorder=1)


def diag_arrow(ax, x0, y0, x1, y1, colour=INK_SECONDARY, lw=0.9):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=lw,
                                 shrinkA=0, shrinkB=0,
                                 connectionstyle="angle,angleA=0,angleB=90,rad=3"),
                zorder=1)


def main():
    apply_style()
    W, H = 168.0, 100.0
    fig, ax = plt.subplots(figsize=(W * MM, H * MM))
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    C_poly = CLASS_COLOR["polyester"]
    C_sacc = CLASS_COLOR["polysaccharide"]

    LX, RX, LANE_W = 4.0, 112.0, 52.0
    LX_C, RX_C = LX + LANE_W / 2, RX + LANE_W / 2

    # root question
    box(ax, 44, 84, 80, 14,
        "Does a stable melt window exist above Tm\nand below decomposition/hydrolysis onset? (§5.1)",
        "#f4f4f1", INK_SECONDARY, INK, fontsize=6.9, weight="bold")
    ax.text(LX_C, 79.5, "No", fontsize=7.5, color=INK, weight="bold", ha="center")
    ax.text(RX_C, 79.5, "Yes", fontsize=7.5, color=INK, weight="bold", ha="center")
    diag_arrow(ax, 60, 84, LX_C, 76)
    diag_arrow(ax, 108, 84, RX_C, 76)

    # lane headers
    box(ax, LX, 62, LANE_W, 12, "Solution processing", C_sacc, C_sacc, "#ffffff", weight="bold")
    box(ax, RX, 62, LANE_W, 12, "Melt processing", C_poly, C_poly, "#ffffff", weight="bold")
    varrow(ax, LX_C, 76, 74)
    varrow(ax, RX_C, 76, 74)

    # left lane items (2)
    left_items = [
        (45, "Cellulose → NMMO/Lyocell,\nLiCl/DMAc dissolution"),
        (28, "Chitosan → dilute-acid dissolution,\nwet/dry-jet spinning"),
    ]
    varrow(ax, LX_C, 62, 59)
    for y, text in left_items:
        box(ax, LX, y, LANE_W, 13, text, "#ffffff", C_sacc, INK, fontsize=6.4)
    varrow(ax, LX_C, 45, 42)

    # right lane items (3)
    right_items = [
        (49, "PBS → wide window (~110 °C),\nleast restrictive"),
        (34, "PHB → narrow window (~25 °C),\ntight thermal control"),
        (19, "PLA → must be dried first, or melt\nhydrolysis erodes MW (§4)"),
    ]
    varrow(ax, RX_C, 62, 60)
    for y, text in right_items:
        box(ax, RX, y, LANE_W, 11, text, "#ffffff", C_poly, INK, fontsize=6.1)
    varrow(ax, RX_C, 49, 46)
    varrow(ax, RX_C, 34, 31)

    # convergent countermeasures box
    box(ax, 22, 2, 124, 14,
        "Widen whichever window exists: plasticisers (cost: stiffness) · nucleating agents "
        "(speed PLA crystallisation) ·\ncompatibilised blends (PLA/PBAT, PLA/TPS) · "
        "nanocellulose/nanochitin reinforcement",
        "#f4f4f1", INK_SECONDARY, INK, fontsize=6.4)
    diag_arrow(ax, LX_C, 28, 60, 17)
    diag_arrow(ax, RX_C, 19, 108, 17)

    save(fig, "fig10_processing_routes", OUT)


if __name__ == "__main__":
    main()
