"""§3.1 多糖链尺度结构：直链淀粉左手螺旋、海藻酸盐 Ca2+ 蛋盒、壳聚糖的无序化。

前两格直接复用 fig13_appendix_chain_structures.py 里已经画好的 panel_amylose /
panel_alginate 函数（同一份代码，不重复实现）；第三格（壳聚糖）是新画的示意——
纯粹示意几何，不涉及立体化学核对（和 Fig 3/Fig 13 的既有约定一致）。
纤维素的链尺度结构已经单独成图（原 Fig 3，现为 Fig 4），这里不重复。
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from fig13_appendix_chain_structures import panel_alginate, panel_amylose
from style import C_POLYSACCHARIDE, INK, INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"


def panel_chitosan(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    ax.text(2, 97, "(c) Chitosan: disrupted H-bond network", fontsize=7.3,
            weight="bold", color=INK, ha="left", va="top")

    colour = C_POLYSACCHARIDE
    rng = np.random.default_rng(7)
    xs = np.linspace(6, 94, 13)
    y0 = 55
    ys = y0 + 6 * np.sin(np.linspace(0, 2.6 * np.pi, len(xs)))
    ax.plot(xs, ys, color=colour, lw=1.8, zorder=3)

    # 随机撒 NH2/NHAc 取代基，标出乙酰化位点打断了规则的 H 键网络
    acetylated = rng.choice(len(xs), size=5, replace=False)
    for i, (x, y) in enumerate(zip(xs, ys)):
        if i in acetylated:
            ax.plot([x, x], [y, y + 9], color="#b8860b", lw=1.1, zorder=3)
            ax.text(x, y + 10.5, "Ac", fontsize=5.2, color="#b8860b",
                    ha="center", va="bottom")
        else:
            ax.plot([x, x], [y, y + 9], color=colour, lw=1.1, zorder=3, alpha=0.55)
            ax.text(x, y + 10.5, "NH$_2$", fontsize=5.0, color=colour,
                    ha="center", va="bottom", alpha=0.75)

    ax.text(50, 22, "irregular DD (degree of deacetylation) breaks up the\n"
                     "regular H-bond register cellulose relies on (§3.1) —\n"
                     "solubility rises but crystallinity falls (§3.1)",
            fontsize=6.0, color=INK_SECONDARY, ha="center", va="top", linespacing=1.5)


def main():
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(170 * MM, 62 * MM))

    panel_amylose(axes[0])
    panel_alginate(axes[1])
    panel_chitosan(axes[2])

    fig.subplots_adjust(top=0.94, bottom=0.03, left=0.02, right=0.98, wspace=0.18)
    save(fig, "fig_polysaccharide_chains", OUT)


if __name__ == "__main__":
    main()
