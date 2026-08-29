"""最终报告的 Fig 5(a) —— 热性质与熔融加工窗口。绘图逻辑在 draw(ax) 里，被
`fig_property_maps.py` 复用（把 (a)(b) 两个面板拼成一张 Fig 5）。单独跑本文件也能出一张
独立的热窗口图。数据：data/thermal_properties.csv。

---- 原始说明 ----
Word Figure 11 · 热性质与熔融加工窗口。

一张图回答"这类材料为什么难加工"：每种材料把 Tg、Tm、分解起始温度画在同一温标上，
Tm 到 Td 之间的阴影就是熔融加工窗口。PHB 的窗口只有几十度，纤维素和壳聚糖根本没有窗口
（分解先于熔融），而作为对照的 LDPE 与 PET 有一两百度的余量。
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

from style import CLASS_COLOR, INK, INK_MUTED, INK_SECONDARY, MM, apply_style, save

HERE = Path(__file__).parent
OUT = HERE / "output"
DATA = HERE / "data" / "thermal_properties.csv"


def load():
    rows = []
    with DATA.open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            rows.append(line)
    return list(csv.DictReader(rows))


def num(value):
    return float(value) if value not in ("", None) else None


def draw(ax):
    """把热窗口图画进给定的 ax——被 fig_property_maps.py 复用，也被本脚本 main() 用。"""
    records = load()
    records.reverse()  # CSV 自上而下 → 图上自下而上，参照物落在最下面

    for i, row in enumerate(records):
        colour = CLASS_COLOR[row["class"]]
        tg, tm, td = num(row["Tg_C"]), num(row["Tm_C"]), num(row["Td_C"])

        # 底轨：从最低标注温度延伸到分解温度
        left = min([v for v in (tg, tm) if v is not None], default=td)
        ax.plot([left, td], [i, i], color="#e2e2de", lw=3.2,
                solid_capstyle="round", zorder=1)

        # 熔融加工窗口
        if row["melts"] == "yes" and tm is not None and td is not None:
            ax.add_patch(Rectangle((tm, i - 0.26), td - tm, 0.52,
                                   facecolor=colour, alpha=0.28,
                                   edgecolor="none", zorder=2))
            ax.text(td + 8, i, f"{td - tm:.0f} °C", fontsize=6.5, color=colour,
                    ha="left", va="center", zorder=4)
        else:
            ax.text(td + 8, i, "no window", fontsize=6.5, color=INK_MUTED,
                    ha="left", va="center", style="italic", zorder=4)

        if tg is not None:
            ax.plot([tg], [i], marker="o", markersize=5, markerfacecolor="white",
                    markeredgecolor=colour, markeredgewidth=1.2, zorder=3)
        if tm is not None:
            ax.plot([tm], [i], marker="D", markersize=4.6, color=colour, zorder=3)
        ax.plot([td], [i], marker="|", markersize=9, markeredgewidth=1.6,
                color=colour, zorder=3)

    ax.set_yticks(range(len(records)))
    ax.set_yticklabels([r["material"] for r in records], fontsize=7)
    ax.set_xlabel("Temperature (°C)")
    ax.set_xlim(-150, 490)                    # 收掉右侧多余空白（原 520），仍容得下 "290 °C" 标签
    ax.set_ylim(-0.8, len(records) + 0.95)    # 顶部留一点空白给图例
    ax.set_xticks(range(-150, 451, 50))
    ax.grid(axis="x", zorder=0)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)

    handles = [
        Line2D([], [], marker="o", markersize=5, markerfacecolor="white",
               markeredgecolor=INK_SECONDARY, markeredgewidth=1.2, linestyle="none",
               label="$T_\\mathrm{g}$"),
        Line2D([], [], marker="D", markersize=4.6, color=INK_SECONDARY,
               linestyle="none", label="$T_\\mathrm{m}$"),
        Line2D([], [], marker="|", markersize=9, markeredgewidth=1.6,
               color=INK_SECONDARY, linestyle="none",
               label="onset of decomposition"),
        Rectangle((0, 0), 1, 1, facecolor=INK_SECONDARY, alpha=0.28,
                  label="melt-processing window"),
    ]
    ax.legend(handles=handles, loc="upper left", frameon=False, ncol=2,
              fontsize=6.5, handletextpad=0.5, columnspacing=1.2, borderpad=0.15,
              labelspacing=0.25, bbox_to_anchor=(0.0, 1.0))


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(170 * MM, 78 * MM), layout="constrained")
    draw(ax)
    save(fig, "fig4_thermal_windows", OUT)


if __name__ == "__main__":
    main()
