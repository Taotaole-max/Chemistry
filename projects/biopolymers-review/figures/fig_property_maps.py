"""=== Word Figure 5 ===  热学与力学包络，一张两面板图（替代旧 Fig 11 + Fig 12）。

(a) 各材料的 Tg / Tm / 分解起始温度画在同一温标上，Tm→Td 阴影即熔融加工窗口；
(b) Ashby 式模量 vs 断裂伸长率图，区间椭圆。

两个面板各自的绘图逻辑复用 fig4_thermal_windows.draw() / fig5_property_map.draw()。
一个 Word 图注。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import fig4_thermal_windows as thermal
import fig5_property_map as mech
from style import FIG_W, FS_PANEL_TITLE, INK, apply_style, save

OUT = Path(__file__).parent / "output"


def main():
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W, 78 / 25.4), layout="constrained")

    thermal.draw(axes[0])
    axes[0].set_title("(a) Thermal transitions and melt-processing windows",
                      fontsize=FS_PANEL_TITLE, fontweight="bold", color=INK,
                      loc="left", pad=4)

    mech.draw(axes[1])
    axes[1].set_title("(b) Modulus vs. elongation at break",
                      fontsize=FS_PANEL_TITLE, fontweight="bold", color=INK,
                      loc="left", pad=4)

    save(fig, "fig_property_maps", OUT)


if __name__ == "__main__":
    main()
