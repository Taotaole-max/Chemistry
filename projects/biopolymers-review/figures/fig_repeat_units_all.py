"""=== Word Figure 3 ===  各家族的重复单元，一张多面板图（替代旧 Fig 3/6/7/8/9 五张）。

13 个单体排成 3 行 × 5 列，按主链化学类别成行：
  行 1 多糖：纤维素 / 直链淀粉 / 壳聚糖 / 海藻酸 M / 海藻酸 G
  行 2 聚酯 + 蛋白：PHB / PLLA / 丝素 / 胶原
  行 3 木质素 + 橡胶：对香豆醇 / 松柏醇 / 芥子醇 / 天然橡胶

SMILES 全部复用 fig2_repeat_units.py / fig12_appendix_monomers.py 里已核对的常量
（verify_stereochemistry / verify_appendix_stereochemistry 机器核对）。一个 Word 图注。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import verify_stereochemistry
import verify_appendix_stereochemistry
from fig2_repeat_units import PANELS as P2
from fig12_appendix_monomers import PANELS as P12
from style import FIG_W, apply_style, draw_mol, panel_title, save

OUT = Path(__file__).parent / "output"
B2 = {p[1]: p for p in P2}
B12 = {p[1]: p for p in P12}

# (tag, display name, smiles, colour, annotate_cip)
def _e(src, key, name):
    _, _, _chem, smiles, colour, ann = src[key]
    return (name, smiles, colour, ann)

GRID = [
    [_e(B2, "Cellulose", "Cellulose"),
     _e(B2, "Amylose (starch)", "Amylose"),
     _e(B2, "Chitosan", "Chitosan"),
     _e(B12, "Alginate M", "Alginate M"),
     _e(B12, "Alginate G*", "Alginate G")],
    [_e(B2, "PHB", "PHB"),
     _e(B2, "PLLA", "PLLA"),
     _e(B12, "Silk fibroin", "Silk fibroin"),
     _e(B12, "Collagen", "Collagen"),
     None],
    [_e(B12, "p-Coumaryl OH", "p-Coumaryl alc."),
     _e(B12, "Coniferyl OH", "Coniferyl alc."),
     _e(B12, "Sinapyl OH", "Sinapyl alc."),
     _e(B12, "Natural rubber", "Natural rubber"),
     None],
]

TAGS = "abcdefghijklmno"


def main():
    verify_stereochemistry.main()
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(3, 5, figsize=(FIG_W, 104 / 25.4), layout="constrained")

    k = 0
    for r in range(3):
        for c in range(5):
            ax = axes[r][c]
            cell = GRID[r][c]
            ax.axis("off")
            if cell is None:
                continue
            name, smiles, colour, ann = cell
            ax.imshow(draw_mol(smiles, annotate_cip=ann))
            panel_title(ax, TAGS[k], name, colour)
            k += 1

    save(fig, "fig_repeat_units_all", OUT)


if __name__ == "__main__":
    main()
