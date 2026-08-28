"""一次生成全部图：python3 make_all.py

每张图同时导出 SVG（插进 Word 用，矢量、放大不糊）和 600 dpi PNG（校对用）。
Fig 2 / Fig 12 出图前会先跑立体化学核对，构型不对就直接报错停下，不会悄悄产出错图。
"""

import importlib
import sys

# 顺序 == Word 正文图号 1–15。2026-08-28 大改：
#  - 删掉附录 A（原 Fig 18/19 两张合集图）——§3.1–3.5 每节已有自己的单体/链结构图，
#    附录纯属重复。附录独有的 SBR 两个共聚单体并进了 fig8_nr_sbr_comparison（Fig 15）。
#  - 原 Fig 13/14/15（降解三张零碎图）：13+14 合并成 fig6_degradation 的一张两面板图，
#    15（能垒示意曲线，仅示意无数值）删掉，正文 §5.4 一句话带过。
MODULES = [
    "fig1_classification",            # Fig 1
    "fig7_causality_chain",           # Fig 2
    "fig_polysaccharide_monomers",    # Fig 3
    "fig3_cellulose_hierarchy",       # Fig 4
    "fig_polysaccharide_chains",      # Fig 5
    "fig_polyester_structures",       # Fig 6
    "fig_protein_structures",         # Fig 7
    "fig_lignin_monomers",            # Fig 8
    "fig_rubber_monomer",             # Fig 9
    "fig9_dispersity",                # Fig 10
    "fig4_thermal_windows",           # Fig 11
    "fig5_property_map",              # Fig 12
    "fig6_degradation",               # Fig 13  (single 2-panel output: fig_degradation)
    "fig10_processing_routes",        # Fig 14
    "fig8_nr_sbr_comparison",         # Fig 15
]
# 保留但不参与构建（仅作为 SMILES / panel 函数的共享来源被 import）：
#   fig2_repeat_units.py, fig12_appendix_monomers.py, fig13_appendix_chain_structures.py
# 已废弃：combine_1x4.py, fig6c_hydrolysis_barriers（原 Fig 15 能垒图）


def main():
    for name in MODULES:
        print(f"[{name}]")
        module = importlib.import_module(name)
        module.main()
    print("\n全部完成，输出在 output/")
    print("提醒：Fig 4 与 Fig 5 的数值仍是 PROVISIONAL，见 data/*.csv 顶部说明。")


if __name__ == "__main__":
    sys.exit(main())
