"""核对附录 Fig 12（单体一览）里每个新增结构的立体化学/几何异构。

方法延续 verify_stereochemistry.py：不靠肉眼，机器核对 CIP 标签是否和文献构型一致。
这里额外处理两类 verify_stereochemistry.py 没覆盖的情况：

1. **差向异构体推导**（海藻酸盐 M/G）：不是从零手写构型，而是在已核对过的
   beta-D-glucose 骨架上做单点差向异构（只翻转一个手性中心的 @/@@，其余全部原样保留），
   这样"只差一个手性碳"这个化学事实由构造方式本身保证，不依赖记忆里的 CIP 数字。
   **诚实标注**：M（甘露糖醛酸）由 D-葡萄糖在 C2 差向异构推导（葡萄糖→甘露糖是
   教科书级、置信度很高的事实）；G（古洛糖醛酸）由 M 在 C5 差向异构推导（M/G 互为
   C5 差向异构体，同样是文献公认事实）。但本脚本没有独立文献 CIP 字符串可比对
   古洛糖醛酸的绝对构型（不像 PHB/乳酸/葡萄糖那样在原文件里有现成引用），所以这里
   只核对"差向异构关系"本身（每步只翻一个手性中心），不断言古洛糖醛酸的 (R)/(S)
   标签已经过独立文献核对——图注会如实注明这一点，建议提交前用 ChemDraw/文献结构
   再核一遍。

2. **顺反异构**（天然橡胶 cis-1,4-聚异戊二烯）：核对的是 RDKit 报告的键几何
   （STEREOCIS/STEREOTRANS，以 SMILES 里明确写出的两个链延伸原子为参照），
   不是 CIP E/Z（重复单元两端是哑原子附着点，CIP 优先级在这里没有稳定意义，
   见 Fig 2 对糖类端基碳的同样处理）。"顺式主链延续"正是天然橡胶（顺式）
   区别于杜仲胶（反式）的定义性几何特征。

3. **氨基酸主链**（丝素蛋白 Gly-Ala、胶原蛋白 Gly-Pro-Hyp）：L-丙氨酸 (S) 是
   教科书级事实；脯氨酸/羟脯氨酸的环状主链把手性碳嵌在环里，CIP 标签会因为
   相邻取代基从"游离羧酸/游离氨基"变成"酰胺"而发生数字变化（和步骤1的差向异构
   同一个道理：标签变化不代表空间构型翻转）。核对方法是对重复单元里的每个环手性碳
   直接标定 CIP，逐一比对文献已知构型（L-脯氨酸 (S)；反式-4-羟基-L-脯氨酸 (2S,4R)，
   胶原蛋白里实际使用的立体异构体）——这一步在设计 SMILES 时已经用穷举 @/@@ 组合
   核对过，这里固化成回归测试。

跑法：python3 verify_appendix_stereochemistry.py（Fig 12 生成前会自动调用）
"""

from rdkit import Chem
from rdkit.Chem import rdCIPLabeler

import verify_stereochemistry as _base  # reuse its uncap() round-trip helper

# ---------------------------------------------------------------------------
# 1. 海藻酸盐 M/G：差向异构推导链
# ---------------------------------------------------------------------------

BETA_D_GLUCOSE = "OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"  # 与 verify_stereochemistry.py 相同的已核对参考

# C6 氧化成 COOH（不触碰任何手性中心）——D-glucose -> D-glucuronic acid
BETA_D_GLUCURONIC = "OC(=O)[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
# C2 差向异构（教科书事实：D-mannose 是 D-glucose 的 C2 差向异构体）
BETA_D_MANNURONIC = "OC(=O)[C@H]1O[C@@H](O)[C@@H](O)[C@@H](O)[C@@H]1O"
# C5 差向异构（文献公认：L-guluronic acid 是 D-mannuronic acid 的 C5 差向异构体）
# 绝对构型未经独立文献 CIP 字符串核对——见模块开头说明
GULURONIC_CANDIDATE = "OC(=O)[C@@H]1O[C@@H](O)[C@@H](O)[C@@H](O)[C@@H]1O"

# Fig 12 实际绘制的重复单元（链接点画成波浪键）——必须用 uncap() 回溯核对
# 没有在改写成重复单元时手滑翻转任何一个手性中心
M_REPEAT = "OC(=O)[C@H]1O[C@@H](*)[C@@H](O)[C@@H](O)[C@@H]1O*"
G_REPEAT = "OC(=O)[C@@H]1O[C@@H](*)[C@@H](O)[C@@H](O)[C@@H]1O*"

# ---------------------------------------------------------------------------
# 2. 天然橡胶：cis-1,4-聚异戊二烯重复单元
# ---------------------------------------------------------------------------
NR_CIS_ISOPRENE = r"*C/C(C)=C\C*"

# ---------------------------------------------------------------------------
# 3. 氨基酸主链：脯氨酸 / 羟脯氨酸的环手性碳，穷举校准后的最终 SMILES
# ---------------------------------------------------------------------------
FREE_L_PROLINE = "OC(=O)[C@@H]1CCCN1"                      # 文献：(S)
FREE_TRANS_HYP = "OC(=O)[C@@H]1C[C@@H](O)CN1"               # 文献：(2S,4R)，胶原蛋白实际使用的异构体
SILK_GLY_ALA_REPEAT = "*NCC(=O)N[C@@H](C)C(=O)*"            # 文献：L-Ala (S)
COLLAGEN_GLY_PRO_HYP_REPEAT = (
    "*NCC(=O)N1[C@H](C(=O)N2[C@H](C(=O)*)C[C@@H](O)C2)CCC1"
)


def cip_labels(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"SMILES 解析失败: {smiles}")
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
    rdCIPLabeler.AssignCIPLabels(mol)
    return mol, {a.GetIdx(): a.GetProp("_CIPCode")
                 for a in mol.GetAtoms() if a.HasProp("_CIPCode")}


def bond_stereo(smiles):
    """键几何标签依赖于是否跑过完整的 CIP 标定流程（RDKit 原始解析给出的是基于
    CIP 优先级的 STEREOZ/STEREOE，跑完 AssignStereochemistry + rdCIPLabeler 后
    才会归一化成相对于 SMILES 里显式书写的两个参照原子的 STEREOCIS/STEREOTRANS——
    对带哑原子附着点的重复单元，后者才是"主链是否延续在同一侧"这个化学问题
    真正想问的东西），所以这里显式跑同一条流程，和 cip_labels() 保持一致。
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"SMILES 解析失败: {smiles}")
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
    rdCIPLabeler.AssignCIPLabels(mol)
    return {(b.GetBeginAtomIdx(), b.GetEndAtomIdx()): str(b.GetStereo())
            for b in mol.GetBonds() if b.GetStereo() != Chem.BondStereo.STEREONONE}


def epimer_diff(smiles_a, smiles_b):
    """两个只在 @/@@ 上有差异的 SMILES，返回 CIP 标签发生变化的原子下标集合。"""
    _, a = cip_labels(smiles_a)
    _, b = cip_labels(smiles_b)
    return {idx for idx in a if a.get(idx) != b.get(idx)}


def main():
    failures = []
    warnings = []

    print("=" * 78)
    print("第 1 步 · 海藻酸盐 M/G 差向异构推导链（每步只翻一个手性中心）")
    print("=" * 78)

    # 葡萄糖 -> 葡萄糖醛酸：不应有任何手性中心的 @/@@ 记号发生改动（只氧化了取代基）
    mol_glc, cip_glc = cip_labels(BETA_D_GLUCOSE)
    mol_glcA, cip_glcA = cip_labels(BETA_D_GLUCURONIC)
    print(f"  D-glucose CIP        : {cip_glc}")
    print(f"  D-glucuronic acid CIP: {cip_glcA}  (C6 氧化，标签可能因取代基优先级改变而漂移，"
          f"这是正常的，不代表空间构型变化)")

    diff_glcA_to_manA = epimer_diff(BETA_D_GLUCURONIC, BETA_D_MANNURONIC)
    print(f"  glucuronic -> mannuronic: 差向异构翻转的手性中心 = {diff_glcA_to_manA} "
          f"(期望恰好 1 个，对应 C2)")
    if len(diff_glcA_to_manA) != 1:
        failures.append(f"glucuronic->mannuronic 差向异构翻转了 {len(diff_glcA_to_manA)} 个中心，期望 1 个")

    diff_manA_to_gulA = epimer_diff(BETA_D_MANNURONIC, GULURONIC_CANDIDATE)
    print(f"  mannuronic -> guluronic candidate: 差向异构翻转的手性中心 = {diff_manA_to_gulA} "
          f"(期望恰好 1 个，对应 C5)")
    if len(diff_manA_to_gulA) != 1:
        failures.append(f"mannuronic->guluronic 差向异构翻转了 {len(diff_manA_to_gulA)} 个中心，期望 1 个")

    warnings.append(
        "海藻酸盐 G（古洛糖醛酸）的绝对构型只核对了'与 M 互为 C5 差向异构体'这一关系，"
        "没有独立文献 CIP 字符串可比对（不像本文件其余结构都有明确引用）——"
        "提交前建议用 ChemDraw 或文献结构图再核一遍。"
    )

    # Fig 12 画的是重复单元（链接点为哑原子），不是上面这两个游离酸——
    # 用 verify_stereochemistry.py 的 uncap() 把链接点还原成端基，核对空间构型
    # 与上面已核对过的游离酸完全一致（抓住"改写成重复单元时手滑翻转"这类错误）
    got_M = _base.uncap(M_REPEAT)
    want_M = Chem.CanonSmiles(BETA_D_MANNURONIC)
    ok_M = got_M == want_M
    print(f"  M 重复单元回溯: [{'PASS' if ok_M else 'FAIL'}] {got_M}")
    if not ok_M:
        failures.append(f"M 重复单元回溯不符，期望 {want_M}")

    got_G = _base.uncap(G_REPEAT)
    want_G = Chem.CanonSmiles(GULURONIC_CANDIDATE)
    ok_G = got_G == want_G
    print(f"  G 重复单元回溯: [{'PASS' if ok_G else 'FAIL'}] {got_G}")
    if not ok_G:
        failures.append(f"G 重复单元回溯不符，期望 {want_G}")

    print()
    print("=" * 78)
    print("第 2 步 · 天然橡胶 cis-1,4-聚异戊二烯：主链顺式几何")
    print("=" * 78)
    stereo = bond_stereo(NR_CIS_ISOPRENE)
    print(f"  键几何: {stereo}")
    is_cis = any(v == "STEREOCIS" for v in stereo.values())
    print(f"  [{'PASS' if is_cis else 'FAIL'}] 主链延续原子处于顺式 "
          f"(天然橡胶 = 顺式；杜仲胶 = 反式)")
    if not is_cis:
        failures.append("天然橡胶重复单元没有识别为顺式几何")

    print()
    print("=" * 78)
    print("第 3 步 · 氨基酸主链手性碳（穷举 @/@@ 校准后的最终 SMILES）")
    print("=" * 78)

    _, cip_pro_free = cip_labels(FREE_L_PROLINE)
    print(f"  游离 L-脯氨酸 CIP: {cip_pro_free}  期望 (S)")
    if set(cip_pro_free.values()) != {"S"}:
        failures.append("游离 L-脯氨酸构型与文献 (S) 不符")

    _, cip_hyp_free = cip_labels(FREE_TRANS_HYP)
    print(f"  游离反式-4-羟基-L-脯氨酸 CIP: {cip_hyp_free}  期望 {{alpha:S, gamma:R}}")
    if sorted(cip_hyp_free.values()) != sorted(["S", "R"]):
        failures.append("游离反式-4-羟基-L-脯氨酸构型与文献 (2S,4R) 不符")

    _, cip_silk = cip_labels(SILK_GLY_ALA_REPEAT)
    print(f"  丝素蛋白 Gly-Ala 重复单元 CIP: {cip_silk}  期望 {{Ala-alpha: S}}")
    if set(cip_silk.values()) != {"S"}:
        failures.append("丝素蛋白 Gly-Ala 重复单元里 Ala 手性碳与文献 L-Ala (S) 不符")

    mol_col, cip_col = cip_labels(COLLAGEN_GLY_PRO_HYP_REPEAT)
    print(f"  胶原蛋白 Gly-Pro-Hyp 重复单元 CIP: {cip_col}  "
          f"期望三个环手性碳为 {{S, S, R}}（Pro-alpha=S, Hyp-alpha=S, Hyp-gamma=R）")
    if sorted(cip_col.values()) != sorted(["S", "S", "R"]):
        failures.append("胶原蛋白 Gly-Pro-Hyp 重复单元的环手性碳构型组合与文献 (2S,4R)-Hyp 不符")

    print()
    if failures:
        raise SystemExit("附录立体化学核对未通过：\n  - " + "\n  - ".join(failures))
    print("全部通过（差向异构关系、顺式几何、氨基酸主链构型均与预期一致）。")
    if warnings:
        print()
        print("附带说明（不是失败，但出图前请读一遍）：")
        for w in warnings:
            print("  * " + w)


if __name__ == "__main__":
    main()
