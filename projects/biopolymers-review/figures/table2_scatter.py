"""Table 2 数据的散点图版本：一张图覆盖表里四列——模量、断裂伸长率、分解温度 Td、
是否有熔融加工窗口——而不是把表格原样渲染成图片。

编码方式：
  x 位置 = 断裂伸长率 (%)，log 轴
  y 位置 = 拉伸模量 (GPa)，log 轴
  误差棒  = 文献报的区间（模量和伸长率都是区间，不是单点）
  点的大小 = 分解起始温度 Td（越大越耐热；天然橡胶没有可比的 Td，用小号灰点+注记）
  点的颜色 = 主链化学类别（沿用 CLASS_COLOR，和其余图一致）
  边框样式 = 有无熔融加工窗口（实线边=可熔融加工，虚线边=分解先于熔融）

Tg/Tm 的具体数值仍以 Table 2/图 4 为准，这张图只把 Td 作为"热稳定性"的一个连续量纳入。

跑法：python3 table2_scatter.py（同时生成中文版 table2_scatter_zh.png/svg 和
英文版 table2_scatter_en.png/svg）
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from style import CLASS_COLOR, INK, INK_SECONDARY, MM, apply_style, save

HERE = Path(__file__).parent
OUT = HERE / "output"

CJK_FONT_STACK = ["Microsoft YaHei", "SimHei", "SimSun", "Arial", "DejaVu Sans"]

CLASS_LABEL_ZH = {
    "polysaccharide": "多糖", "polyester": "聚酯", "protein": "蛋白质",
    "other": "其他生物聚合物", "petro": "石油基对照",
}
CLASS_LABEL_EN = {
    "polysaccharide": "Polysaccharide", "polyester": "Polyester", "protein": "Polypeptide",
    "other": "Other biopolymer", "petro": "Fossil-based reference",
}

# (name_zh, name_en, class, E_min, E_max, eps_min, eps_max, Td_C or None, melts, label_pos)
ROWS = [
    ("纤维素", "Cellulose", "polysaccharide", 10, 30, 8, 15, 300, False, "above"),
    ("淀粉（TPS）", "TPS", "polysaccharide", 0.02, 1.0, 20, 100, 300, False, "below"),
    ("壳聚糖", "Chitosan", "polysaccharide", 1.0, 4.0, 3, 30, 280, False, "right"),
    ("丝素蛋白", "Silk fibroin", "protein", 5, 17, 15, 30, 300, False, "right"),
    ("PHB", "PHB", "polyester", 1.5, 4.0, 2, 8, 200, True, "left"),
    ("PHBV", "PHBV", "polyester", 0.8, 2.5, 5, 25, 200, True, "below"),
    ("PLLA", "PLLA", "polyester", 2.5, 4.0, 3, 10, 300, True, "above"),
    ("PBS", "PBS", "polyester", 0.3, 0.7, 200, 500, 350, True, "above"),
    ("天然橡胶", "Natural rubber", "other", 0.001, 0.005, 500, 800, None, False, "above"),
    ("LDPE（对照）", "LDPE", "petro", 0.15, 0.35, 200, 600, 400, True, "below"),
    ("PET（对照）", "PET", "petro", 2.0, 4.0, 50, 300, 400, True, "above"),
]

OFFSET = {
    "above": (0.0, 0.16, "center", "bottom"),
    "below": (0.0, -0.16, "center", "top"),
    "left": (-0.10, 0.0, "right", "center"),
    "right": (0.10, 0.0, "left", "center"),
}

SIZE_MIN, SIZE_MAX = 30, 340
TD_MIN, TD_MAX = 200, 400


def td_size(td):
    if td is None:
        return 55
    t = max(TD_MIN, min(TD_MAX, td))
    return SIZE_MIN + (SIZE_MAX - SIZE_MIN) * (t - TD_MIN) / (TD_MAX - TD_MIN)


def render(name_idx, class_label, headers, stem, note, cjk=False):
    apply_style()
    if cjk:
        mpl.rcParams["font.sans-serif"] = CJK_FONT_STACK
        mpl.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(170 * MM, 108 * MM))

    seen = []
    for row in ROWS:
        name, cls = row[name_idx], row[2]
        E_min, E_max, eps_min, eps_max, td, melts, pos = row[3:10]
        if cls not in seen:
            seen.append(cls)
        colour = CLASS_COLOR[cls]

        x0, x1 = np.log10(eps_min), np.log10(eps_max)
        y0, y1 = np.log10(E_min), np.log10(E_max)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        cx_lin, cy_lin = 10 ** cx, 10 ** cy

        xerr = [[cx_lin - 10 ** x0], [10 ** x1 - cx_lin]]
        yerr = [[cy_lin - 10 ** y0], [10 ** y1 - cy_lin]]
        ax.errorbar(cx_lin, cy_lin, xerr=xerr, yerr=yerr, fmt="none",
                    ecolor=colour, elinewidth=0.8, capsize=2, capthick=0.8,
                    alpha=0.55, zorder=2)

        edge_style = dict(edgecolor=INK, linewidth=1.1) if melts else \
                     dict(edgecolor=INK_SECONDARY, linewidth=1.0, linestyle=(0, (2, 1.5)))
        ax.scatter([cx_lin], [cy_lin], s=[td_size(td)], facecolor=colour, alpha=0.85,
                   zorder=3, **edge_style)

        dx, dy, ha, va = OFFSET[pos]
        ax.annotate(name, (cx, cy), xytext=(cx + dx, cy + dy),
                    fontsize=6.6, color=colour, ha=ha, va=va, zorder=4)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(headers[0])
    ax.set_ylabel(headers[1])
    ax.set_xlim(1.2, 1600)
    ax.set_ylim(0.0006, 90)
    xticks = [1, 3, 10, 30, 100, 300, 1000]
    ax.set_xticks(xticks)
    ax.set_xticklabels([str(t) for t in xticks])
    yticks = [0.001, 0.01, 0.1, 1, 10, 100]
    ax.set_yticks(yticks)
    ax.set_yticklabels(["0.001", "0.01", "0.1", "1", "10", "100"])
    ax.grid(True, which="major", zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    class_handles = [Line2D([], [], marker="o", markersize=7, linestyle="none",
                            markerfacecolor=CLASS_COLOR[k], markeredgecolor=CLASS_COLOR[k],
                            alpha=0.75, label=class_label[k]) for k in seen]
    style_handles = [
        Line2D([], [], marker="o", markersize=8, linestyle="none", markerfacecolor="#c9c9c4",
               markeredgecolor=INK, markeredgewidth=1.1, label=headers[2]),
        Line2D([], [], marker="o", markersize=8, linestyle="none", markerfacecolor="#c9c9c4",
               markeredgecolor=INK_SECONDARY, markeredgewidth=1.0, label=headers[3]),
    ]
    size_handles = [
        Line2D([], [], marker="o", markersize=np.sqrt(td_size(200)) * 0.9, linestyle="none",
               markerfacecolor="none", markeredgecolor=INK_SECONDARY, label=headers[4]),
        Line2D([], [], marker="o", markersize=np.sqrt(td_size(400)) * 0.9, linestyle="none",
               markerfacecolor="none", markeredgecolor=INK_SECONDARY, label=headers[5]),
    ]

    leg1 = ax.legend(handles=class_handles, loc="lower left", frameon=False, fontsize=6.6,
                     handletextpad=0.5, borderpad=0.2, bbox_to_anchor=(0.0, 0.0))
    ax.add_artist(leg1)
    leg2 = ax.legend(handles=style_handles, loc="lower left", frameon=False, fontsize=6.6,
                     handletextpad=0.5, borderpad=0.2, bbox_to_anchor=(0.30, 0.0))
    ax.add_artist(leg2)
    ax.legend(handles=size_handles, loc="lower left", frameon=False, fontsize=6.6,
             handletextpad=0.9, labelspacing=1.1, borderpad=0.2, bbox_to_anchor=(0.62, 0.0))

    ax.text(0.0, -0.17, note, transform=ax.transAxes, fontsize=6.2, color=INK_SECONDARY,
            ha="left", va="top", linespacing=1.5)

    save(fig, stem, OUT)


def main():
    render(0, CLASS_LABEL_ZH,
           ["断裂伸长率 (%)", "拉伸模量 (GPa)", "有熔融窗口", "无熔融窗口",
            f"Td ≈ {TD_MIN} °C", f"Td ≈ {TD_MAX} °C"],
           "table2_scatter_zh",
           "点大小 = 分解起始温度 Td（天然橡胶无可比 Td，用小号点示意）；误差棒 = 文献报告区间；"
           "边框实/虚线区分有无熔融加工窗口。\n完整 Tg/Tm/Td 数值和结晶度/加工方式描述见正文表 2。",
           cjk=True)
    render(1, CLASS_LABEL_EN,
           ["Elongation at break (%)", "Tensile modulus (GPa)", "melts", "no melt",
            f"Td ≈ {TD_MIN} °C", f"Td ≈ {TD_MAX} °C"],
           "table2_scatter_en",
           "Marker size = decomposition onset Td (natural rubber has no comparable Td, shown small); "
           "error bars = literature range; solid/dashed\nedge marks presence of a melt-processing window. "
           "Full Tg/Tm/Td values and crystallinity/processing notes remain in Table 2.")


if __name__ == "__main__":
    main()
