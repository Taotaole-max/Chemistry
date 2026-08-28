"""一次生成全部图：python3 make_all.py

每张图同时导出 SVG（插进 Word 用，矢量、放大不糊）和 600 dpi PNG（校对用）。
Fig 2 / Fig 12 出图前会先跑立体化学核对，构型不对就直接报错停下，不会悄悄产出错图。
"""

import importlib
import sys

# 顺序 == Word 正文图号 1–8。2026-08-28 第二轮大改：把 15 张独立图合并成 8 张多面板图
# （真实论文的做法：一个 Figure 8-12 个子面板、一个图注），省下 ~2 页而不删任何论证。
#  - 旧 Fig 3/6/7/8/9（各家族单体）→ fig_repeat_units_all（Fig 3，13 面板）
#  - 旧 Fig 4/5/6c/7cd（各家族高阶结构）→ fig_higher_order_all（Fig 4，6 面板）
#  - 旧 Fig 11/12（热窗口 + Ashby）→ fig_property_maps（Fig 5，2 面板）
#  - 旧 Fig 14（加工流程图）删掉，§6 文字保留判定逻辑（加工不是题目必答子题）
MODULES = [
    "fig1_classification",       # Fig 1  分类树
    "fig7_causality_chain",      # Fig 2  结构–性质因果链
    "fig_repeat_units_all",      # Fig 3  各家族重复单元（13 面板合集）
    "fig_higher_order_all",      # Fig 4  各家族高阶结构（6 面板合集）
    "fig_property_maps",         # Fig 5  热窗口 + Ashby（2 面板）
    "fig9_dispersity",           # Fig 6  分散度 Đ
    "fig6_degradation",          # Fig 7  降解两路径（输出 fig_degradation）
    "fig8_nr_sbr_comparison",    # Fig 8  NR vs SBR
]
# 保留但不参与构建（作为 SMILES / panel 函数 / draw() 的共享来源被 import）：
#   fig2_repeat_units.py, fig12_appendix_monomers.py, fig13_appendix_chain_structures.py,
#   fig3_cellulose_hierarchy.py, fig_polysaccharide_*.py, fig_polyester_structures.py,
#   fig_protein_structures.py, fig_lignin_monomers.py, fig_rubber_monomer.py,
#   fig4_thermal_windows.py, fig5_property_map.py, fig10_processing_routes.py
# 已废弃：combine_1x4.py, fig6c_hydrolysis_barriers


def main():
    for name in MODULES:
        print(f"[{name}]")
        module = importlib.import_module(name)
        module.main()
    print("\n全部完成，输出在 output/")
    print("提醒：Fig 4 与 Fig 5 的数值仍是 PROVISIONAL，见 data/*.csv 顶部说明。")


if __name__ == "__main__":
    sys.exit(main())
