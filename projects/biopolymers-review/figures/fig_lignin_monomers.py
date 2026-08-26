"""§3.4 木质素的三种单木质醇前体（p-香豆醇/松柏醇/芥子醇，0/1/2 个 OMe）。

SMILES 直接复用 fig12_appendix_monomers.py 里已核对的常量。木质素没有周期性的链
结构可画——自由基偶联产物是无规交联网络，不是规则重复链（正文 §3.4 已经说明这一点），
所以这里只画单体，不配一张"链结构"图，避免为了凑图而画一个没有真实拓扑依据的示意。
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

PANELS = [
    ("a", *BY_NAME_12["p-Coumaryl OH"][1:]),
    ("b", *BY_NAME_12["Coniferyl OH"][1:]),
    ("c", *BY_NAME_12["Sinapyl OH"][1:]),
]

PX_W, PX_H = 760, 520


def render(smiles):
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DCairo(PX_W, PX_H)
    opts = drawer.drawOptions()
    opts.bondLineWidth = 3
    opts.fixedFontSize = 38
    opts.padding = 0.08
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    return mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png")


def main():
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(140 * MM, 46 * MM))

    for ax, (tag, name, chem_name, smiles, colour, _annotate) in zip(axes, PANELS):
        ax.imshow(render(smiles))
        ax.axis("off")
        ax.text(0.0, 1.18, f"({tag}) {name}", transform=ax.transAxes,
                fontsize=7.3, weight="bold", color=colour, ha="left", va="top")
        ax.text(0.0, 1.04, chem_name, transform=ax.transAxes,
                fontsize=5.8, color=INK_SECONDARY, ha="left", va="top")

    fig.subplots_adjust(top=0.76, bottom=0.02, left=0.02, right=0.98, wspace=0.15)
    save(fig, "fig_lignin_monomers", OUT)


if __name__ == "__main__":
    main()
