"""=== Word Figure 5 ===  §3.1 多糖链尺度结构：直链淀粉左手螺旋、海藻酸盐 Ca2+ 蛋盒、
壳聚糖的无序化。

前两格复用 fig13_appendix_chain_structures.py 里的 panel_amylose / panel_alginate
（同一份代码）；第三格（壳聚糖）是新画的纯示意几何，不涉及立体化学核对。
纤维素的链尺度结构已单独成图（Word Fig 4），这里不重复。

排版：170 mm 通栏、三格等宽、H_M 高度、constrained layout。机理说明关掉，走 Word 图注；
附录 Fig 19(a)(b) 保留说明。
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import fig13_appendix_chain_structures as chains
from style import C_POLYSACCHARIDE, FIG_W, H_M, INK, apply_style, save

OUT = Path(__file__).parent / "output"

chains.DRAW_CAPTIONS = False


def panel_chitosan(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    ax.text(2, 97, "(c) Chitosan: disrupted H-bond network", fontsize=7.3,
            weight="bold", color=INK, ha="left", va="top")

    colour = C_POLYSACCHARIDE
    rng = np.random.default_rng(7)
    xs = np.linspace(6, 94, 13)
    ys = 52 + 6 * np.sin(np.linspace(0, 2.6 * np.pi, len(xs)))
    ax.plot(xs, ys, color=colour, lw=1.8, zorder=3)

    acetylated = rng.choice(len(xs), size=5, replace=False)
    for i, (x, y) in enumerate(zip(xs, ys)):
        if i in acetylated:
            ax.plot([x, x], [y, y + 10], color="#b8860b", lw=1.1, zorder=3)
            ax.text(x, y + 11.5, "Ac", fontsize=5.2, color="#b8860b",
                    ha="center", va="bottom")
        else:
            ax.plot([x, x], [y, y + 10], color=colour, lw=1.1, zorder=3, alpha=0.55)
            ax.text(x, y + 11.5, "NH$_2$", fontsize=5.0, color=colour,
                    ha="center", va="bottom", alpha=0.75)


def main():
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(FIG_W, H_M / 25.4), layout="constrained")

    chains.panel_amylose(axes[0])
    chains.panel_alginate(axes[1])
    panel_chitosan(axes[2])

    save(fig, "fig_polysaccharide_chains", OUT)


if __name__ == "__main__":
    main()
