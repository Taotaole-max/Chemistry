"""[数据模块] 五种生物聚合物的重复单元 SMILES + 名称，定义在 PANELS 里。
最终报告的 Fig 3（`fig_repeat_units_all.py`）import 这个 PANELS。本文件自己的 main()
是早期版本、不再参与构建，留着只是为了 PANELS 常量和它的立体化学核对逻辑。

---- 原始说明 ----
Fig 2 · 五种代表性生物聚合物的重复单元。

结构由 RDKit 从 SMILES 绘制，链接点画成波浪键（聚合物重复单元的通用画法）。
立体化学由 verify_stereochemistry.py 机器核对后才允许出图——本脚本开头会调用它。

关于立体标注：PHB / PLLA 的手性碳不与哑原子相邻，CIP 规则适用，图上标出 (R)/(S)；
糖类的端基碳与哑原子相邻，CIP 优先级失去意义，标出来反而是错的，所以糖类不加标注，
构型信息由楔形键承载。
"""

import io
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

import verify_stereochemistry
from style import (C_POLYESTER, C_POLYSACCHARIDE, INK, INK_SECONDARY, MM,
                   apply_style, save)

OUT = Path(__file__).parent / "output"

# (标号, 名称, 化学名, SMILES, 颜色, 是否标 CIP)
PANELS = [
    ("a", "Cellulose", r"$\beta$(1$\rightarrow$4)-D-glucan",
     "OC[C@H]1O[C@@H](*)[C@H](O)[C@@H](O)[C@@H]1O*", C_POLYSACCHARIDE, False),
    ("b", "Amylose (starch)", r"$\alpha$(1$\rightarrow$4)-D-glucan",
     "OC[C@H]1O[C@H](*)[C@H](O)[C@@H](O)[C@@H]1O*", C_POLYSACCHARIDE, False),
    ("c", "Chitosan", r"$\beta$(1$\rightarrow$4)-2-amino-2-deoxy-D-glucan",
     "OC[C@H]1O[C@@H](*)[C@H](N)[C@@H](O)[C@@H]1O*", C_POLYSACCHARIDE, False),
    ("d", "PHB", "poly[(R)-3-hydroxybutyrate]",
     "*O[C@H](C)CC(=O)*", C_POLYESTER, True),
    ("e", "PLLA", "poly[(S)-lactic acid]",
     "*O[C@@H](C)C(=O)*", C_POLYESTER, True),
]

NOTE = (
    "Panels (a) and (b) differ only in the\n"
    "configuration at C1. That single centre\n"
    "separates cellulose — extended ribbon-like\n"
    "chains, 60–70 % crystalline, no melting\n"
    "transition — from amylose, which coils into\n"
    "helices and is plasticised by water."
)

PX_W, PX_H = 960, 560


def render(smiles, annotate_cip):
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DCairo(PX_W, PX_H)
    opts = drawer.drawOptions()
    opts.dummiesAreAttachments = True      # 链接点画成波浪键
    opts.addStereoAnnotation = annotate_cip
    opts.bondLineWidth = 3
    opts.fixedFontSize = 42
    opts.padding = 0.06
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    return mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png")


def main():
    verify_stereochemistry.main()   # 立体化学不过就不出图

    apply_style()
    fig, axes = plt.subplots(2, 3, figsize=(170 * MM, 96 * MM))

    for ax, (tag, name, chem_name, smiles, colour, annotate) in zip(
            axes.flat, PANELS):
        ax.imshow(render(smiles, annotate))
        ax.axis("off")
        ax.text(0.0, 1.30, f"({tag}) {name}", transform=ax.transAxes,
                fontsize=8, weight="bold", color=colour, ha="left", va="top")
        ax.text(0.0, 1.15, chem_name, transform=ax.transAxes,
                fontsize=6.5, color=INK_SECONDARY, ha="left", va="top")

    note_ax = axes.flat[5]
    note_ax.axis("off")
    note_ax.text(0.0, 0.95, NOTE, transform=note_ax.transAxes, fontsize=7,
                 color=INK, ha="left", va="top", linespacing=1.6)

    fig.subplots_adjust(hspace=0.40, wspace=0.04, top=0.90, bottom=0.02)
    save(fig, "fig2_repeat_units", OUT)


if __name__ == "__main__":
    main()
