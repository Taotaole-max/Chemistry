"""=== Word Figure 8 ===  §3.4 木质素的三种单木质醇前体（p-香豆醇/松柏醇/芥子醇，
0/1/2 个 OMe）。

SMILES 复用 fig12_appendix_monomers.py 里已核对的常量。木质素没有周期性的链结构可画
——自由基偶联产物是无规交联网络，不是规则重复链（正文 §3.4 已说明），所以只画单体。

排版：170 mm 通栏、三格等宽、H_S、constrained layout。化学名（0/1/2 个 OMe）挪进图注。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import verify_appendix_stereochemistry
from fig12_appendix_monomers import PANELS as FIG12_PANELS
from style import FIG_W, H_S, apply_style, draw_mol, panel_title, save

OUT = Path(__file__).parent / "output"
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}

KEYS = [("a", "p-Coumaryl OH"), ("b", "Coniferyl OH"), ("c", "Sinapyl OH")]


def main():
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(FIG_W, H_S / 25.4), layout="constrained")

    for ax, (tag, key) in zip(axes, KEYS):
        _, name, _chem, smiles, colour, _annotate = BY_NAME_12[key]
        ax.imshow(draw_mol(smiles, annotate_cip=False))
        ax.axis("off")
        panel_title(ax, tag, name.replace(" OH", ""), colour)

    save(fig, "fig_lignin_monomers", OUT)


if __name__ == "__main__":
    main()
