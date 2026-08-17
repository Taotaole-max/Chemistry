"""一次生成全部图：python3 make_all.py

每张图同时导出 SVG（插进 Word 用，矢量、放大不糊）和 600 dpi PNG（校对用）。
Fig 2 出图前会先跑立体化学核对，构型不对就直接报错停下，不会悄悄产出错图。
"""

import importlib
import sys

MODULES = [
    "fig1_classification",
    "fig2_repeat_units",
    "fig3_cellulose_hierarchy",
    "fig4_thermal_windows",
    "fig5_property_map",
    "fig6_degradation",
]


def main():
    for name in MODULES:
        print(f"[{name}]")
        module = importlib.import_module(name)
        module.main()
    print("\n全部完成，输出在 output/")
    print("提醒：Fig 4 与 Fig 5 的数值仍是 PROVISIONAL，见 data/*.csv 顶部说明。")


if __name__ == "__main__":
    sys.exit(main())
