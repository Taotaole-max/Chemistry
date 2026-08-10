# %% [markdown]
# # 项目 1：用材料成分/结构特征预测带隙 (band gap)
#
# 数据来源：Materials Project (https://materialsproject.org)
# 特征工程：matminer
# 模型：随机森林 (先跑通流程，之后可以换 XGBoost / GNN)

# %%
import os
import pandas as pd
from mp_api.client import MPRester
from dotenv import load_dotenv

from pymatgen.core import Composition
from matminer.featurizers.composition import ElementProperty

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

import matplotlib.pyplot as plt


def main():
    load_dotenv()
    MP_API_KEY = os.environ.get("MP_API_KEY")

    # ---- 1. 从 Materials Project 拉数据 ----
    with MPRester(MP_API_KEY) as mpr:
        docs = mpr.materials.summary.search(
            energy_above_hull=(0, 0.02),      # 只要热力学稳定的材料
            fields=["material_id", "formula_pretty", "band_gap"],
            chunk_size=1000,
        )
    print(f"拿到 {len(docs)} 条材料数据")

    rows = []
    for d in docs:
        rows.append({
            "material_id": d.material_id,
            "formula": d.formula_pretty,
            "band_gap": d.band_gap,
        })
    df = pd.DataFrame(rows)
    print(df.head())

    # 先用小数据集测试，确认整个流程没问题、电脑不会崩之后，再删掉这行跑全量
    df = df.head(1000)

    # ---- 2. 用 matminer 做特征工程（单进程逐行处理，避免 Windows 多进程崩溃）----
    df["composition"] = df["formula"].apply(Composition)

    ep_feat = ElementProperty.from_preset("magpie")
    feature_cols = ep_feat.feature_labels()

    feat_rows = []
    for comp in df["composition"]:
        try:
            feat_rows.append(ep_feat.featurize(comp))
        except Exception:
            feat_rows.append([None] * len(feature_cols))

    feat_df = pd.DataFrame(feat_rows, columns=feature_cols, index=df.index)
    df = pd.concat([df, feat_df], axis=1)
    df = df.dropna()
    print(df.shape)

    # ---- 3. 训练一个随机森林做回归预测 ----
    X = df[feature_cols]
    y = df["band_gap"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=300, n_jobs=1, random_state=42)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, pred))
    print("R2 :", r2_score(y_test, pred))

    # ---- 4. 看看哪些特征最重要 ----
    importances = pd.Series(model.feature_importances_, index=feature_cols)
    importances.sort_values(ascending=False).head(15).plot(kind="barh")
    plt.gca().invert_yaxis()
    plt.title("Top 15 important features for band gap prediction")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

# %% [markdown]
# ## 练习方向（跑通之后可以试试）
# - 换预测目标：formation_energy_per_atom（形成能）
# - 换模型：试试 XGBoost / GradientBoosting，看 MAE 有没有改善
# - 加限制条件：只挑半导体材料（0 < band_gap < 4），看模型在这个子集上表现如何
#   —— 这一步是为项目 4（半导体带隙 + 主动学习）做铺垫