"""[数据模块] 其余材料（海藻酸 M/G、天然橡胶、SBR 单体、三种木质醇、丝素、胶原）的
重复单元 SMILES + 名称，定义在 PANELS 里。Fig 3（`fig_repeat_units_all.py`）和
Fig 8（`fig8_nr_sbr_comparison.py`）import 这个 PANELS。本文件的 main() 是早期版本、
不再参与构建。

---- 原始说明 ----
Fig 12 (附录) · 正文 §3/§7.3 提到、但 Fig 2 没画出重复单元的十种材料。

Fig 2 已经覆盖纤维素/直链淀粉/壳聚糖/PHB/PLLA；这张图补齐其余材料的单体/重复单元：
海藻酸盐的 M/G 两种糖醛酸、天然橡胶、SBR 的两种共聚单体、木质素的三种木质醇前体、
丝素蛋白与胶原蛋白的主链重复基序。方法和 Fig 2 完全一致——RDKit 从 SMILES 绘制，
链接点画成波浪键，立体化学由 verify_appendix_stereochemistry.py 机器核对后才允许出图。

**诚实标注**：海藻酸盐 G（古洛糖醛酸）的绝对构型只核对了"与 M 互为 C5 差向异构体"
这一关系（文献公认事实），没有独立文献 CIP 字符串可比对其绝对构型——提交前建议用
ChemDraw 或文献结构图再核一遍，见 verify_appendix_stereochemistry.py 开头说明。
其余九个结构（天然橡胶顺式几何、SBR 两种共聚单体、三种木质醇、丝素/胶原蛋白主链
手性碳）均已核对至与文献一致。
"""

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

# (标号, 名称, 化学名/说明, SMILES, 颜色, 是否标 CIP)
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
    verify_appendix_stereochemistry.main()   # 立体化学/几何不过就不出图

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
