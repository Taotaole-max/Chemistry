"""=== Word Figure 7 ===  §3.3 蛋白质结构：丝素/胶原蛋白主链重复基序 + 各自二级结构。

前两格 SMILES 复用 fig12_appendix_monomers.py 里已核对的常量；后两格复用
fig13_appendix_chain_structures.py 的 panel_silk / panel_collagen（同一份代码）。

排版：170 mm 通栏、2×2、H_L 高度、constrained layout。二级结构那两格的机理说明关掉
（走 Word 图注）；附录 Fig 19(d)(e) 保留说明。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import verify_appendix_stereochemistry
import fig13_appendix_chain_structures as chains
from fig12_appendix_monomers import PANELS as FIG12_PANELS
from style import FIG_W, H_L, apply_style, draw_mol, panel_title, save

OUT = Path(__file__).parent / "output"
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}

chains.DRAW_CAPTIONS = False


def monomer_panel(ax, tag, key):
    _, name, _chem, smiles, colour, annotate = BY_NAME_12[key]
    ax.imshow(draw_mol(smiles, annotate_cip=annotate))
    ax.axis("off")
    panel_title(ax, tag, name, colour)


def main():
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(FIG_W, H_L / 25.4), layout="constrained")

    monomer_panel(axes[0, 0], "a", "Silk fibroin")
    monomer_panel(axes[0, 1], "b", "Collagen")
    chains.panel_silk(axes[1, 0], tag="c")
    chains.panel_collagen(axes[1, 1], tag="d")

    save(fig, "fig_protein_structures", OUT)


if __name__ == "__main__":
    main()
