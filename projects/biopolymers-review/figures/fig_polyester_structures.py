"""=== Word Figure 6 ===  §3.2 聚酯（PHA/PLA）结构：PHB 与 PLLA 的重复单元 + 螺旋堆积。

前两格 SMILES 复用 fig2_repeat_units.py 里已核对的常量；第三格复用
fig13_appendix_chain_structures.py 的 panel_pha_pla（同一份代码）。

排版：170 mm 通栏、三格等宽、H_M 高度、constrained layout。第三格的机理说明关掉
（DRAW_CAPTIONS=False），改在 report.md 图注里写；附录 Fig 19(c) 保留那句说明。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import verify_stereochemistry
import fig13_appendix_chain_structures as chains
from fig2_repeat_units import PANELS as FIG2_PANELS
from style import FIG_W, H_M, apply_style, draw_mol, panel_title, save

OUT = Path(__file__).parent / "output"
BY_NAME_2 = {p[1]: p for p in FIG2_PANELS}

chains.DRAW_CAPTIONS = False  # 正文复用时说明走 Word 图注


def monomer_panel(ax, tag, key):
    _, name, _chem, smiles, colour, annotate = BY_NAME_2[key]
    ax.imshow(draw_mol(smiles, annotate_cip=annotate))
    ax.axis("off")
    panel_title(ax, tag, name, colour)


def main():
    verify_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(FIG_W, H_M / 25.4), layout="constrained")

    monomer_panel(axes[0], "a", "PHB")
    monomer_panel(axes[1], "b", "PLLA")
    chains.panel_pha_pla(axes[2])

    save(fig, "fig_polyester_structures", OUT)


if __name__ == "__main__":
    main()
