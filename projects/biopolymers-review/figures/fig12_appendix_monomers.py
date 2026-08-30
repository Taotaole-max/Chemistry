import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

import verify_appendix_stereochemistry
from style import (C_OTHER, C_POLYSACCHARIDE, C_PROTEIN, INK_SECONDARY,
                    MM, apply_style, save)

OUT = Path(__file__).parent / "output"

PANELS = [
    ("a", "Alginate M", "beta-D-mannuronic acid",
     "OC(=O)[C@H]1O[C@@H](*)[C@@H](O)[C@@H](O)[C@@H]1O*", C_POLYSACCHARIDE, False),
    ("b", "Alginate G*", "alpha-L-guluronic acid",
     "OC(=O)[C@@H]1O[C@@H](*)[C@@H](O)[C@@H](O)[C@@H]1O*", C_POLYSACCHARIDE, False),
    ("c", "Natural rubber", "cis-1,4-polyisoprene",
     r"*C/C(C)=C\C*", C_OTHER, False),
    ("d", "SBR: butadiene", "1,4-unit",
     "*CC=CC*", C_OTHER, False),
    ("e", "SBR: styrene", "vinylbenzene unit",
     "*CC(*)c1ccccc1", C_OTHER, False),
    ("f", "p-Coumaryl OH", "lignin precursor, 0 OMe",
     "OC/C=C/c1ccc(O)cc1", C_OTHER, False),
    ("g", "Coniferyl OH", "lignin precursor, 1 OMe",
     "OC/C=C/c1ccc(O)c(OC)c1", C_OTHER, False),
    ("h", "Sinapyl OH", "lignin precursor, 2 OMe",
     "OC/C=C/c1cc(OC)c(O)c(OC)c1", C_OTHER, False),
    ("i", "Silk fibroin", "(Gly-Ala)n repeat",
     "*NCC(=O)N[C@@H](C)C(=O)*", C_PROTEIN, True),
    ("j", "Collagen", "Gly-Pro-Hyp repeat",
     "*NCC(=O)N1[C@H](C(=O)N2[C@H](C(=O)*)C[C@@H](O)C2)CCC1", C_PROTEIN, True),
]

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

def main():
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(2, 5, figsize=(200 * MM, 84 * MM))

    for ax, (tag, name, chem_name, smiles, colour, annotate) in zip(
            axes.flat, PANELS):
        ax.imshow(render(smiles, annotate))
        ax.axis("off")
        ax.text(0.0, 1.26, f"({tag}) {name}", transform=ax.transAxes,
                fontsize=7.5, weight="bold", color=colour, ha="left", va="top",
                clip_on=False)
        ax.text(0.0, 1.12, chem_name, transform=ax.transAxes,
                fontsize=6, color=INK_SECONDARY, ha="left", va="top",
                clip_on=False)

    fig.subplots_adjust(hspace=0.55, wspace=0.12, top=0.86, bottom=0.02,
                        left=0.01, right=0.99)
    save(fig, "fig12_appendix_monomers", OUT)

if __name__ == "__main__":
    main()
