"""§3.5 天然橡胶单体：cis-1,4-聚异戊二烯重复单元。

SMILES 复用 fig12_appendix_monomers.py 里已核对的常量（顺式几何已由
verify_appendix_stereochemistry.py 核对）。链尺度的应变诱导结晶结构不在这里重复画——
§7.3 案例研究已经有一张紧凑的 NR/SBR 结构对比图（fig8_nr_sbr_comparison.py），正文
在这里直接向前指路，避免同一个结构画两次。
"""

import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

import verify_appendix_stereochemistry
from fig12_appendix_monomers import PANELS as FIG12_PANELS
from style import INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}
NAME, CHEM_NAME, SMILES, COLOUR, ANNOTATE = BY_NAME_12["Natural rubber"][1:]

PX_W, PX_H = 900, 460


def render(smiles):
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DCairo(PX_W, PX_H)
    opts = drawer.drawOptions()
    opts.dummiesAreAttachments = True
    opts.bondLineWidth = 3
    opts.fixedFontSize = 40
    opts.padding = 0.08
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    return mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png")


def main():
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, ax = plt.subplots(figsize=(80 * MM, 40 * MM))
    ax.imshow(render(SMILES))
    ax.axis("off")
    ax.text(0.0, 1.16, NAME, transform=ax.transAxes, fontsize=7.5, weight="bold",
            color=COLOUR, ha="left", va="top")
    ax.text(0.0, 1.00, CHEM_NAME, transform=ax.transAxes, fontsize=6.0,
            color=INK_SECONDARY, ha="left", va="top")

    fig.subplots_adjust(top=0.74, bottom=0.03, left=0.02, right=0.98)
    save(fig, "fig_rubber_monomer", OUT)


if __name__ == "__main__":
    main()
