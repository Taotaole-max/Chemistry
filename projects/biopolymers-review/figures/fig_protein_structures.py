"""§3.3 蛋白质结构：丝素蛋白、胶原蛋白的主链重复基序 + 各自的二级结构。

前两格 SMILES 复用 fig12_appendix_monomers.py 里已核对的常量；后两格复用
fig13_appendix_chain_structures.py 的 panel_silk / panel_collagen（同一份代码）。
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
from fig13_appendix_chain_structures import panel_collagen, panel_silk
from style import INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}

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
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(120 * MM, 70 * MM),
                              gridspec_kw={"height_ratios": [1.0, 1.3]})

    monomer_panel(axes[0, 0], "a", *BY_NAME_12["Silk fibroin"][1:])
    monomer_panel(axes[0, 1], "b", *BY_NAME_12["Collagen"][1:])
    panel_silk(axes[1, 0], tag="c")
    panel_collagen(axes[1, 1], tag="d")

    fig.subplots_adjust(top=0.90, bottom=0.02, left=0.02, right=0.98,
                         wspace=0.30, hspace=0.45)
    save(fig, "fig_protein_structures", OUT)


if __name__ == "__main__":
    main()
