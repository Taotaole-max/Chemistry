"""Fig 8 · 天然橡胶 vs SBR 案例研究一览（§7.3 总览图）。

不用编造出来的雷达图数值，而是一张"记分卡"：每个维度给 NR 和 SBR 各一个定性状态
（有利 / 取决于配方或场景 / 有据可查的风险或代价），配一句极短的落地陈述和引用编号。
颜色是状态色，不是主链化学分类色，图内单独给了图例避免和其他图的配色混淆。
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from style import INK, INK_SECONDARY, MM, apply_style, save

HERE = Path(__file__).parent
OUT = HERE / "output"

GOOD = "#2e8b57"
MIXED = "#d99a2b"
RISK = "#c94f4f"

# (dimension, NR status, NR note (2 lines), NR ref, SBR status, SBR note (2 lines), SBR ref)
ROWS = [
    ("Structure /\nMW control", MIXED, "extracted; varies by\nclone & tree age", "19",
     GOOD, "engineered via emulsion/\nsolution copolymerisation", "20,21"),
    ("SIC & tear\nresistance", GOOD, "strong strain-induced\ncrystallisation", "10,23",
     MIXED, "crystallises far less;\nrelies on filler/cure", "24"),
    ("Blend\nperformance", MIXED, "SIC weakens as SBR\nfraction rises", "22",
     MIXED, "reaches parity via\nreinforcement, not backbone", "24"),
    ("Tg / cure\nnetwork", MIXED, "depends on formulation\n& cure conditions", "25,26",
     MIXED, "depends on formulation\n& cure conditions", "25,26"),
    ("Bio-\ncompatibility", MIXED, "real potential, but latex\nprotein allergy risk", "27,28",
     RISK, "no unconditional\nbiocompatibility claim", "27,28"),
    ("Environmental\nfootprint", MIXED, "renewable, but LCA shows\nreal land/energy cost", "29,30",
     RISK, "fossil feedstock;\nbiodegradable grades emerging", "31"),
    ("Price\nstability", RISK, "historically the more\nvolatile of the two", "32",
     MIXED, "steadier, but tied to\npetrochemical supply chain", "32"),
]

LABEL_W = 1.9
COL_W = 3.3
GAP = 0.7
COL_X = [LABEL_W + 0.15, LABEL_W + 0.15 + COL_W + GAP]
HEADERS = ["", "Natural rubber (NR)", "SBR"]


def main():
    apply_style()
    n = len(ROWS)
    fig_h_mm = 22 + n * 15.5
    fig, ax = plt.subplots(figsize=(170 * MM, fig_h_mm * MM))
    total_w = COL_X[1] + COL_W + 0.2
    ax.set_xlim(0, total_w)
    ax.set_ylim(-1.3, n + 1.1)
    ax.axis("off")

    for x, h in zip(COL_X, HEADERS[1:]):
        ax.text(x + 0.28, n + 0.55, h, fontsize=7.4, fontweight="bold", color=INK,
                ha="left", va="center")
    ax.plot([0, total_w], [n + 0.15, n + 0.15], color=INK_SECONDARY, lw=0.8)

    for i, (dim, c1, t1, r1, c2, t2, r2) in enumerate(ROWS):
        y = n - i - 0.5
        ax.text(0, y, dim, fontsize=6.9, color=INK, ha="left", va="center",
                 fontweight="bold", linespacing=1.2)

        for x, colour, text, ref in ((COL_X[0], c1, t1, r1), (COL_X[1], c2, t2, r2)):
            ax.add_patch(Circle((x + 0.09, y), 0.09, facecolor=colour, edgecolor="none"))
            ax.text(x + 0.28, y, f"{text} [{ref}]", fontsize=6.4, color=INK_SECONDARY,
                     ha="left", va="center", linespacing=1.25,
                     wrap=True)

        if i < n - 1:
            ax.plot([0, total_w], [y - 0.5, y - 0.5], color="#ececea", lw=0.7)

    legend_y = -0.75
    for dx, colour, label in (
        (0.0, GOOD, "structurally favourable"),
        (3.3, MIXED, "formulation- or context-dependent"),
        (7.7, RISK, "documented risk or caveat"),
    ):
        ax.add_patch(Circle((dx + 0.09, legend_y), 0.09, facecolor=colour, edgecolor="none"))
        ax.text(dx + 0.28, legend_y, label, fontsize=6.3, color=INK_SECONDARY,
                 ha="left", va="center")

    save(fig, "fig8_nr_sbr_comparison", OUT)


if __name__ == "__main__":
    main()
