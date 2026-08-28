"""=== Word Figure 1 ===  生物聚合物分类：主链化学（主分支）× 来源（叶子标签）。

上一版把"来源"（提取/微生物/单体聚合）当第一层分支、主链化学只做叶子颜色——
和正文 §2 的论断正好反了："origin predicts behaviour poorly ... the repeating
linkage ... is the better predictor ... this review is organised on that
basis"。这一版把主链化学类别改成第一层分支（和 Table 1 / Fig 7 的五类完全对齐），
来源退成每个叶子上的一个小标签（E/M/S），只保留正文 §3 里实际讨论过的材料，
不再引入 bacterial cellulose、xanthan、PEF、bio-based PE 等正文没展开的旁支。
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from style import CLASS_COLOR, INK, INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"

# (branch label, class color key, [(material, origin_tag), ...])
BRANCHES = [
    ("Polysaccharide", "polysaccharide", [
        ("Cellulose", "E"),
        ("Starch", "E"),
        ("Chitosan", "E"),
        ("Alginate", "E"),
    ]),
    ("Polyester", "polyester", [
        ("PHA (PHB, PHBV)", "M"),
        ("PLA", "S"),
    ]),
    ("Protein", "protein", [
        ("Silk fibroin", "E"),
        ("Collagen / gelatin", "E"),
    ]),
    ("Polyphenolic", "other", [
        ("Lignin", "E"),
    ]),
    ("Polyisoprene", "other", [
        ("Natural rubber", "E"),
    ]),
]

ORIGIN_LEGEND = [
    ("E", "Extracted from biomass"),
    ("M", "Microbially synthesised"),
    ("S", "From bio-based monomers"),
]

ROW = 6.4
LEAF_W = 54.0
LEAF_X = 88.0
BRANCH_X = 30.0
BRANCH_W = 50.0
ROOT_X = 2.0
ROOT_W = 24.0
TAG_D = 4.6  # 来源标签小圆的直径
BRANCH_GAP = 5.0  # 单叶分支的分支框高 11mm，间距要够大才不重叠


def box(ax, x, y, w, h, text, facecolor, edgecolor, textcolor, weight="normal", fontsize=7.5):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=1.2",
        linewidth=0.7, facecolor=facecolor, edgecolor=edgecolor, zorder=2,
    ))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=textcolor, weight=weight, zorder=3, linespacing=1.2)


def elbow(ax, x0, y0, x1, y1, colour):
    xm = (x0 + x1) / 2
    ax.plot([x0, xm, xm, x1], [y0, y0, y1, y1],
            color=colour, linewidth=0.7, solid_capstyle="butt", zorder=1)


def main():
    apply_style()

    n_leaves = sum(len(leaves) for _, _, leaves in BRANCHES)
    n_branches = len(BRANCHES)
    LEGEND_H = 13.0  # 图底部整行图例专用条带，不再和树重叠
    height = n_leaves * ROW + (n_branches - 1) * BRANCH_GAP + 16.0 + LEGEND_H
    content_w = 150.0  # data 坐标横向范围：树到 ~144，底部图例三项到 ~140，留点余量

    # 图物理宽度锁死 170 mm（通栏），data 坐标 0..content_w 映射到整宽 → 内容占满、
    # 高度按比例缩放。轻微横向拉伸对示意树不可见。
    fig, ax = plt.subplots(figsize=(170 * MM, 170 * MM * height / content_w))
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_xlim(0, content_w)
    ax.set_ylim(0, height)
    ax.axis("off")

    y_cursor = height - 16.0
    branch_centres = []
    for label, cls, leaves in BRANCHES:
        colour = CLASS_COLOR[cls]
        ys = []
        for name, origin in leaves:
            y = y_cursor - ROW
            box(ax, LEAF_X, y + 0.7, LEAF_W, ROW - 1.8, name,
                facecolor="#ffffff", edgecolor=colour, textcolor=INK)
            # thin colour bar on the leaf's left edge, ties it back to the branch
            ax.add_patch(FancyBboxPatch(
                (LEAF_X, y + 0.7), 1.6, ROW - 1.8,
                boxstyle="round,pad=0,rounding_size=0.5",
                linewidth=0, facecolor=colour, zorder=3))
            # origin tag: small filled circle + letter, top-right corner of the leaf
            tx, ty = LEAF_X + LEAF_W - TAG_D / 2 - 0.6, y + ROW - 1.6
            ax.add_patch(plt.Circle((tx, ty), TAG_D / 2, facecolor=INK,
                                     edgecolor="none", zorder=4))
            ax.text(tx, ty, origin, ha="center", va="center", fontsize=5.6,
                    color="#ffffff", weight="bold", zorder=5)
            ys.append(y + ROW / 2 - 0.2)
            y_cursor -= ROW
        y_cursor -= BRANCH_GAP

        h = 11.0
        centre = sum(ys) / len(ys)
        box(ax, BRANCH_X, centre - h / 2, BRANCH_W, h, label,
            facecolor=colour, edgecolor=colour, textcolor="#ffffff", weight="bold")
        for ly in ys:
            elbow(ax, BRANCH_X + BRANCH_W, centre, LEAF_X, ly, colour)
        branch_centres.append((centre, colour))

    root_y = sum(c for c, _ in branch_centres) / len(branch_centres)
    for centre, colour in branch_centres:
        elbow(ax, ROOT_X + ROOT_W, root_y, BRANCH_X, centre, INK_SECONDARY)
    box(ax, ROOT_X, root_y - 5.5, ROOT_W, 11.0, "Biopolymers",
        facecolor=INK, edgecolor=INK, textcolor="#ffffff", weight="bold", fontsize=7.2)

    # legend: origin tags, one horizontal strip below the whole tree (own reserved band)
    ly = LEGEND_H / 2 + 1.0
    ax.text(ROOT_X, ly, "Origin\n(leaf tag)", fontsize=6.8, color=INK,
            ha="left", va="center", weight="bold", linespacing=1.15)
    lx = ROOT_X + 22.0
    for tag, label in ORIGIN_LEGEND:
        ax.add_patch(plt.Circle((lx, ly), 2.1, facecolor=INK,
                                 edgecolor="none", zorder=2))
        ax.text(lx, ly, tag, ha="center", va="center", fontsize=5.6,
                color="#ffffff", weight="bold", zorder=3)
        ax.text(lx + 3.6, ly, label, fontsize=6.6, color=INK_SECONDARY,
                ha="left", va="center")
        lx += 3.6 + len(label) * 1.55 + 5.0
    ax.plot([0, content_w], [LEGEND_H - 1.5, LEGEND_H - 1.5], color="#e2e2de", lw=0.6)

    save(fig, "fig1_classification", OUT)


if __name__ == "__main__":
    main()
