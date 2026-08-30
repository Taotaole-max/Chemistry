from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import fig13_appendix_chain_structures as chains
from style import (C_POLYSACCHARIDE, FIG_W, INK, INK_SECONDARY, apply_style, save)

OUT = Path(__file__).parent / "output"
HBOND = "#c0392b"
chains.DRAW_CAPTIONS = False

def panel_cellulose(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    ax.text(2, 97, "(a) Cellulose: ribbon → sheet → crystal", fontsize=7.3,
            weight="bold", color=INK, ha="left", va="top")

    w, h, gap = 74, 7, 9
    for i in range(3):
        y = 66 - i * (h + gap)
        ax.add_patch(plt.Rectangle((13, y), w, h, facecolor=C_POLYSACCHARIDE,
                                   edgecolor=C_POLYSACCHARIDE, alpha=0.85, zorder=3))
        ax.text(13 + w / 2, y + h / 2, "cellulose chain", fontsize=6,
                color="#ffffff", ha="center", va="center", zorder=4)
        if i < 2:
            for xh in np.linspace(22, 78, 6):
                ax.plot([xh, xh], [y - gap, y], color=HBOND, lw=0.9,
                        linestyle=(0, (1.6, 1.6)), zorder=2)
    ax.text(50, 27, "intra- + inter-chain H-bonds lock the sheet;\n"
                    "sheets stack by van der Waals into the Iα/Iβ crystal —\n"
                    "cohesive energy exceeds the backbone, so it decomposes\n"
                    "near 300 °C before melting",
            fontsize=5.6, color=INK_SECONDARY, ha="center", va="top", linespacing=1.45)

def main():
    apply_style()
    fig, axes = plt.subplots(2, 3, figsize=(FIG_W, 80 / 25.4), layout="constrained")

    panel_cellulose(axes[0][0])
    chains.panel_amylose(axes[0][1], tag="b")
    chains.panel_alginate(axes[0][2], tag="c")
    chains.panel_pha_pla(axes[1][0], tag="d")
    chains.panel_silk(axes[1][1], tag="e")
    chains.panel_collagen(axes[1][2], tag="f")

    save(fig, "fig_higher_order_all", OUT)

if __name__ == "__main__":
    main()
