"""§3.1 多糖重复单元一览：纤维素、直链淀粉、壳聚糖、海藻酸盐 M/G。

放在 3.1 小节正文里（不是附录），让"结构决定性质"这条论证在读到对应材料时就有图可看。
SMILES 直接复用 fig2_repeat_units.py / fig12_appendix_monomers.py 里已经过
verify_stereochemistry.py / verify_appendix_stereochemistry.py 核对的常量，不重新
手写，保证和那两张图里的构型完全一致（同一个 SMILES 字符串）。
"""

import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

import verify_stereochemistry
import verify_appendix_stereochemistry
from fig2_repeat_units import PANELS as FIG2_PANELS
from fig12_appendix_monomers import PANELS as FIG12_PANELS
from style import INK_SECONDARY, MM, apply_style, save

OUT = Path(__file__).parent / "output"

BY_NAME_2 = {p[1]: p for p in FIG2_PANELS}
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}

# 复用 Fig 2 / Fig 12 已核对的 SMILES；只改标号和排版，不改任何构型字符串。
# 壳聚糖的化学名在这里缩短一点（原名太长，会和右邻面板的标题挤在一起）。
_CHITOSAN = BY_NAME_2["Chitosan"]
PANELS = [
    ("a", *BY_NAME_2["Cellulose"][1:]),
    ("b", *BY_NAME_2["Amylose (starch)"][1:]),
    ("c", _CHITOSAN[1], "2-amino-2-deoxy-D-glucan", *_CHITOSAN[3:]),
    ("d", *BY_NAME_12["Alginate M"][1:]),
    ("e", *BY_NAME_12["Alginate G*"][1:]),
]

NOTE = (
    "(a)/(b) differ only at C1 — that single centre separates\n"
    "cellulose's extended, 60-70% crystalline ribbon from amylose's\n"
    "water-plasticised helix (§3.1). (d)/(e) differ only at C5 — the\n"
    "M/G ratio sets alginate's stiffness-brittleness trade-off (§8)."
)

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
    verify_stereochemistry.main()
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(1, 6, figsize=(170 * MM, 40 * MM))

    for ax, (tag, name, chem_name, smiles, colour, annotate) in zip(axes, PANELS):
        ax.imshow(render(smiles, annotate))
        ax.axis("off")
        ax.text(0.0, 1.22, f"({tag}) {name}", transform=ax.transAxes,
                fontsize=7.3, weight="bold", color=colour, ha="left", va="top")
        ax.text(0.0, 1.08, chem_name, transform=ax.transAxes,
                fontsize=5.8, color=INK_SECONDARY, ha="left", va="top")

    note_ax = axes[5]
    note_ax.axis("off")
    note_ax.text(0.0, 0.92, NOTE, transform=note_ax.transAxes, fontsize=6.2,
                 color=INK_SECONDARY, ha="left", va="top", linespacing=1.5)

    fig.subplots_adjust(top=0.78, bottom=0.02, left=0.01, right=0.99, wspace=0.32)
    save(fig, "fig_polysaccharide_monomers", OUT)


if __name__ == "__main__":
    main()
