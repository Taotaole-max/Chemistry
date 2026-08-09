# AI for Chemistry 学习指导

给零基础入门者的机器学习 + 化学材料科学路线图。每一条资源都是可以直接打开的仓库或课程，整理于 2026-08。

## 学习路径

三个阶段可以叠着走，不必等前一个"学完"再开始下一个：

1. **机器学习基础** —— 监督学习、神经网络、训练/验证的基本直觉。目标是能读懂一篇 ML 论文的方法部分。
2. **化学信息学工具** —— 学会用 RDKit 把分子变成机器能处理的数字表示，这是所有化学 ML 项目的地基。
3. **领域交叉应用** —— 用 DeepChem / SchNetPack 跑通一个真实的分子性质预测或势能面拟合任务。

## 先从这里开始：更简单的中文资源

如果觉得正式教材（d2l、吴恩达课程）一上来就有点吃力，先从这几个更轻松的入口摸一摸门道，不用数学基础也能看懂。

| 资源 | 类型 | 说明 |
|---|---|---|
| [MorvanZhou/tutorials](https://github.com/MorvanZhou/tutorials) | 图文+视频 | "莫烦Python"，公认中文圈最好懂的机器学习/深度学习入门教程，从"什么是神经网络"讲起，例子生活化，几乎不需要数学基础 |
| [MLEveryday/100-Days-Of-ML-Code](https://github.com/MLEveryday/100-Days-Of-ML-Code) | 每日小任务 | 把机器学习拆成 100 个小步骤，每天只学一点、跑一小段代码，不会有"一节课学不完"的挫败感 |
| [datawhalechina/leedl-tutorial](https://github.com/datawhalechina/leedl-tutorial) | 课程（苹果书） | 李宏毅老师的深度学习课程讲义，风格幽默、举例生活化，是中文圈公认最好懂的深度学习课之一，配套视频 |
| [zjtdzyx/machine-learning-project](https://github.com/zjtdzyx/machine-learning-project) | 练习项目 | 六个经典算法的完整小项目，代码、训练、评估、可视化都有，适合"先跑起来一个能用的东西"再回头理解原理 |
| [fengdu78/machine_learning_beginner](https://github.com/fengdu78/machine_learning_beginner) | 短文合集 | 公众号"机器学习初学者"的文章合集，短小的概念讲解，适合碎片时间读 |

跟着这几个先建立感觉，等不再觉得"看不懂"了，再回到下面更系统、也更硬核的资源。

## 机器学习基础入门（更系统，也更硬核）

不涉及化学，把 ML 当成一门完整的学科来学。这一层数学和工程量都更大，建议在上面的入门资源之后再来。

| 资源 | 类型 | 说明 |
|---|---|---|
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 课程 | 12 周 26 课时，配测验和小项目，Python 为主，零基础友好，中文翻译齐全 |
| [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh) | 教材 | 《动手学深度学习》，李沐团队编写，理论 + 可运行代码 + 配套视频 |
| [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) | 课程 | Andrew Ng 在 Coursera 的经典课程，监督/无监督学习和神经网络基础，免费旁听 |
| [fast.ai · Practical Deep Learning](https://course.fast.ai/) | 课程 | 先动手训练一个能用的模型，再回头讲原理，适合"跑起来再理解"的学习方式 |
| [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 工具清单 | 按语言分类的 ML 框架与库大全 |

## 化学信息学基础工具

在做 ML 之前，先能把分子/材料数字化。这三个库不是"机器学习库"，但几乎所有化学 ML 项目都构建在它们之上。

| 资源 | 领域 | 说明 |
|---|---|---|
| [rdkit/rdkit](https://github.com/rdkit/rdkit) | 分子表示 | 化学信息学的事实标准库：把 SMILES 分子式转成指纹、描述符、3D 构象 |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | 晶体/材料 | Materials Project 出品，处理晶体结构、相图、电子结构数据 |
| [hackingmaterials/matminer](https://github.com/hackingmaterials/matminer) | 特征工程 | 劳伦斯伯克利实验室 Hacking Materials 团队出品，把材料结构批量转换成 ML 可用的特征向量 |

## 化学 × 深度学习框架

分子性质预测 / 势能面 / 材料生成。建议按顺序尝试：DeepChem 门槛最低，SchNetPack 和 MACE 更贴近器件仿真背景。

| 资源 | 方向 | 说明 |
|---|---|---|
| [deepchem/deepchem](https://github.com/deepchem/deepchem) | 入门首选 | 化学 + 材料科学的高层 ML 工具箱，内置图神经网络、分子指纹、材料科学教程 |
| [atomistic-machine-learning/schnetpack](https://github.com/atomistic-machine-learning/schnetpack) | 势能面 | 用深度网络预测分子和材料的势能面、量子化学性质 |
| [ACEsuit/mace](https://github.com/ACEsuit/mace) | 原子间势 | 等变图神经网络原子间势，材料模拟里常用的基准模型之一 |
| [FAIR-Chem/fairchem](https://github.com/FAIR-Chem/fairchem) | 催化/材料 | Meta FAIR 化学团队维护，源自 Open Catalyst Project，提供开箱即用的原子尺度基础模型 |

## 2026 前沿：机器学习原子间势

目前"ML + 材料"里最活跃的子方向 —— 用图神经网络直接学习原子间的相互作用力，替代传统的量子化学计算，速度提升几个数量级。等走完前两个阶段，这些论文会读起来顺手很多。

- **[MLANet（2026）](https://arxiv.org/abs/2603.22810)** —— 动态注意力图神经网络原子间势。用双路径动态注意力做几何感知的消息传递，在分子、周期性材料、二维材料和表面催化反应上都测试过，计算成本比主流等变模型低不少。
- **[GRACE（2026）](https://www.nature.com/articles/s41524-026-01979-1)** —— 图原子簇展开。把传统的"原子簇展开"方法和图神经网络结合，作为下一代原子尺度基础模型的通用框架。
- **[PET-MAD（2025）](https://www.nature.com/articles/s41467-025-65662-7)** —— 轻量级通用原子间势。在无机固体和有机分子的混合数据集上训练，专门为"跨材料体系通用"这个目标做了数据多样性优化。
- **[UniFFBench（2026）](https://arxiv.org/abs/2508.05762)** —— 通用力场的实验基准评测。拿真实实验测量数据检验这些"通用"力场模型到底有多准。

## 延伸清单

需要找更细分的工具时再查：

- [lmmentel/awesome-python-chemistry](https://github.com/lmmentel/awesome-python-chemistry) —— Python 化学相关包的分类大全，量子化学、分子动力学、化学信息学都覆盖了
- [armankhondker/awesome-ai-ml-resources](https://github.com/armankhondker/awesome-ai-ml-resources) —— 免费 AI/ML 资源和路线图合集

## 建议的第一步

别一次啃完整个清单。先看几集"莫烦Python"或跟着 100-Days-Of-ML-Code 走几天，找到"看得懂"的感觉；之后再跑通 `deepchem` 的 `Introduction_To_Material_Science` 教程 notebook，跑通后回到 `src/` 下写一个用 RDKit 算分子指纹 + scikit-learn 做简单性质预测的小脚本 —— 这一步能把入门、阶段一和阶段二串起来。

---

整理时间 2026-08，资源本身持续更新，建议以各仓库最新 README 为准。
