"""一次生成全部图：python3 make_all.py

每张图同时导出 SVG（插进 Word 用，矢量、放大不糊）和 600 dpi PNG（校对用）。
Fig 2 / Fig 12 出图前会先跑立体化学核对，构型不对就直接报错停下，不会悄悄产出错图。
"""

import importlib
import sys

MODULES = [
    "fig1_classification",
    "fig7_causality_chain",
    "fig_polysaccharide_monomers",
    "fig3_cellulose_hierarchy",
    "fig_polysaccharide_chains",
    "fig_polyester_structures",
    "fig_protein_structures",
    "fig_lignin_monomers",
    "fig_rubber_monomer",
    "fig9_dispersity",
    "fig4_thermal_windows",
    "fig5_property_map",
    "fig6_degradation",
    "fig10_processing_routes",
    "fig8_nr_sbr_comparison",
    "fig12_appendix_monomers",
    "fig13_appendix_chain_structures",
]
# fig2_repeat_units.py and combine_1x4.py are intentionally NOT in this list:
# fig2's five panels were redistributed into fig_polysaccharide_monomers /
# fig_polyester_structures (see build_docx.py's FIGURE_FILES comment for the full
# script -> current figure-number mapping); combine_1x4.py's output is no longer
# used in either report (Fig. 11 removed per user request, 2026-08-26). Both source
# files are kept in this directory but decoupled from the build.


def main():
    for name in MODULES:
        print(f"[{name}]")
        module = importlib.import_module(name)
        module.main()
    print("\n全部完成，输出在 output/")
    print("提醒：Fig 4 与 Fig 5 的数值仍是 PROVISIONAL，见 data/*.csv 顶部说明。")


if __name__ == "__main__":
    sys.exit(main())
