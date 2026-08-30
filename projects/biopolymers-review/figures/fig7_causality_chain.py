from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle

from style import CLASS_COLOR, INK, INK_SECONDARY, MM, apply_style, save

HERE = Path(__file__).parent
OUT = HERE / "output"

ROWS = [
    ("Cellulose", "polysaccharide",
     "dense inter- & intrachain\nH-bonding, sheet stacking",
     "very high axial modulus\n(~130-150 GPa)",
     "no melt transition —\ndecomposes at ~300 °C"),
    ("Starch / chitosan /\nalginate", "polysaccharide",
     "weaker, ionically or\nchemically tunable forces",
     "tunable solubility,\ngelation, charge",
     "properties drift with\nDD, G-content, humidity"),
    ("PHA (PHB/PHBV)", "polyester",
     "ester backbone, moderate\ncrystallinity (55-70%)",
     "melt-processable\nphase forms",
     "processing window only\n~25-55 °C wide"),
    ("PLA", "polyester",
     "stereochemistry-controlled\nchain packing",
     "stereocomplex Tm\n+50 °C over homocrystal",
     "Tg ceiling ~60 °C;\nslow crystallisation"),
    ("Protein\n(silk, collagen)", "protein",
     "sequence-directed fold,\nnot simple packing",
     "combined strength +\ntoughness (silk); triple helix",
     "irreversible denaturation\ncollapses structure"),
    ("Lignin", "other",
     "random radical coupling,\nno periodic chain",
     "chemically recalcitrant\naromatic network",
     "no single structure-\nproperty relationship"),
    ("Natural rubber", "other",
     "free rotation; strain-\ninduced crystallisation only",
     "self-reinforcing\nelastomer under load",
     "MW & network vary by\nclone and tree age"),
]

COL_X = [0.5, 3.15, 5.75, 8.35]
COL_W = 2.45
HEADERS = ["Family", "Intermolecular force", "Consequence", "Limitation"]

def main():
    apply_style()
    n = len(ROWS)
    row_h = 1.0
    fig_h_mm = 20 + n * 15.5
    fig, ax = plt.subplots(figsize=(170 * MM, fig_h_mm * MM))
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_xlim(0, 10.9)
    ax.set_ylim(-0.15, n + 1.1)
    ax.axis("off")

    for x, h in zip(COL_X, HEADERS):
        ax.text(x, n + 0.55, h, fontsize=7.2, fontweight="bold", color=INK,
                ha="left", va="center")
    ax.plot([0, 10.9], [n + 0.15, n + 0.15], color=INK_SECONDARY, lw=0.8)

    for i, (name, cls, force, consequence, limit) in enumerate(ROWS):
        y = n - i - 0.5
        colour = CLASS_COLOR[cls]

        ax.add_patch(Rectangle((0, y - 0.42), 0.14, 0.84, facecolor=colour,
                                edgecolor="none"))
        ax.text(0.32, y, name, fontsize=7.3, color=INK, ha="left", va="center",
                linespacing=1.25, fontweight="bold")

        for j, text in enumerate((force, consequence, limit)):
            x0 = COL_X[j + 1]
            ax.text(x0, y, text, fontsize=6.6, color=INK_SECONDARY, ha="left",
                     va="center", linespacing=1.3)
            if j < 2:
                arrow_x = x0 + COL_W
                ax.annotate("", xy=(arrow_x + 0.22, y), xytext=(arrow_x - 0.05, y),
                            arrowprops=dict(arrowstyle="-|>", color=colour, lw=1.1,
                                             shrinkA=0, shrinkB=0))

        if i < n - 1:
            ax.plot([0, 10.9], [y - 0.5, y - 0.5], color="#ececea", lw=0.7)

    save(fig, "fig7_causality_chain", OUT)

if __name__ == "__main__":
    main()
