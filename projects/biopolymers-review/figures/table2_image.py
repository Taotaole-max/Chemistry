"""Table 2 · 代表性生物聚合物热学/力学/结构性质概览，渲染成图片（中英各一版）。

内容和 report_zh.md / report.md 里 Table 2 的 markdown 表格逐字对应，只是从原生
Word 表格换成一张图，配色沿用 CLASS_COLOR（材料名前的圆点标主链化学类别，
和 fig4/fig5/fig7 保持同一套图例），方便和其余图片一起排版、也更好控制列宽/换行。

跑法：python3 table2_image.py（同时生成中文版 table2_properties_zh.png/svg
和英文版 table2_properties_en.png/svg）
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

from style import CLASS_COLOR, INK, INK_SECONDARY, MM, apply_style, save

CJK_FONT_STACK = ["Microsoft YaHei", "SimHei", "SimSun", "Arial", "DejaVu Sans"]

HERE = Path(__file__).parent
OUT = HERE / "output"

# (material_zh, material_en, class, thermal, modulus, elongation, crystallinity_zh, crystallinity_en)
ROWS = [
    ("纤维素", "Cellulose", "polysaccharide",
     "n/o / no melt / ~300", "10–30", "8–15",
     "60–70%；NMMO/Lyocell、LiCl/DMAc", "60–70%; NMMO/Lyocell, LiCl/DMAc"),
    ("淀粉（TPS）", "Starch (TPS)", "polysaccharide",
     "~−20 / no melt / ~300", "0.02–1.0", "20–100",
     "半结晶，依赖湿度；TPS 共混", "semicryst., humidity-dep.; TPS blend"),
    ("壳聚糖", "Chitosan", "polysaccharide",
     "n/o / no melt / ~280", "1.0–4.0", "3–30",
     "低–中；稀酸溶液", "low–moderate; dilute-acid solution"),
    ("丝素蛋白", "Silk fibroin", "protein",
     "~175 / no melt / ~300", "5–17", "15–30",
     "β-折叠纳米晶；溶液纺丝", "β-sheet nanocrystalline; solution-spun"),
    ("PHB", "PHB", "polyester",
     "4 / 175 / ~200", "1.5–4.0", "2–8",
     "55–70%；熔融，窗口窄", "55–70%; melt, narrow window"),
    ("PHBV（20% HV）", "PHBV (20% HV)", "polyester",
     "0 / 145 / ~200", "0.8–2.5", "5–25",
     "低于 PHB；熔融，窗口较宽", "< PHB; melt, wider window"),
    ("PLLA", "PLLA", "polyester",
     "60 / 175 / ~300", "2.5–4.0", "3–10",
     "结晶缓慢；熔融，需干燥", "slow-crystallising; melt, needs drying"),
    ("PBS", "PBS", "polyester",
     "−32 / 114 / ~350", "0.3–0.7", "200–500",
     "中等；熔融，窗口宽", "moderate; melt, wide window"),
    ("天然橡胶", "Natural rubber", "other",
     "low / SIC only / n/a", "0.001–0.005", "500–800",
     "应变诱导 [19]；胶乳凝结/硫化", "strain-induced [19]; latex coag./vulc."),
    ("LDPE（对照）", "LDPE (ref.)", "petro",
     "−120 / 110 / ~400", "0.15–0.35", "200–600",
     "中等；熔融，窗口很宽", "moderate; melt, very wide window"),
    ("PET（对照）", "PET (ref.)", "petro",
     "78 / 255 / ~400", "2.0–4.0", "50–300",
     "中等；熔融，窗口宽", "moderate; melt, wide window"),
]

HEADERS_ZH = ["材料", "Tg/Tm/Td (°C)", "模量 (GPa)", "断裂伸长率 (%)", "结晶度/加工方式"]
HEADERS_EN = ["Material", "Tg/Tm/Td (°C)", "Modulus (GPa)", "Elongation (%)", "Crystallinity / processing"]

COL_X = [0.0, 2.35, 3.55, 4.75, 6.05]
COL_W = [2.35, 1.20, 1.20, 1.30, 3.75]
TOTAL_W = COL_X[-1] + COL_W[-1]
ROW_H = 0.62
HEADER_H = 0.62


def render(mat_idx, crys_idx, headers, stem, note, cjk=False):
    apply_style()
    if cjk:
        mpl.rcParams["font.sans-serif"] = CJK_FONT_STACK
        mpl.rcParams["axes.unicode_minus"] = False
    n = len(ROWS)
    fig_h = HEADER_H + n * ROW_H + 0.55
    fig, ax = plt.subplots(figsize=(TOTAL_W * 28 * MM, fig_h * 28 * MM))
    ax.set_xlim(0, TOTAL_W)
    ax.set_ylim(-0.55, HEADER_H + n * ROW_H)
    ax.axis("off")

    # Header band
    ax.add_patch(Rectangle((0, n * ROW_H), TOTAL_W, HEADER_H,
                           facecolor=INK, edgecolor="none", zorder=1))
    for x, w, label in zip(COL_X, COL_W, headers):
        ax.text(x + 0.10, n * ROW_H + HEADER_H / 2, label, fontsize=8.5,
                fontweight="bold", color="#ffffff", ha="left", va="center", zorder=2)

    for i, row in enumerate(ROWS):
        y0 = (n - i - 1) * ROW_H
        if i % 2 == 1:
            ax.add_patch(Rectangle((0, y0), TOTAL_W, ROW_H,
                                   facecolor="#f4f4f1", edgecolor="none", zorder=1))
        colour = CLASS_COLOR[row[2]]
        cy = y0 + ROW_H / 2

        ax.add_patch(Circle((COL_X[0] + 0.09, cy), 0.075, facecolor=colour,
                            edgecolor="none", zorder=3))
        ax.text(COL_X[0] + 0.26, cy, row[mat_idx], fontsize=8.0, color=INK,
                ha="left", va="center", zorder=3, fontweight="bold")

        for col, x, w in zip((3, 4, 5), COL_X[1:4], COL_W[1:4]):
            ax.text(x + w / 2, cy, row[col], fontsize=7.6, color=INK_SECONDARY,
                    ha="center", va="center", zorder=3)

        ax.text(COL_X[4] + 0.10, cy, row[crys_idx], fontsize=7.3, color=INK_SECONDARY,
                ha="left", va="center", zorder=3)

    ax.plot([0, TOTAL_W], [-0.06, -0.06], color=INK_SECONDARY, lw=0.8)
    ax.text(0.0, -0.45, note, fontsize=6.3, color=INK_SECONDARY, ha="left", va="top")

    save(fig, stem, OUT)


def main():
    render(0, 6, HEADERS_ZH, "table2_properties_zh",
           "数量级估计范围，部分数值仍为 PROVISIONAL，详见正文与 figures/data/*.csv。", cjk=True)
    render(1, 7, HEADERS_EN, "table2_properties_en",
           "Order-of-magnitude ranges; several values still PROVISIONAL — see body text and figures/data/*.csv.")


if __name__ == "__main__":
    main()
