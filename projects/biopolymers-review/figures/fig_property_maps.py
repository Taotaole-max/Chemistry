"""=== Word Figure 5 ===  热学与力学包络，一张两面板图（替代旧 Fig 11 + Fig 12）。

(a) 各材料的 Tg / Tm / 分解起始温度画在同一温标上，Tm→Td 阴影即熔融加工窗口；
(b) Ashby 式模量 vs 断裂伸长率图，区间椭圆。

两个面板各自的绘图逻辑复用 fig4_thermal_windows.draw() / fig5_property_map.draw()。
一个 Word 图注。

布局：**不用 constrained layout**。改用 subplots_adjust 手工给死边距——这样两个子图的
坐标框宽高严格相等（constrained layout 会因为 (a) 的长 y 标签把两框拉成不一样大）。
边距是一次调好的：left 给 (a) 的材料名留位，wspace 给 (b) 的 y 轴标题留位。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import fig4_thermal_windows as thermal
import fig5_property_map as mech
from style import FIG_W, FS_PANEL_TITLE, INK, apply_style, save

OUT = Path(__file__).parent / "output"


def main():
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W, 82 / 25.4))
    # 手工边距：两个子图因此严格等宽等高。
    #   left  0.155 → 给 (a) 的 y 轴材料名留 ~1.04 in
    #   wspace 0.36 → 子图间距，容下 (b) 旋转的 "Tensile modulus (GPa)" + 刻度
    #   top/bottom 给面板标题和 x 轴标题留位
    fig.subplots_adjust(left=0.155, right=0.988, top=0.885, bottom=0.145, wspace=0.36)

    thermal.draw(axes[0])
    axes[0].set_title("(a) Thermal transitions and melt windows",
                      fontsize=FS_PANEL_TITLE, fontweight="bold", color=INK,
                      loc="left", pad=4)

    mech.draw(axes[1])
    axes[1].set_title("(b) Modulus vs. elongation at break",
                      fontsize=FS_PANEL_TITLE, fontweight="bold", color=INK,
                      loc="left", pad=4)

    save(fig, "fig_property_maps", OUT)


if __name__ == "__main__":
    main()
