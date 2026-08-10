# Chemistry

化学计算与仿真代码

## 项目结构

```
Chemistry/
├── data/           # 输入/输出数据文件
├── src/            # 计算/仿真脚本
├── projects/       # 独立的小项目，每个子目录自带 README / requirements
│   └── bandgap-prediction-rf/   # 随机森林预测材料带隙
├── requirements.txt
└── README.md
```

## 环境准备

```bash
pip install -r requirements.txt
```

## 项目

- [分子/材料能带预测（RF）](projects/bandgap-prediction-rf/README.md) —— 用 Materials Project 数据 + matminer 特征工程 + 随机森林预测带隙。

## 学习资料

[AI for Chemistry 学习指导](docs/AI_FOR_CHEMISTRY_GUIDE.md) —— 机器学习 + 化学材料科学的入门路线图，含精选仓库、课程和 2026 前沿论文。
