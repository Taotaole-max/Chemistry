"""Fig 3 · 纤维素的三级结构：链内氢键 → 片层内链间氢键 → 片层间堆叠。

这张图要回答一个具体问题：为什么纤维素在到达熔点之前就分解？
答案是三级结构累积起来的内聚能超过了主链键能——分子级、片层级、晶体级各贡献一部分。
图是示意性的（几何比例不代表真实键长键角），晶胞类型是文献事实，晶胞参数不放在图上，
待核对原始中子衍射数据后再补进 Table 1。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle

from style import C_POLYSACCHARIDE, INK, INK_MUTED, INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"

BLUE = C_POLYSACCHARIDE
HBOND = "#c0392b"       # 氢键用暖色，与结构的蓝色区分开
VDW = INK_MUTED


def pyranose(ax, x, y, w=13.0, h=7.0, label=None):
    """简化的吡喃环：一个拉长的六边形，代表椅式糖环。"""
    pts = np.array([
        [x, y + h * 0.5], [x + w * 0.25, y + h], [x + w * 0.75, y + h],
        [x + w, y + h * 0.5], [x + w * 0.75, y], [x + w * 0.25, y],
    ])
    ax.add_patch(Polygon(pts, closed=True, facecolor="#ffffff",
                         edgecolor=BLUE, linewidth=1.1, zorder=3))
    if label:
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=6.5, color=INK_SECONDARY, zorder=4)


def panel_label(ax, x, y, tag, title):
    ax.text(x, y, f"({tag}) {title}", fontsize=7.5, weight="bold",
            color=INK, ha="left", va="bottom")


def main():
    apply_style()
    W, H = 170.0, 66.0
    fig, ax = plt.subplots(figsize=(W * MM, H * MM))
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    # ---- (a) 单链：糖苷键连接 + 链内氢键把链锁成平直带状 ----
    x0, y0 = 2.0, 30.0
    panel_label(ax, x0, 54.0, "a", "Chain: intramolecular H-bonds")
    ax.text(x0, 50.0, "locks the ribbon-like conformation", fontsize=6.5,
            color=INK_SECONDARY, ha="left", va="bottom")

    pyranose(ax, x0, y0, label="C1")
    ax.plot([x0 + 13.0, x0 + 16.5], [y0 + 3.5, y0 + 3.5], color=BLUE, lw=1.1, zorder=3)
    ax.text(x0 + 14.7, y0 + 4.6, "O", fontsize=6.5, color=HBOND, ha="center",
            va="bottom", zorder=4)
    pyranose(ax, x0 + 16.5, y0, label="C4")
    ax.text(x0 + 14.9, y0 - 2.6,
            r"$\beta$(1$\rightarrow$4) glycosidic bond; a second H-bond,"
            "\n" r"O2$-$H$\cdots$O6$'$, further rigidifies the linkage",
            fontsize=6.0, color=INK_SECONDARY, ha="center", va="top", linespacing=1.5)

    # 链内氢键：只画一条清楚的（O3-H...O5'），第二条（O2-H...O6'）改成文字说明，
    # 避免两条括号线和标签在这么窄的面板里彼此压字（这里之前有重叠）
    xa, xb, dy = x0 + 9.5, x0 + 20.0, 9.5
    ax.plot([xa, xb], [y0 + dy, y0 + dy], color=HBOND, lw=0.9,
            linestyle=(0, (1.6, 1.6)), zorder=2)
    ax.plot([xa, xa], [y0 + 7.0, y0 + dy], color=HBOND, lw=0.7, zorder=2)
    ax.plot([xb, xb], [y0 + 7.0, y0 + dy], color=HBOND, lw=0.7, zorder=2)
    ax.text((xa + xb) / 2, y0 + dy + 0.9, r"O3$-$H$\cdots$O5$'$", fontsize=6.2,
            color=HBOND, ha="center", va="bottom")

    # ---- (b) 片层：链间氢键 ----
    x1 = 62.0
    panel_label(ax, x1, 54.0, "b", "Sheet: inter-chain H-bonds")
    ax.text(x1, 50.0, "one hydrogen-bonded plane", fontsize=6.5,
            color=INK_SECONDARY, ha="left", va="bottom")

    ribbon_w, ribbon_h, gap = 40.0, 4.2, 5.6
    for i in range(3):
        y = y0 + 12.0 - i * (ribbon_h + gap)
        ax.add_patch(Rectangle((x1, y), ribbon_w, ribbon_h, facecolor=BLUE,
                               edgecolor=BLUE, alpha=0.85, zorder=3))
        ax.text(x1 + ribbon_w / 2, y + ribbon_h / 2, "cellulose chain",
                fontsize=6.2, color="#ffffff", ha="center", va="center", zorder=4)
        if i < 2:
            for xh in np.linspace(x1 + 5.0, x1 + ribbon_w - 5.0, 5):
                ax.plot([xh, xh], [y - gap, y], color=HBOND, lw=0.9,
                        linestyle=(0, (1.6, 1.6)), zorder=2)
    ax.text(x1 + ribbon_w / 2, y0 - 9.2, r"O6$-$H$\cdots$O3$''$  (in-plane)",
            fontsize=6.2, color=HBOND, ha="center", va="top")

    # ---- (c) 晶体：片层堆叠 ----
    x2 = 118.0
    panel_label(ax, x2, 54.0, "c", "Crystal: stacked sheets")
    ax.text(x2, 50.0,
            "dispersion-dominated stacking; "
            r"I$\alpha$ triclinic (1 chain/cell)," "\n"
            r"I$\beta$ monoclinic (2 chains/cell)",
            fontsize=6.0, color=INK_SECONDARY, ha="left", va="top",
            linespacing=1.5)

    sheet_w, sheet_h = 34.0, 3.4
    for i in range(4):
        y = y0 + 6.0 - i * 6.0
        shift = i * 2.6
        ax.add_patch(Polygon(np.array([
            [x2 + shift, y], [x2 + shift + sheet_w, y],
            [x2 + shift + sheet_w - 5.0, y + sheet_h], [x2 + shift - 5.0, y + sheet_h],
        ]), closed=True, facecolor=BLUE, edgecolor=BLUE, alpha=0.8, zorder=3))
        if i < 3:
            for j, frac in enumerate((0.3, 0.5, 0.7)):
                ax.plot([x2 + shift + sheet_w * frac] * 3,
                        [y - 1.1, y - 1.9, y - 2.7],
                        marker=".", markersize=1.6, linestyle="none",
                        color=VDW, zorder=4)
    ax.text(x2 + sheet_w / 2 + 4.0, 17.0,
            "van der Waals / CH$\\cdots$O stacking", fontsize=6.2, color=VDW,
            ha="center", va="top")
    # ---- 结论条 ----
    ax.add_patch(FancyBboxPatch(
        (2.0, 1.5), W - 4.0, 12.5,
        boxstyle="round,pad=0,rounding_size=1.2",
        facecolor="#f4f4f1", edgecolor=INK_SECONDARY, linewidth=0.6, zorder=1))
    ax.text(W / 2, 7.75,
            "Cohesive energy accumulated over (a)–(c) exceeds the strength of the glycosidic backbone.\n"
            "Cellulose therefore decomposes near 300 °C before any melting transition is reached, and\n"
            "dissolves only in solvents that can break the hydrogen-bond network.",
            fontsize=6.3, color=INK, ha="center", va="center", linespacing=1.6, zorder=2)

    save(fig, "fig3_cellulose_hierarchy", OUT)


if __name__ == "__main__":
    main()
