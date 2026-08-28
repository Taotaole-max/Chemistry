"""=== Word Figure 15 ===  §7.3 案例研究：NR vs SBR 的结构基础。

上排：三个重复单元——NR（cis-1,4-聚异戊二烯）、SBR 的 1,4-丁二烯单元、SBR 的苯乙烯
单元。SBR 这两个共聚单体原来只在附录出现，附录删掉后并进这里。
下排：链尺度对比——静置时两者都是无规卷曲；受力时 NR 的规整链段局部结晶成束
（应变诱导结晶 SIC），SBR 无规共聚 + 支化，受力后仍无序。这是 Table 5 里
"SIC & tear resistance"一行的结构起源。

颜色：NR/SBR 不套主链化学五色（都不属于那五类），两条链用中性深/浅灰、靠实线/虚线
区分，不暗示第六个颜色类别。图内不写大标题——进 Word 图注。
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import verify_appendix_stereochemistry
from fig12_appendix_monomers import PANELS as FIG12_PANELS
from style import (FIG_W, FS_PANEL_SUB, H_L, INK, INK_MUTED, INK_SECONDARY,
                   apply_style, draw_mol, panel_title, save)

HERE = Path(__file__).parent
OUT = HERE / "output"
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}

NR_COLOUR = "#4a4a47"
SBR_COLOUR = "#8a8a85"

MONOMERS = [
    ("a", "Natural rubber", "Natural rubber"),
    ("b", "SBR: butadiene", "SBR: butadiene"),
    ("c", "SBR: styrene", "SBR: styrene"),
]


def chain_bundle(ax, x0, y0, w, h, ordered, colour, linestyle):
    n_strands = 5
    xs = np.linspace(x0 + 0.5, x0 + w - 0.5, 50)
    for k in range(n_strands):
        y_base = y0 + h * (k + 0.5) / n_strands
        rng = np.random.default_rng(seed=k + (1 if ordered else 100))
        if ordered:
            ys = y_base + 0.30 * np.sin(2.6 * (xs - x0))
        else:
            phase = rng.uniform(0, 2 * np.pi)
            ys = (y_base
                  + 0.55 * (h / n_strands) * np.sin(1.3 * (xs - x0) + phase)
                  + 0.25 * (h / n_strands) * np.sin(3.1 * (xs - x0) + phase * 1.6))
        ax.plot(xs, ys, color=colour, lw=1.1, linestyle=linestyle,
                solid_capstyle="round", zorder=3)


def structure_box(ax, x0, w, label, ordered, colour, linestyle):
    y0, h = 3.0, 15.0
    ax.add_patch(plt.Rectangle((x0, y0), w, h, facecolor="#f7f7f5",
                               edgecolor=INK_MUTED, linewidth=0.6, zorder=2))
    chain_bundle(ax, x0, y0, w, h, ordered, colour, linestyle)
    ax.text(x0 + w / 2, y0 - 1.6, label, fontsize=FS_PANEL_SUB, color=INK_SECONDARY,
            ha="center", va="top", linespacing=1.2)


def panel_structure(ax):
    ax.set_xlim(0, 106)
    ax.set_ylim(-6.0, 24.0)
    ax.axis("off")
    ax.text(0.0, 1.0, "(d) Chain scale: at rest vs. under strain",
            transform=ax.transAxes, fontsize=8, fontweight="bold", color=INK,
            ha="left", va="top")

    box_w, gap = 19.0, 6.0
    xs = [2.0, 2.0 + box_w + gap, 2.0 + 2 * (box_w + gap) + 8.0,
          2.0 + 3 * (box_w + gap) + 8.0]

    structure_box(ax, xs[0], box_w, "NR — at rest\n(amorphous coil)",
                  False, NR_COLOUR, "-")
    structure_box(ax, xs[1], box_w, "NR — strained\n(SIC: aligned crystallites)",
                  True, NR_COLOUR, "-")
    structure_box(ax, xs[2], box_w, "SBR — at rest\n(amorphous coil)",
                  False, SBR_COLOUR, (0, (3, 2)))
    structure_box(ax, xs[3], box_w, "SBR — strained\n(stays amorphous)",
                  False, SBR_COLOUR, (0, (3, 2)))

    for x in (xs[1], xs[3]):
        ax.annotate("strain", xy=(x + box_w / 2, 18.6), xytext=(x + box_w / 2, 22.0),
                    ha="center", va="bottom", fontsize=6.0, color=INK_SECONDARY,
                    arrowprops=dict(arrowstyle="-|>", color=INK_SECONDARY, lw=0.9))
    ax.plot([xs[1] + box_w + gap / 2] * 2, [2.0, 18.0], color="#deded9", lw=0.8, zorder=1)


def main():
    verify_appendix_stereochemistry.main()

    apply_style()
    fig = plt.figure(figsize=(FIG_W, H_L / 25.4), layout="constrained")
    gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 1.25])

    for j, (tag, key, name) in enumerate(MONOMERS):
        ax = fig.add_subplot(gs[0, j])
        _, _n, _chem, smiles, _colour, _annotate = BY_NAME_12[key]
        ax.imshow(draw_mol(smiles, annotate_cip=False))
        ax.axis("off")
        panel_title(ax, tag, name, INK_SECONDARY)

    panel_structure(fig.add_subplot(gs[1, :]))
    save(fig, "fig8_nr_sbr_comparison", OUT)


if __name__ == "__main__":
    main()
