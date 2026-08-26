"""NR vs SBR 链尺度结构对比（§7.3 案例研究配图，正文图号在 report.md 里赋值）。

静置时两者都是无规卷曲链；受力时 NR 的链段能局部规整排列、结晶成束（应变诱导结晶
SIC），SBR 结构不规整（无规共聚、支化），受力后仍然保持无序——这是 §7.3 记分卡里
"SIC & tear resistance"一行的结构起源。颜色不借用主链化学配色（NR 不是"其他"类的
木质素/核酸，SBR 也不在五类配色里），两条链都用中性灰、靠实线/虚线区分，避免暗示
一个新的第六个颜色类别。附录图（原 Fig 13(f)，现已重新编号）有完整版。

原本这张图还带一个七行定性记分卡（面板 b），现在改成 report.md/report_zh.md 里的
一张原生 Word 表格（Table 5），不再用 matplotlib 画状态圆点——表格比图片更紧凑，
也更符合"结构用图、数据比较用表"的分工。
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from style import INK, INK_MUTED, INK_SECONDARY, MM, apply_style, save

HERE = Path(__file__).parent
OUT = HERE / "output"

NR_COLOUR = "#4a4a47"     # neutral dark grey — solid line
SBR_COLOUR = "#8a8a85"    # neutral mid grey — dashed line (style.C_OTHER)


def panel_tag(ax, text, colour=INK):
    ax.text(0.0, 1.05, text, transform=ax.transAxes, fontsize=7.5,
            weight="bold", color=colour, ha="left", va="bottom")


def chain_bundle(ax, x0, y0, w, h, ordered, colour, linestyle):
    """Schematic chain segments: 'ordered'=True draws aligned, tightly-packed
    wavy strands (crystalline bundle); False draws loosely coiled, out-of-phase
    strands (amorphous). Not to scale — mechanism only, same convention as Fig 3."""
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
    y0, h = 2.0, 15.0
    ax.add_patch(plt.Rectangle((x0, y0), w, h, facecolor="#f7f7f5",
                                edgecolor=INK_MUTED, linewidth=0.6, zorder=2))
    chain_bundle(ax, x0, y0, w, h, ordered, colour, linestyle)
    ax.text(x0 + w / 2, y0 - 2.2, label, fontsize=6.3, color=INK_SECONDARY,
            ha="center", va="top", linespacing=1.2)


def panel_structure(ax):
    ax.set_xlim(0, 106)
    ax.set_ylim(-9.0, 22.5)
    ax.axis("off")
    panel_tag(ax, "Chain-scale origin of SIC: NR vs. SBR, at rest vs. under strain")

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
        ax.annotate("strain", xy=(x + box_w / 2, 17.6), xytext=(x + box_w / 2, 20.6),
                    ha="center", va="bottom", fontsize=6.0, color=INK_SECONDARY,
                    arrowprops=dict(arrowstyle="-|>", color=INK_SECONDARY, lw=0.9))

    ax.plot([xs[1] + box_w + gap / 2] * 2, [1.0, 17.0], color="#dedeD9", lw=0.8, zorder=1)
    ax.text(53.0, -8.5, "Full comparison in the Appendix.",
            fontsize=6.0, color=INK_MUTED, ha="center", va="bottom", style="italic")


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(150 * MM, 46 * MM))
    panel_structure(ax)
    fig.subplots_adjust(top=0.86, bottom=0.14, left=0.01, right=0.99)
    save(fig, "fig8_nr_sbr_comparison", OUT)


if __name__ == "__main__":
    main()
