# 分子/材料能带预测（RF）

用材料的化学成分特征预测带隙（band gap），走通「取数据 → 特征工程 → 训练模型 → 看特征重要性」的完整机器学习流程。目前用随机森林（Random Forest）打底，方便后续替换成 XGBoost / GNN 做对比。

## 数据与方法

- **数据来源**：[Materials Project](https://materialsproject.org)，通过 `mp-api` 拉取 `energy_above_hull` 在 0~0.02 eV/atom 之间（即热力学稳定）的材料，字段包括 `material_id`、`formula_pretty`、`band_gap`。
- **特征工程**：[matminer](https://hackingmaterials.lbl.gov/matminer/) 的 `ElementProperty`（`magpie` 预设），把化学式（`pymatgen.Composition`）转成一组基于元素属性统计量的数值特征。
- **模型**：`sklearn.ensemble.RandomForestRegressor`（300 棵树），`train_test_split` 做 8:2 切分。
- **评估**：MAE、R²，以及前 15 个最重要特征的条形图。

## 目录结构

```
bandgap-prediction-rf/
├── 01_bandgap_prediction.py   # 主脚本
├── requirements.txt
├── .env.example                # API key 模板，复制成 .env 并填入真实 key
└── README.md
```

## 环境准备

```bash
cd projects/bandgap-prediction-rf
pip install -r requirements.txt
cp .env.example .env   # 然后把 MP_API_KEY 换成你自己的
```

`MP_API_KEY` 在 [Materials Project 个人主页](https://next-gen.materialsproject.org/api) 申请，注意 `.env` 不要提交到 Git（已在仓库根目录的 `.gitignore` 里忽略）。

## 运行

```bash
python 01_bandgap_prediction.py
```

脚本默认只取前 1000 条数据跑通流程；确认电脑不会崩、流程没问题之后，把 `df = df.head(1000)` 这行删掉即可跑全量数据。

## 已知限制 / 后续练习方向

- 特征工程是单进程逐行跑的（`ep_feat.featurize` 在循环里调用），是为了避免 Windows 下 matminer 多进程崩溃，数据量大时会慢，可以考虑批量 `featurize_dataframe` 或换 Linux/WSL 环境用多进程加速。
- 换预测目标：`formation_energy_per_atom`（形成能）。
- 换模型：试试 XGBoost / GradientBoosting，对比 MAE 有没有改善。
- 加限制条件：只挑半导体材料（`0 < band_gap < 4`），看模型在这个子集上表现如何——这一步是为「半导体带隙 + 主动学习」方向做铺垫。
