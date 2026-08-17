"""Fig 1 · 生物聚合物分类树：来源（三支）× 主链化学（叶子颜色）。

两个分类轴同时呈现：横向层级是来源，叶子底色是主链化学类别。
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from style import (CLASS_COLOR, INK, INK_SECONDARY, MM, apply_style, save)

OUT = Path(__file__).parent / "output"

# (来源分支, [(材料名, 主链类别), ...])
BRANCHES = [
    ("Extracted from biomass", [
        ("Cellulose", "polysaccharide"),
        ("Starch", "polysaccharide"),
        ("Chitin / chitosan", "polysaccharide"),
        ("Alginate", "polysaccharide"),
        ("Collagen / gelatin", "protein"),
        ("Silk fibroin", "protein"),
        ("Lignin", "other"),
        ("Natural rubber", "other"),
    ]),
    ("Synthesised by\nmicro-organisms", [
        ("PHAs (PHB, PHBV)", "polyester"),
        ("Bacterial cellulose", "polysaccharide"),
        ("Xanthan", "polysaccharide"),
    ]),
    ("Polymerised from\nbio-based monomers", [
        ("PLA", "polyester"),
        ("PBS", "polyester"),
        ("PEF", "polyester"),
        ("Bio-based PE", "other"),
    ]),
]

LEGEND = [
    ("Polysaccharide", "polysaccharide"),
    ("Polyester", "polyester"),
    ("Polypeptide", "protein"),
    ("Other backbone", "other"),
]

ROW = 6.2       # 每片叶子的行高 (mm)
LEAF_W = 50.0   # 叶子框宽 (mm)
LEAF_X = 96.0   # 叶子框左边界 (mm)
BRANCH_X = 38.0
BRANCH_W = 50.0
ROOT_X = 2.0
ROOT_W = 30.0


def box(ax, x, y, w, h, text, facecolor, edgecolor, textcolor, weight="normal"):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=1.2",
        linewidth=0.7, facecolor=facecolor, edgecolor=edgecolor, zorder=2,
    ))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=7.5, color=textcolor, weight=weight, zorder=3, linespacing=1.25)


def elbow(ax, x0, y0, x1, y1):
    """直角连接线：先水平出到中点，再竖直，再水平进入。"""
    xm = (x0 + x1) / 2
    ax.plot([x0, xm, xm, x1], [y0, y0, y1, y1],
            color=INK_SECONDARY, linewidth=0.6, solid_capstyle="butt", zorder=1)


def main():
    apply_style()

    n_leaves = sum(len(leaves) for _, leaves in BRANCHES)
    height = n_leaves * ROW + 14
    width = 170.0

    fig, ax = plt.subplots(figsize=(width * MM, height * MM))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis("off")

    # 叶子自上而下排布
    y_cursor = height - 10.0
    branch_centres = []
    for _, leaves in BRANCHES:
        ys = []
        for name, klass in leaves:
            y = y_cursor - ROW
            colour = CLASS_COLOR[klass]
            box(ax, LEAF_X, y + 0.6, LEAF_W, ROW - 1.6, name,
                facecolor=colour, edgecolor=colour, textcolor="#ffffff")
            ys.append(y + ROW / 2 - 0.2)
            y_cursor -= ROW
        y_cursor -= 2.0  # 分支之间留白
        branch_centres.append((sum(ys) / len(ys), ys))

    # 来源分支框 + 连线
    root_y = sum(c for c, _ in branch_centres) / len(branch_centres)
    for (label, _), (centre, leaf_ys) in zip(BRANCHES, branch_centres):
        h = 11.0
        box(ax, BRANCH_X, centre - h / 2, BRANCH_W, h, label,
            facecolor="#f4f4f1", edgecolor=INK_SECONDARY, textcolor=INK)
        for ly in leaf_ys:
            elbow(ax, BRANCH_X + BRANCH_W, centre, LEAF_X, ly)
        elbow(ax, ROOT_X + ROOT_W, root_y, BRANCH_X, centre)

    box(ax, ROOT_X, root_y - 5.5, ROOT_W, 11.0, "Biopolymers",
        facecolor=INK, edgecolor=INK, textcolor="#ffffff", weight="bold")

    # 图例：主链化学类别（叶子颜色的含义），放在左下角空白处，竖排避免标签相撞
    lx = ROOT_X
    ly = 4.0 + len(LEGEND) * 4.4
    ax.text(lx, ly + 4.4, "Backbone chemistry", fontsize=7, color=INK,
            ha="left", va="center", weight="bold")
    for label, klass in LEGEND:
        ax.add_patch(FancyBboxPatch(
            (lx, ly - 1.3), 3.2, 2.6,
            boxstyle="round,pad=0,rounding_size=0.6",
            linewidth=0, facecolor=CLASS_COLOR[klass], zorder=2))
        ax.text(lx + 4.6, ly, label, fontsize=7, color=INK_SECONDARY,
                ha="left", va="center")
        ly -= 4.4

    save(fig, "fig1_classification", OUT)


if __name__ == "__main__":
    main()
