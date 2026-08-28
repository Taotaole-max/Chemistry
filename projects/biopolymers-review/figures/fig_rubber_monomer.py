"""=== Word Figure 9 ===  §3.5 天然橡胶单体：cis-1,4-聚异戊二烯重复单元。

SMILES 复用 fig12_appendix_monomers.py 里已核对的常量（顺式几何已由
verify_appendix_stereochemistry.py 核对）。链尺度的应变诱导结晶结构不在这里画——
§7.3 案例研究有一张 NR/SBR 结构对比图，正文在这里直接向前指路。

排版：170 mm 通栏、单格、H_S、constrained layout。单个小分子占一张通栏图偏空，
所以画得大一点（放大 draw_mol 的画布），并居中。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import verify_appendix_stereochemistry
from fig12_appendix_monomers import PANELS as FIG12_PANELS
from style import FIG_W, FS_PANEL_TITLE, H_S, apply_style, draw_mol, save

OUT = Path(__file__).parent / "output"
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}
_, NAME, _CHEM, SMILES, COLOUR, _ANNOTATE = BY_NAME_12["Natural rubber"]


def main():
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, ax = plt.subplots(figsize=(FIG_W, H_S / 25.4), layout="constrained")
    ax.imshow(draw_mol(SMILES, annotate_cip=False, px_w=1100, px_h=460))
    ax.axis("off")
    ax.set_anchor("N")
    ax.set_title("Natural rubber  ·  cis-1,4-polyisoprene", fontsize=FS_PANEL_TITLE,
                 fontweight="bold", color=COLOUR, loc="left", pad=3.0)
    save(fig, "fig_rubber_monomer", OUT)


if __name__ == "__main__":
    main()
