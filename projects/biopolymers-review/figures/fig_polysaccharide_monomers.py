"""=== Word Figure 3 ===  §3.1 多糖重复单元一览：纤维素、直链淀粉、壳聚糖、海藻酸盐 M/G。

放在 3.1 小节正文里（不是附录），让"结构决定性质"这条论证在读到对应材料时就有图可看。
SMILES 直接复用 fig2_repeat_units.py / fig12_appendix_monomers.py 里已经过
verify_stereochemistry.py / verify_appendix_stereochemistry.py 核对的常量，不重新
手写，保证和那两张图里的构型完全一致（同一个 SMILES 字符串）。

排版：170 mm 通栏、5 个单体等距铺满、H_S 高度、constrained layout。化学名和
"(a)/(b) 只差 C1、(d)/(e) 只差 C5"这段解释都挪进 report.md 的图注，图上只留 (a)…(e)。
"""

from pathlib import Path

import matplotlib.pyplot as plt

import verify_stereochemistry
import verify_appendix_stereochemistry
from fig2_repeat_units import PANELS as FIG2_PANELS
from fig12_appendix_monomers import PANELS as FIG12_PANELS
from style import FIG_W, H_S, apply_style, draw_mol, panel_title, save

OUT = Path(__file__).parent / "output"

BY_NAME_2 = {p[1]: p for p in FIG2_PANELS}
BY_NAME_12 = {p[1]: p for p in FIG12_PANELS}

# 复用 Fig 2 / Fig 12 已核对的 SMILES；PANELS 元组是
# (tag, name, chem_name, smiles, colour, annotate)，[3:] 取 (smiles, colour, annotate)。
PANELS = [
    ("a", "Cellulose", *BY_NAME_2["Cellulose"][3:]),
    ("b", "Amylose", *BY_NAME_2["Amylose (starch)"][3:]),
    ("c", "Chitosan", *BY_NAME_2["Chitosan"][3:]),
    ("d", "Alginate M", *BY_NAME_12["Alginate M"][3:]),
    ("e", "Alginate G", *BY_NAME_12["Alginate G*"][3:]),
]


def main():
    verify_stereochemistry.main()
    verify_appendix_stereochemistry.main()

    apply_style()
    fig, axes = plt.subplots(1, 5, figsize=(FIG_W, H_S / 25.4), layout="constrained")

    for ax, (tag, name, smiles, colour, annotate) in zip(axes, PANELS):
        ax.imshow(draw_mol(smiles, annotate_cip=annotate))
        ax.axis("off")
        panel_title(ax, tag, name, colour)

    save(fig, "fig_polysaccharide_monomers", OUT)


if __name__ == "__main__":
    main()
