"""最终报告的 Fig 5(b) —— 模量 vs 断裂伸长率（Ashby 式）。绘图逻辑在 draw(ax) 里，被
`fig_property_maps.py` 复用。数据：data/mechanical_properties.csv。

---- 原始说明 ----
Word Figure 12 · 性能图：拉伸模量 vs 断裂伸长率（Ashby 式）。

画区间椭圆而不是单点——生物聚合物的力学数据本身就分散，单点会假装它有确定值。
读法：左上角是又硬又脆，右下角是又软又韧。生物聚合物几乎全部落在左侧（伸长率低），
石油基通用塑料占据右侧，这就是"输在韧性不输在强度"这句判断的图形依据。

坐标在 log10 空间手工构造（而不是 set_xscale('log')），因为椭圆要在对数坐标里保持形状。
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse

from style import CLASS_COLOR, INK, INK_SECONDARY, MM, apply_style, save

HERE = Path(__file__).parent
OUT = HERE / "output"
DATA = HERE / "data" / "mechanical_properties.csv"

CLASS_LABEL = {
    "polysaccharide": "Polysaccharide",
    "polyester": "Polyester",
    "protein": "Polypeptide",
    "other": "Other biopolymer",
    "petro": "Fossil-based reference",
}

# label_pos -> (dx, dy, ha, va) in log10 units
OFFSET = {
    "above": (0.0, 0.16, "center", "bottom"),
    "below": (0.0, -0.16, "center", "top"),
    "left": (-0.10, 0.0, "right", "center"),
    "right": (0.10, 0.0, "left", "center"),
}


def load():
    with DATA.open(encoding="utf-8") as fh:
        rows = [line for line in fh if not line.startswith("#") and line.strip()]
    return list(csv.DictReader(rows))


def draw(ax):
    """把 Ashby 图画进给定的 ax——被 fig_property_maps.py 复用，也被本脚本 main() 用。"""
    records = load()

    seen = []
    for row in records:
        colour = CLASS_COLOR[row["class"]]
        if row["class"] not in seen:
            seen.append(row["class"])

        x0, x1 = np.log10(float(row["eps_min_pct"])), np.log10(float(row["eps_max_pct"]))
        y0, y1 = np.log10(float(row["E_min_GPa"])), np.log10(float(row["E_max_GPa"]))
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        # 给零宽度的区间一个可见的最小尺寸
        w, h = max(x1 - x0, 0.12), max(y1 - y0, 0.12)

        ax.add_patch(Ellipse((cx, cy), w, h, facecolor=colour, alpha=0.30,
                             edgecolor=colour, linewidth=1.0, zorder=3))

        dx, dy, ha, va = OFFSET[row["label_pos"]]
        ax.text(cx + dx + (w / 2 if ha == "left" else -w / 2 if ha == "right" else 0),
                cy + dy + (h / 2 if va == "bottom" else -h / 2 if va == "top" else 0),
                row["material"], fontsize=6.5, color=colour, ha=ha, va=va, zorder=4)

    ax.set_xlabel("Elongation at break (%)")
    ax.set_ylabel("Tensile modulus (GPa)")
    ax.set_xlim(np.log10(1.2), np.log10(1600))
    ax.set_ylim(np.log10(0.0006), np.log10(240))   # 顶部留白给面板标题

    xticks = [1, 3, 10, 30, 100, 300, 1000]
    ax.set_xticks(np.log10(xticks))
    ax.set_xticklabels([str(t) for t in xticks])
    yticks = [0.001, 0.01, 0.1, 1, 10, 100]
    ax.set_yticks(np.log10(yticks))
    ax.set_yticklabels(["0.001", "0.01", "0.1", "1", "10", "100"])
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    # 读图导引：右下角一句（左上角那句删掉，给面板标题让位）
    ax.text(np.log10(1200), np.log10(0.0009), "soft and extensible", fontsize=6.8,
            color=INK_SECONDARY, style="italic", ha="right", va="center")

    handles = [Line2D([], [], marker="o", markersize=6, linestyle="none",
                      markerfacecolor=CLASS_COLOR[k], markeredgecolor=CLASS_COLOR[k],
                      alpha=0.6, label=CLASS_LABEL[k]) for k in seen]
    ax.legend(handles=handles, loc="lower left", frameon=False, ncol=2,
              handletextpad=0.5, columnspacing=1.2, borderpad=0.2)


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(170 * MM, 82 * MM), layout="constrained")
    draw(ax)
    save(fig, "fig5_property_map", OUT)


if __name__ == "__main__":
    main()
