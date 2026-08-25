"""Fig 9 · 分散度 (Đ) 跨家族对比（§4 / Table 3 的配图）。

把 Table 3 里散在文字和表格里的 Đ 范围画成一条线一眼看的图，蛋白质/核酸精确等于
1.00（模板合成），天然橡胶没有可靠的文献定量值，画成开口箭头并在图上明确写"未定量"
——不编造精度。放这张图之后，Table 3 就不用再重复 Đ 这一列，只留 Mn 和测量方法/局限。
"""

from pathlib import Path

import matplotlib.pyplot as plt

from style import CLASS_COLOR, INK, INK_MUTED, INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"

# (material, class, D_low, D_high, note)  D_high=None -> open-ended (unquantified)
ROWS = [
    ("Natural rubber", "other", 2.0, None, "clone- and age-dependent, not\nconsistently quantified"),
    ("PLA", "polyester", 1.1, 2.5, "near-living to broad,\ncatalyst-dependent"),
    ("PHA (PHB/PHBV)", "polyester", 1.5, 3.0, None),
    ("Chitosan", "polysaccharide", 1.5, 5.0, None),
    ("Cellulose (regenerated)", "polysaccharide", 1.5, 3.0, "native cellulose is broader\nand rarely quantified"),
    ("Protein / DNA / RNA", "protein", 1.0, 1.0, "template-synthesised —\nexact, not a range"),
]


def main():
    apply_style()
    n = len(ROWS)
    fig, ax = plt.subplots(figsize=(170 * MM, (14 * n + 22) * MM))

    for i, (name, cls, lo, hi, note) in enumerate(ROWS):
        colour = CLASS_COLOR[cls]
        if hi is None:
            ax.plot([lo, lo + 1.4], [i, i], color=colour, lw=3.0,
                    solid_capstyle="round", zorder=2)
            ax.annotate("", xy=(lo + 1.75, i), xytext=(lo + 1.4, i),
                        arrowprops=dict(arrowstyle="-|>", color=colour, lw=1.4),
                        zorder=2)
        elif lo == hi:
            ax.plot([lo], [i], marker="o", markersize=7, markerfacecolor=colour,
                    markeredgecolor=colour, zorder=3)
        else:
            ax.plot([lo, hi], [i, i], color=colour, lw=3.0,
                    solid_capstyle="round", zorder=2)
            ax.plot([lo, hi], [i, i], marker="|", markersize=8,
                    markeredgewidth=1.4, color=colour, linestyle="none", zorder=3)

        if note:
            label_x = (lo + 1.75) if hi is None else max(lo, hi) + 0.15
            ax.text(label_x, i, note, fontsize=6.0, color=INK_SECONDARY,
                    ha="left", va="center", linespacing=1.3)

    ax.axvline(1.0, color=INK_MUTED, lw=0.7, linestyle=(0, (2, 2)), zorder=1)
    ax.text(1.0, n - 0.15, "Đ = 1\n(monodisperse)", fontsize=6.0, color=INK_MUTED,
            ha="center", va="bottom", linespacing=1.2)

    ax.set_yticks(range(n))
    ax.set_yticklabels([r[0] for r in ROWS], fontsize=7.3)
    ax.set_xlabel("Dispersity Đ = Mw / Mn")
    ax.set_xlim(0.7, 8.6)
    ax.set_ylim(-0.8, n - 0.1)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.grid(axis="x", zorder=0)
    ax.set_axisbelow(True)

    ax.text(0.0, 1.05,
            "Colour: blue = polysaccharide, orange = polyester, green = protein, "
            "grey = other backbone. Open arrow = no reliable\nliterature range exists; "
            "ranges reproduce those stated in Table 3, not new measurements.",
            transform=ax.transAxes, fontsize=6.3, color=INK_SECONDARY,
            ha="left", va="bottom", linespacing=1.5)

    save(fig, "fig9_dispersity", OUT)


if __name__ == "__main__":
    main()
