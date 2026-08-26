"""§3.2 聚酯（PHA/PLA）结构：PHB 与 PLLA 的重复单元 + 螺旋堆积。

前两格的 SMILES 直接复用 fig2_repeat_units.py 里已核对的常量；第三格复用
fig13_appendix_chain_structures.py 的 panel_pha_pla（同一份代码）。
"""

import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

import verify_stereochemistry
from fig2_repeat_units import PANELS as FIG2_PANELS
from fig13_appendix_chain_structures import panel_pha_pla
from style import INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"
BY_NAME_2 = {p[1]: p for p in FIG2_PANELS}

PX_W, PX_H = 760, 520


def render(smiles, annotate_cip):
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DCairo(PX_W, PX_H)
    opts = drawer.drawOptions()
    opts.dummiesAreAttachments = True
    opts.addStereoAnnotation = annotate_cip
    opts.bondLineWidth = 3
    opts.fixedFontSize = 38
    opts.padding = 0.07
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    return mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png")


def monomer_panel(ax, tag, name, chem_name, smiles, colour, annotate):
    ax.imshow(render(smiles, annotate))
    ax.axis("off")
    ax.text(0.0, 1.16, f"({tag}) {name}", transform=ax.transAxes,
            fontsize=7.3, weight="bold", color=colour, ha="left", va="top")
    ax.text(0.0, 1.03, chem_name, transform=ax.transAxes,
            fontsize=5.8, color=INK_SECONDARY, ha="left", va="top")


def main():
    verify_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(170 * MM, 58 * MM))

    monomer_panel(axes[0], "a", *BY_NAME_2["PHB"][1:])
    monomer_panel(axes[1], "b", *BY_NAME_2["PLLA"][1:])
    panel_pha_pla(axes[2])

    fig.subplots_adjust(top=0.80, bottom=0.02, left=0.02, right=0.98, wspace=0.20)
    save(fig, "fig_polyester_structures", OUT)


if __name__ == "__main__":
    main()
