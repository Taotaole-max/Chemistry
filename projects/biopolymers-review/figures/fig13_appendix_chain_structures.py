"""Fig 13 (附录) · 链尺度的空间/构象结构，六个家族各一格。

Fig 3 已经用一整张图讲清楚了纤维素的链→片层→晶体三级结构；这张图补的是 Fig 3
没有覆盖、但正文 §3 反复用来解释性质的"链怎么摆"这件事本身——直链淀粉为什么会
被水增塑（螺旋，不是带状）、海藻酸盐怎么靠 Ca2+ 交联（"蛋盒"结构，正文只提了名字
没画机理）、PHA/PLA 为什么能熔融加工（螺旋堆积，不是带状晶体）、丝素蛋白的强度
韧性从哪来（β-折叠纳米晶体）、胶原蛋白的三螺旋为什么必须每三个残基就有一个甘氨酸、
天然橡胶和 SBR 在应变下到底谁结晶谁不结晶（§7.3 案例研究的结构内核）。

和 Fig 3 一样：全部示意性（matplotlib 手绘几何图形），几何比例不代表真实键长键角/
螺距/晶胞参数，只保证拓扑关系和"谁比谁更规整"这类定性事实正确。不用 RDKit——
这些是链尺度、二级/三级结构层面的排列，RDKit 画的是单个重复单元的原子连接，
两者互补，不是重复。

布局约定（每格严格三段，避免文字互相压字——这张图第一版因为每格塞了 3-4 段
浮动注释文字，在窄格里彼此重叠，返工过一次）：标题固定在顶部；图形本身画在
中段；机理说明只放一处、固定锚在底部同一条基线上，其余想说的话都并进这一段，
不再额外散布浮动短句。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from style import (C_OTHER, C_POLYESTER, C_POLYSACCHARIDE, C_PROTEIN, INK,
                    INK_MUTED, INK_SECONDARY, MM, apply_style, save)

OUT = Path(__file__).parent / "output"

HBOND = "#c0392b"
IONIC = "#b8860b"

CAPTION_TOP_Y = 24  # 每格说明文字的固定锚点（top-anchored，图形区在这条线以上）

# 附录 Fig 19 是独立速查图，每格保留一句机理说明；但正文 §3 复用这些 panel 函数时
# （fig_polysaccharide_chains / fig_polyester_structures / fig_protein_structures）
# 说明文字应该走 Word 图注，不在图上重复——那几个脚本会把这个开关置 False。
DRAW_CAPTIONS = True


def panel_label(ax, tag, title):
    ax.text(2, 97, f"({tag}) {title}", fontsize=7.3, weight="bold",
            color=INK, ha="left", va="top")


def caption(ax, text):
    if not DRAW_CAPTIONS:
        return
    ax.text(50, CAPTION_TOP_Y, text, fontsize=6, color=INK_SECONDARY,
            ha="center", va="top", linespacing=1.45)


def setup(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")


# ---------------------------------------------------------------------------
def panel_amylose(ax, tag="a"):
    setup(ax)
    panel_label(ax, tag, "Amylose: left-handed helix")
    colour = C_POLYSACCHARIDE
    cx = 50
    theta = np.linspace(0, 4.4 * np.pi, 300)
    y = 32 + theta * (56 / theta.max())
    r = 15
    x_front = cx + r * np.sin(theta)
    x_back = cx - r * np.sin(theta)
    ax.plot(x_back, y, color=colour, lw=1.1, alpha=0.35, zorder=2)
    ax.plot(x_front, y, color=colour, lw=1.8, alpha=0.95, zorder=4)
    for t in np.linspace(0.3, 4.2 * np.pi, 9):
        xx = cx + r * np.sin(t)
        yy = 32 + t * (56 / theta.max())
        z = 5 if np.cos(t) > 0 else 2
        a = 0.95 if np.cos(t) > 0 else 0.35
        ax.plot(xx, yy, marker="o", markersize=3.2, color=colour, alpha=a, zorder=z)
    ax.plot([cx, cx], [30, 89], color=INK_MUTED, lw=0.7, linestyle=(0, (1, 1.6)), zorder=1)
    caption(ax, "Left-handed helix — contrast cellulose's extended\n"
                "ribbon (§3.1 figure). I$_2$/water enters the cavity and\n"
                "plasticises the chain (§3.1).")


# ---------------------------------------------------------------------------
def panel_alginate(ax, tag="b"):
    setup(ax)
    panel_label(ax, tag, "Alginate: Ca$^{2+}$ egg-box")
    colour = C_POLYSACCHARIDE
    xs = np.linspace(8, 88, 9)

    def buckled(y0, phase):
        yy = y0 + 7 * np.sin(np.linspace(0, 3.2 * np.pi, len(xs)) + phase)
        return xs, yy

    x1, y1 = buckled(68, 0)
    x2, y2 = buckled(40, np.pi)
    ax.plot(x1, y1, color=colour, lw=1.8, zorder=3)
    ax.plot(x2, y2, color=colour, lw=1.8, zorder=3)
    ax.text(90, 68, "G-block", fontsize=6, color=colour, ha="left", va="center")
    ax.text(90, 40, "G-block", fontsize=6, color=colour, ha="left", va="center")

    for i in range(1, len(xs) - 1, 2):
        cxx, cy = xs[i], (y1[i] + y2[i]) / 2
        ax.plot(cxx, cy, marker="o", markersize=7, color=IONIC, zorder=5,
                markeredgecolor=INK, markeredgewidth=0.4)
        ax.text(cxx, cy, "Ca", fontsize=4.6, color="#ffffff", ha="center",
                va="center", zorder=6, weight="bold")
        for (xa, ya) in [(xs[i], y1[i]), (xs[i], y2[i])]:
            ax.plot([cxx, xa], [cy, ya], color=IONIC, lw=0.8,
                    linestyle=(0, (1.4, 1.2)), zorder=2)
    caption(ax, "Ca$^{2+}$ bridges carboxylate O across two G-block\n"
                "chains — ionic, reversible with a chelator; G-content\n"
                "sets junction density, i.e. stiffness vs. brittleness (§3.1, §8).")


# ---------------------------------------------------------------------------
def panel_pha_pla(ax, tag="c"):
    setup(ax)
    panel_label(ax, tag, "PHA / PLA: helical packing")
    colour = C_POLYESTER
    for k, cx in enumerate([30, 70]):
        theta = np.linspace(0, 3.6 * np.pi, 220)
        y = 28 + theta * (52 / theta.max())
        r = 11
        x_front = cx + r * np.sin(theta)
        x_back = cx - r * np.sin(theta)
        ax.plot(x_back, y, color=colour, lw=1.0, alpha=0.3, zorder=2)
        ax.plot(x_front, y, color=colour, lw=1.6, alpha=0.9, zorder=4)
        label = r"PHB 2$_1$" if k == 0 else r"PLLA 10$_3$"
        ax.text(cx, 83, label, fontsize=6.3, color=colour, ha="center", va="bottom")
    caption(ax, "Helix, not an extended ribbon — crystallises but\n"
                "still melts (§5.1), unlike cellulose's H-bonded\n"
                "ribbon (§3.1), which decomposes before melting (§3.2).")


# ---------------------------------------------------------------------------
def panel_silk(ax, tag="d"):
    setup(ax)
    panel_label(ax, tag, "Silk: β-sheet nanocrystal")
    colour = C_PROTEIN
    xs = np.linspace(10, 66, 11)
    row_y = [78, 62, 46]
    for row, y0 in enumerate(row_y):
        yy = y0 + 3.2 * (np.arange(len(xs)) % 2)
        ax.plot(xs, yy, color=colour, lw=1.5, zorder=3)
        if row < len(row_y) - 1:
            for i in range(0, len(xs), 2):
                ax.plot([xs[i], xs[i]], [y0, row_y[row + 1]], color=HBOND, lw=0.6,
                        linestyle=(0, (1.2, 1.2)), zorder=2)
    ax.annotate("", xy=(70, 62), xytext=(82, 62),
                arrowprops=dict(arrowstyle="-|>", color=INK_SECONDARY, lw=1.0))
    ax.text(84, 62, "Ala CH$_3$\nstacking", fontsize=5.6, color=INK_SECONDARY,
            ha="left", va="center", linespacing=1.3)
    caption(ax, "Antiparallel β-strands, H-bonded (dashed), stack into\n"
                "2–4 nm nanocrystallites in a compliant amorphous\n"
                "matrix — source of silk's strength + toughness (§3.3).")


# ---------------------------------------------------------------------------
def panel_collagen(ax, tag="e"):
    setup(ax)
    panel_label(ax, tag, "Collagen: Gly-X-Y triple helix")
    colour = C_PROTEIN
    cx = 50
    theta = np.linspace(0, 3.4 * np.pi, 260)
    y = 30 + theta * (60 / theta.max())
    r = 13
    for off in (0, 2.09, 4.19):  # 3 strands, 120 deg apart
        x = cx + r * np.sin(theta + off)
        front = np.cos(theta + off) > 0.15
        ax.plot(np.where(front, x, np.nan), y, color=colour, lw=1.6, alpha=0.95, zorder=4)
        ax.plot(np.where(~front, x, np.nan), y, color=colour, lw=1.0, alpha=0.30, zorder=2)
        for t in np.linspace(0.3, 3.3 * np.pi, 7):
            xx = cx + r * np.sin(t + off)
            yy = 30 + t * (60 / theta.max())
            if np.cos(t + off) > 0.15:
                ax.plot(xx, yy, marker="o", markersize=2.6, color=INK, zorder=5)
    caption(ax, "3 left-handed helices supercoiled into a right-handed\n"
                "triple helix; Gly (dots) at every 3rd position is the\n"
                "only residue small enough for the crowded core (§3.3).")


# ---------------------------------------------------------------------------
def _tangle(ax, cx, cy, spread, colour, n=4, seed=0):
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 2 * np.pi, 60)
    for i in range(n):
        r0 = spread * (0.35 + 0.5 * rng.random())
        wob = rng.uniform(1.5, 3.0)
        ph = rng.uniform(0, 6.28)
        x = cx + r0 * np.cos(t + ph) + 0.15 * spread * np.sin(wob * t)
        y = cy + r0 * np.sin(t + ph) + 0.15 * spread * np.cos(wob * t)
        ax.plot(x, y, color=colour, lw=1.0, alpha=0.75, zorder=3)


def panel_sic(ax):
    setup(ax)
    panel_label(ax, "f", "NR vs. SBR: strain crystallisation")
    nr_colour = C_OTHER
    sbr_colour = INK_MUTED

    ax.text(24, 85, "at rest", fontsize=6, weight="bold", color=INK_SECONDARY, ha="center")
    ax.text(76, 85, "under strain", fontsize=6, weight="bold", color=INK_SECONDARY, ha="center")
    ax.plot([50, 50], [28, 82], color=INK_MUTED, lw=0.5, linestyle=(0, (1, 1.6)))
    ax.text(10, 70, "NR", fontsize=6.3, weight="bold", color=nr_colour, ha="left")
    ax.text(10, 40, "SBR", fontsize=6.3, weight="bold", color=sbr_colour, ha="left")

    _tangle(ax, 26, 70, 9, nr_colour, seed=1)
    _tangle(ax, 26, 40, 9, sbr_colour, seed=2)

    for xb in np.linspace(66, 92, 5):
        ax.plot([xb, xb], [64, 76], color=nr_colour, lw=1.6, zorder=3)
    _tangle(ax, 79, 40, 8, sbr_colour, seed=3)

    ax.annotate("", xy=(60, 70), xytext=(38, 70),
                arrowprops=dict(arrowstyle="-|>", color=INK_SECONDARY, lw=1.0))
    ax.annotate("", xy=(60, 40), xytext=(38, 40),
                arrowprops=dict(arrowstyle="-|>", color=INK_SECONDARY, lw=1.0))
    caption(ax, "Stereoregular cis-1,4 NR aligns into crystalline bundles\n"
                "under strain (SIC, X-ray confirmed); SBR's irregular\n"
                "backbone stays amorphous even stretched — core of §7.3.")


def main():
    apply_style()
    fig, axes = plt.subplots(2, 3, figsize=(190 * MM, 128 * MM))

    panel_amylose(axes[0, 0])
    panel_alginate(axes[0, 1])
    panel_pha_pla(axes[0, 2])
    panel_silk(axes[1, 0])
    panel_collagen(axes[1, 1])
    panel_sic(axes[1, 2])

    fig.subplots_adjust(hspace=0.28, wspace=0.18, top=0.97, bottom=0.02,
                        left=0.02, right=0.98)
    save(fig, "fig13_appendix_chain_structures", OUT)


if __name__ == "__main__":
    main()
