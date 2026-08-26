# 图是怎么做的

题目第 5 条要求"不要大量搬网图，欢迎自己画"。所以这里全部图**都由代码生成**，
脚本、数据、输出一起进仓库：图形是原创的，数据来自文献并逐条标注来源，
任何人（包括评卷人）都能重跑一遍验证。

**2026-08-26 结构性改版**：应用户要求，§3.1–3.5 每一节现在都有自己的单体结构图
和链尺度空间结构图，Fig 6（降解）拆成三张独立图，Fig 8 的记分卡改成 Table 5（原生
Word 表格），Fig 11（四图拼接总览）整个删掉，Fig 10（加工路线图）重新配色排版更接近
期刊风格，Fig 3（纤维素三级结构，现为 Fig 4）修了文字与图形重叠的问题。全部 19 张图
按**正文实际出现顺序**从 1 到 19 连续编号——编号对照表见下。附录 A（Fig 18/19）不计入
正文 10 页限制（和参考文献一样），保留作为"全部材料一次看全"的完整参考图，正文里的
对应小图会注明"完整版见 Fig 18/19"。

## 编号对照表（脚本文件名保持不变，只有 Word 里的图号变了）

| Word 图号 | 脚本 | 内容 | 所在章节 |
|---|---|---|---|
| Fig 1 | `fig1_classification.py` | 分类树（主链化学为主分支） | §2 |
| Fig 2 | `fig7_causality_chain.py` | 七个家族的结构–性质因果链总览 | §3 开头 |
| Fig 3 | `fig_polysaccharide_monomers.py`（新） | 多糖单体：纤维素/直链淀粉/壳聚糖/海藻酸盐 M/G | §3.1 |
| Fig 4 | `fig3_cellulose_hierarchy.py` | 纤维素三级结构（已修复文字重叠） | §3.1 |
| Fig 5 | `fig_polysaccharide_chains.py`（新） | 直链淀粉螺旋、海藻酸盐蛋盒、壳聚糖 H 键网络 | §3.1 |
| Fig 6 | `fig_polyester_structures.py`（新） | PHB/PLLA 单体 + PHA/PLA 螺旋堆积 | §3.2 |
| Fig 7 | `fig_protein_structures.py`（新） | 丝素/胶原蛋白单体 + 各自二级结构 | §3.3 |
| Fig 8 | `fig_lignin_monomers.py`（新） | 三种木质醇前体 | §3.4 |
| Fig 9 | `fig_rubber_monomer.py`（新） | 天然橡胶单体 | §3.5 |
| Fig 10 | `fig9_dispersity.py` | 分散度 Đ 跨家族对比 | §4 |
| Fig 11 | `fig4_thermal_windows.py` | 热性质与加工窗口 | §5.1 |
| Fig 12 | `fig5_property_map.py` | 模量 vs 断裂伸长 Ashby 图 | §5.2 |
| Fig 13 | `fig6a_polyester_hydrolysis.py`（原 Fig6a） | 聚酯主链水解机理 | §5.4 |
| Fig 14 | `fig6b_enzymatic_degradation.py`（原 Fig6b） | 多糖/蛋白酶促降解 | §5.4 |
| Fig 15 | `fig6c_hydrolysis_barriers.py`（原 Fig6c） | 酯水解能垒次序示意 | §5.4 |
| Fig 16 | `fig10_processing_routes.py` | 加工路线判定流程图（已重新配色） | §6 |
| Fig 17 | `fig8_nr_sbr_comparison.py`（现只剩结构面板） | NR/SBR 链尺度结构对比（紧凑版） | §7.3 |
| Fig 18 | `fig12_appendix_monomers.py` | 十五种材料重复单元合集（附录，完整参考） | 附录 A |
| Fig 19 | `fig13_appendix_chain_structures.py` | 六个家族链尺度结构合集（附录，完整参考） | 附录 A |
| Table 5 | 原 Fig 8 记分卡，改为原生表格 | NR vs SBR 七维度打分 | §7.3 |

旧的 `fig2_repeat_units.py`（原 Fig 2，纤维素/直链淀粉/壳聚糖/PHB/PLLA 五合一）和
`combine_1x4.py`（原 Fig 11，四图拼接总览）已从 `make_all.py` 的构建列表和
`build_docx.py` 的 `FIGURE_FILES` 里移除，脚本文件本身还留在目录里，仅供参考，
不再参与生成。`fig2_repeat_units.py` 的五个结构分别拆分进了 Fig 3（多糖部分）和
Fig 6（聚酯部分），没有丢失任何一个。

```
figures/
├── make_all.py                        # 一条命令生成全部图
├── style.py                           # 统一配色、字号、线宽、导出规格
├── verify_stereochemistry.py          # 机器核对糖类/聚酯的构型（Fig 3/6/18 共用）
├── verify_appendix_stereochemistry.py # 机器核对附录新增结构的构型/几何（Fig 18/9/17 等共用）
├── fig1_classification.py             ├── fig9_dispersity.py
├── fig3_cellulose_hierarchy.py        ├── fig10_processing_routes.py
├── fig4_thermal_windows.py            ├── fig12_appendix_monomers.py
├── fig5_property_map.py               ├── fig13_appendix_chain_structures.py
├── fig6a_polyester_hydrolysis.py      ├── fig_polysaccharide_monomers.py
├── fig6b_enzymatic_degradation.py     ├── fig_polysaccharide_chains.py
├── fig6c_hydrolysis_barriers.py       ├── fig_polyester_structures.py
├── fig7_causality_chain.py            ├── fig_protein_structures.py
├── fig8_nr_sbr_comparison.py          ├── fig_lignin_monomers.py
│                                       └── fig_rubber_monomer.py
├── (未参与构建，仅存档) fig2_repeat_units.py, fig6_degradation.py, combine_1x4.py
├── data/
│   ├── thermal_properties.csv       # Fig 11 数据（附 ref 列）
│   └── mechanical_properties.csv    # Fig 12 数据（附 ref 列）
└── output/                      # 生成的 SVG + 600 dpi PNG
```

跑法：

```bash
pip install -r requirements.txt
cd figures && python3 make_all.py
```

## 统一规格

| 项 | 规定 | 为什么 |
|---|---|---|
| 输出 | SVG + 600 dpi PNG | SVG 插进 Word 不糊、可缩放；PNG 用来校对 |
| 宽度 | 170 mm（通栏，与 2.54 cm 页边距的正文同宽） | 导出时就按物理尺寸设定，**不要在 Word 里再缩放** |
| 图内字体 | Arial 8 pt，最小 6 pt | 与正文 Times 12 pt 区分，缩到半栏仍可读 |
| 文字保留为文字 | `svg.fonttype = "none"` | Word 用系统 Arial 渲染，不是一堆路径 |
| 配色 | 5 色，已过色盲安全校验 | 见下 |
| 黑白兼容 | 颜色之外再加形状或线型 | 老师可能黑白打印 |
| 嵌入高度 | 三档：S 1.3in / M 1.9in / L 2.3in（`build_docx.py` 的 `FIGURE_HEIGHT_S/M/L`） | 之前每张图各自一个高度上限，大小参差不齐；改版统一成三档，视觉上更一致 |

**配色**：蓝 `#2a78d6` 多糖 · 橙 `#eb6834` 聚酯 · 绿 `#1baf7a` 蛋白 · 紫 `#4a3aa7` 石油基对照 · 灰 `#8a8a85` 其他。
全部图**颜色跟着材料类别走**，不跟着排名走——读者建立一次映射，全篇通用。
这五色在 all-pairs 模式下最差色盲对 ΔE 9.2、最差常视力对 ΔE 16.3，均达标；
绿色对白底对比度偏低，所以凡用到绿色的地方都配了直接标注。超过五类的一律折进灰色，不新增色相。
NR/SBR 的链尺度对比图（Fig 17/19f）刻意不给 SBR 一个"第六色"，两条链都用中性灰、
靠实线/虚线区分。

## §3.1–3.5：每节自己的单体图 + 链结构图

用户原话"把文章里出现的每一个高分子的单体 还有链的空间结构都作图表示出来"——上一版
只把这些图放进了附录（Fig 18/19），这一版改成**正文对应小节直接配图**，附录保留作为
完整参考合集，不是唯一出处。六张新图全部复用 `fig2_repeat_units.py` /
`fig12_appendix_monomers.py` / `fig13_appendix_chain_structures.py` 里已经核验过的
SMILES 和布局逻辑（`import` 复用，没有重新敲一遍立体化学）：

- **Fig 3**（`fig_polysaccharide_monomers.py`）：纤维素、直链淀粉、壳聚糖、海藻酸盐
  M/G 五个单体，(a)/(b) 只差 C1、(d)/(e) 只差 C5，一眼看出构型差异对应的性质差异。
- **Fig 4**：原 Fig 3，纤维素三级结构，**这一版修了文字与图形重叠的 bug**（面板 (a)
  的氢键标注和面板 (c) 的说明文字都调整了间距/位置，重新渲染后目视确认无重叠）。
- **Fig 5**（`fig_polysaccharide_chains.py`）：直链淀粉左手螺旋、海藻酸盐蛋盒结构、
  壳聚糖乙酰化打断氢键网络——三格并排，纤维素的链尺度结构已经在 Fig 4 讲完不重复。
- **Fig 6**（`fig_polyester_structures.py`）：PHB/PLLA 单体 + PHA/PLA 的螺旋堆积
  （2₁/10₃ 螺旋），单体和链结构合在一张图里，因为 PHA/PLA 这两个尺度篇幅都不大。
- **Fig 7**（`fig_protein_structures.py`）：丝素蛋白 (Gly-Ala)ₙ / 胶原蛋白 Gly-Pro-Hyp
  两个单体，配各自的二级结构——丝素的 β-折叠纳米晶体、胶原的三螺旋，2x2 布局。
- **Fig 8**（`fig_lignin_monomers.py`）：三种木质醇前体（对香豆醇/松柏醇/芥子醇，
  0/1/2 个甲氧基）。木质素没有周期性链，只有单体值得画，正文写明了这一点。
- **Fig 9**（`fig_rubber_monomer.py`）：天然橡胶单体，*顺*-1,4-聚异戊二烯；链尺度的
  应变诱导结晶结构不在这里重复，留给 §7.3 的 Fig 17（NR vs SBR 案例研究）。

## 正文其余图（沿用之前版本的设计，只是编号变了）

### Fig 1 · 分类树（§2）
手工计算坐标的层级图。主分支是主链化学类别（五类，和 Table 1、Fig 2 完全对齐），
叶子是正文 §3 实际讨论过的材料，每个叶子右上角一个小圆标来源（E=提取 / M=微生物合成 /
S=生物基单体聚合）。

### Fig 2 · 结构–性质因果链一览（§3 总览图）
七个家族一行一条因果链：重复单元化学 → 主导分子间作用力 → 关键性质结果 → 关键局限，
颜色跟 `CLASS_COLOR` 走。替掉了 §3 正文里大段的机理复述。

### Fig 10 · 分散度 Đ 跨家族对比（§4）
蛋白质/核酸精确等于 1.00（模板合成），天然橡胶没有可靠文献定量值，画成开口箭头并
写明"未定量"。Table 3 因此不用再重复 Đ 这一列。

### Fig 11 · 热性质与加工窗口（§5.1）
数据来自 `data/thermal_properties.csv`。Tg（空心圆）、Tm（实心菱形）、分解起始温度
（竖线）画在同一温标上，Tm 到 Td 之间的阴影就是熔融加工窗口。

### Fig 12 · 性能图：模量 vs 断裂伸长（§5.2）
数据来自 `data/mechanical_properties.csv`。画区间椭圆而不是单点。

### Fig 13/14/15 · 降解机理（§5.4，原 Fig 6 的三格拆成三张独立图）
原来是一张图三个面板，图内文字被批评"太多"。现在拆开：Fig 13 只画聚酯水解反应式，
Fig 14 只画酶解可及性示意，Fig 15 只画能垒次序示意——每张图单独成图、单独一句短
说明，不再挤在一张图里对比着看。三张图仍然按顺序紧跟在 §5.4 同一段论证里出现。

### Fig 16 · 加工路线决策图（§6，原 Fig 10）
**这一版重新配色排版**：原来是圆角实心色块的流程图，偏"演示文稿"风格；改成细线框 +
色条强调的样式，向 Fig 2（因果链）、Fig 11/12（分析类图）等更克制的期刊风格靠拢，
内容和判定逻辑完全没变。

### Fig 17 · NR vs. SBR 案例研究结构图（§7.3，原 Fig 8）
原来是"结构面板 + 记分卡"两块拼在一张图里；记分卡改成了 Table 5（原生 Word 表格，
可编辑可搜索），这里只保留链尺度结构对比：NR 静置无定形卷曲 → 受力应变诱导结晶成
有序束；SBR 受力后仍保持无定形。完整六格版本在附录 Fig 19(f)。

## 附录 A（Fig 18/19）：完整参考合集，不计入正文 10 页限制

§3.1–3.5 已经把每种材料的单体图和链结构图安排进了对应小节，附录不再是"唯一出处"，
而是"全部材料一次看全"的参考合集，方便回查、也覆盖了正文小图里省略的少数结构
（比如 SBR 的两个共聚单体，§7.3 没有单独画出）。

### Fig 18 · 十五种材料的重复单元合集（附录 A，原 Fig 12）
和正文 Fig 3/6 同一套 SMILES（`import` 复用，非重新核验）。**立体化学怎么核对**
（`verify_appendix_stereochemistry.py`，出图前自动跑，不通过就报错停下）：天然橡胶
的顺式几何、SBR 两种共聚单体、三种木质醇、丝素/胶原蛋白的手性碳都核对到了和文献一致。
**唯一一处没有完全核实的地方**：海藻酸盐 G（古洛糖醛酸）的绝对构型，只核对了
"是 M 的 C5 差向异构体"这个文献公认的关系，手头没有独立的文献 CIP 字符串可以直接
比对——图注和 `report.md`/`report_zh.md` 里都老实标出了这一点，建议提交前找 ChemDraw
或文献结构图再核一遍。

### Fig 19 · 六个家族的链尺度空间结构合集（附录 A，原 Fig 13）
matplotlib 手绘示意图，六格，和正文 Fig 4/5/6/7/17 是同一批图的完整版合集（(f) 面板
即 Fig 17 的完整六格版本）。纤维素已经在 Fig 4 单独成图，这里不重复。

## 表格

Table 1–4 **不做成图片**，直接在 Word 里排三线表（top rule / header rule / bottom rule，
无竖线），这是化学期刊的标准表格样式，可编辑、可搜索、打印清楚。

**Table 5**（新增，§7.3）：NR vs. SBR 七维度打分，原来是 Fig 8 的一个记分卡面板
（matplotlib 画的彩色圆点状态标记），这一版改成和 Table 1-4 同规格的原生 Word 表格——
用户反馈"图片大小不一，看起来乱"，这类纯打分表格本来就该是表格而不是图。

## 数据的诚实状态

`data/*.csv` 里所有数值目前标的是 **PROVISIONAL**：教科书量级的常见值，用来把图的形式和
论证走通，**还没有逐条核对原始文献**。核对时两件事必须一起处理：

- 把 `ref` 列换成真实引用编号；
- 统一 Td 的定义（本表取"氮气下 TGA 显著失重起始温度"，文献里也有用 5% 失重或最大失重速率
  温度的，差 30–50 °C），Tg 必须同时报含水量与增塑剂条件。

## 插进 Word 的实操

1. 插入 → 图片 → 选 **SVG**（Word 2016+ 原生支持矢量）
2. 版式设"嵌入型"，不要"四周环绕"——否则改一处正文全图乱跑
3. 图注用**题注**功能（引用 → 插入题注），自动编号
4. 正文里的 "Figure 3" 用**交叉引用**，图序变动后不用手改
5. 图注统一格式：`Figure N. 说明文字. Drawn by the authors; data from [ref].`
   —— 最后半句直接回应题目第 5、6 条
6. **图片和图注必须留在同一页**：`build_docx.py` 给每个图片段落设了
   `keep_with_next = True`，否则 Word 有时会把图注单独推到下一页、留一页几乎空白
   （这次 PDF 视觉核对时在附录 Fig 19 上抓到过一次，已修复并对所有图生效）。
