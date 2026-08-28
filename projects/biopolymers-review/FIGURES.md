# 图是怎么做的

题目第 5 条要求"不要大量搬网图，欢迎自己画"。所以这里全部图**都由代码生成**，
脚本、数据、输出一起进仓库：图形是原创的，数据来自文献并逐条标注来源，
任何人（包括评卷人）都能重跑一遍验证。

跑法：

```bash
pip install -r requirements.txt          # matplotlib + numpy + rdkit
cd figures && python make_all.py          # 生成全部 15 张图到 output/
cd .. && python build_docx.py             # 英文 report.md -> docx
python build_docx.py report_zh.md Biopolymers-review-DRAFT-ZH.docx SimSun   # 中文对照
```

## 2026-08-28 大改：19 张 → 15 张，删掉附录

用户反馈"图太多、太乱、画幅不统一"。这一轮：

1. **删掉附录 A**（原 Fig 18/19 两张合集图）。§3.1–3.5 每节已有自己的单体图和链结构图，
   附录是重复。附录独有的 SBR 两个共聚单体并进了 §7.3 的 Fig 15。
2. **降解三张零碎图**（原 Fig 13/14/15）→ 13（酯水解反应式）+ 14（酶解可及性）合并成
   一张两面板图（`fig6_degradation.py` → `output/fig_degradation.png`）；15（能垒示意
   曲线，本来就"仅示意、不含数值"的计算旁支）删掉，正文 §5.4 一句话带过。
3. **统一画幅**（`style.py`）：
   - 所有图固定 **170 mm 通栏宽**，`save()` 不再用 `bbox_inches="tight"`（导出尺寸 ==
     figsize，Word 里所有图同一比例、同一字号）；配合 constrained layout 保证标签不被裁。
   - 图内不再写大标题、不写整段说明——都进 Word 图注（`report.md` / `report_zh.md` 的
     `*[Figure N — ...]*` 占位行）。
   - 分子式统一走 `style.draw_mol()`：同一线宽、同一字号、同一画布像素、自动裁白边，
     跨图分子大小一致。
4. **Table 2** 从散点图（`table2_scatter`，已删）改回 `report.md` 里的真三线表。
5. 脚本文件名保持不变（历史原因），每个脚本开头加了 `=== Word Figure N ===` 注释对齐图号。

## 编号对照表

| Word 图号 | 脚本 | 内容 | 章节 |
|---|---|---|---|
| Fig 1 | `fig1_classification.py` | 分类树（主链化学为主分支） | §2 |
| Fig 2 | `fig7_causality_chain.py` | 结构–性质因果链（5 类主链、7 行） | §3 开头 |
| Fig 3 | `fig_polysaccharide_monomers.py` | 多糖单体：纤维素/直链淀粉/壳聚糖/海藻酸 M/G | §3.1 |
| Fig 4 | `fig3_cellulose_hierarchy.py` | 纤维素三级结构 | §3.1 |
| Fig 5 | `fig_polysaccharide_chains.py` | 直链淀粉螺旋 / 海藻酸蛋盒 / 壳聚糖无序化 | §3.1 |
| Fig 6 | `fig_polyester_structures.py` | PHB/PLLA 单体 + PHA/PLA 螺旋堆积 | §3.2 |
| Fig 7 | `fig_protein_structures.py` | 丝素/胶原单体 + 各自二级结构 | §3.3 |
| Fig 8 | `fig_lignin_monomers.py` | 三种单木质醇前体 | §3.4 |
| Fig 9 | `fig_rubber_monomer.py` | 天然橡胶单体 | §3.5 |
| Fig 10 | `fig9_dispersity.py` | 分散度 Đ 跨家族对比 | §4 |
| Fig 11 | `fig4_thermal_windows.py` | 热性质与加工窗口 | §5.1 |
| Fig 12 | `fig5_property_map.py` | 模量 vs 断裂伸长 Ashby 图 | §5.2 |
| Fig 13 | `fig6_degradation.py` | 酯水解 + 酶解可及性，两面板 | §5.4 |
| Fig 14 | `fig10_processing_routes.py` | 加工路线判定流程图 | §6 |
| Fig 15 | `fig8_nr_sbr_comparison.py` | NR + SBR 单体 + 链尺度应变结晶对比 | §7.3 |

**仅作为共享 SMILES / panel 函数被 import、不参与构建**：`fig2_repeat_units.py`、
`fig12_appendix_monomers.py`、`fig13_appendix_chain_structures.py`。
**已废弃**：`combine_1x4.py`、`fig6c_hydrolysis_barriers`（原 Fig 15 能垒图）、
`table2_image.py`、`table2_scatter.py`。

## 统一规格（`style.py`）

| 项 | 规定 |
|---|---|
| 输出 | SVG（进 Word）+ 600 dpi PNG（校对） |
| 宽度 | **固定 170 mm**，`FIG_W` 常量，`save()` 用 `bbox_inches=None` |
| 高度 | 三档 `H_S 34 / H_M 52 / H_L 64` mm，对齐 `build_docx.py` 的嵌入高度上限 |
| 图内字号 | 面板标签 8 pt bold、短标注 6.5 pt、次要 6 pt（画布尺寸固定 → 所见即所得） |
| 配色 | 蓝多糖 `#2a78d6` · 橙聚酯 `#eb6834` · 绿蛋白 `#1baf7a` · 紫石油基对照 `#4a3aa7` · 灰其他 `#8a8a85`，已过色盲 all-pairs 校验 |
| 分子式 | `draw_mol()`：`bondLineWidth=3`、`fixedFontSize=38`、760×520 px、自动裁白边；`(R)/(S)` 只在立体化学是重点时标（多糖 C1/C5、聚酯） |

## 数据的诚实状态

`data/thermal_properties.csv` / `mechanical_properties.csv` 里的数值**仍是 PROVISIONAL**，
只有 PBS（[12]）和 PHB 的分解机理（[5]）真正核对过。Table 2、Table 3 同样。提交前必须
逐条对一手文献，并统一 Td 定义（本表取 N₂ 下 TGA 显著失重起始温度）、Tg 报含水量条件。

海藻酸盐 G（古洛糖醛酸）的绝对构型只核对了"与 M 互为 C5 差向异构体"，没有独立 CIP
字符串比对——提交前用 ChemDraw 或文献结构图再核一遍（图 3 图注已标注）。

## 插进 Word 的实操

`build_docx.py` 已经处理：SVG 按 `FIGURE_MAX_HEIGHT_IN` 的三档高度上限嵌入、宽度由
图自身宽高比反推（封顶 6.5 in），图片段落 `keep_with_next=True` 防止图注被推到下一页。
图注格式 `Figure N. 说明. Drawn by the authors; data from [ref].`（回应题目第 5、6 条）。
