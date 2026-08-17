"""核对 Fig 2 里每个结构的立体化学。

糖类把 β 画成 α、或者把 (R)-3HB 画成 (S)，是最容易被评卷人一眼抓住的错误。
所以这里不靠肉眼，分三步机器核对：

1. **单体构型**：用 RDKit 的 CIP 标定器标出手性中心，与文献构型逐一比对。
2. **重复单元回溯**：把重复单元的链接点还原成端基（C1 接回 OH、C4 的氧接回 H），
   得到的分子应当与第 1 步核对过的单体**规范 SMILES 完全相同**。
   这一步能抓住任何在改写成聚合物时手滑翻掉的构型。
3. **链中手性碳**：PHB / PLLA 的手性碳不与哑原子相邻，CIP 规则完全适用，直接断言 (R) / (S)。
   糖类的端基碳与哑原子相邻，CIP 优先级失去意义，因此不在这一步断言，由第 2 步保证。

跑法：python3 verify_stereochemistry.py（Fig 2 生成前会自动调用）
"""

from rdkit import Chem
from rdkit.Chem import rdCIPLabeler

BETA_D_GLUCOSE = "OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
ALPHA_D_GLUCOSE = "OC[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
# 2-氨基-2-脱氧-β-D-葡萄糖：由已核对的 β-D-葡萄糖把 C2 的 OH 换成 NH2 得到
BETA_D_GLUCOSAMINE = "OC[C@H]1O[C@@H](O)[C@H](N)[C@@H](O)[C@@H]1O"

# (名称, SMILES, 文献构型, {原子索引: 期望 CIP})
MONOMERS = [
    ("beta-D-glucopyranose", BETA_D_GLUCOSE,
     "(2R,3R,4S,5S,6R)-6-(hydroxymethyl)oxane-2,3,4,5-tetrol",
     {4: "R", 6: "R", 8: "S", 10: "S", 2: "R"}),
    ("alpha-D-glucopyranose", ALPHA_D_GLUCOSE,
     "(2S,3R,4S,5S,6R)-6-(hydroxymethyl)oxane-2,3,4,5-tetrol",
     {4: "S", 6: "R", 8: "S", 10: "S", 2: "R"}),
    ("(R)-3-hydroxybutanoic acid", "C[C@@H](O)CC(=O)O",
     "PHB 的单体；细菌合成只给 (R) 一个对映体", {1: "R"}),
    ("(S)-lactic acid", "C[C@H](O)C(=O)O",
     "PLLA 的单体；L-乳酸即 (S)", {1: "S"}),
]

# Fig 2 实际绘制的重复单元
# (名称, SMILES, 回溯目标单体或 None, 链中手性碳期望 CIP 或 None)
REPEAT_UNITS = [
    ("Cellulose — beta(1->4)-D-glucan",
     "OC[C@H]1O[C@@H](*)[C@H](O)[C@@H](O)[C@@H]1O*", BETA_D_GLUCOSE, None),
    ("Amylose (starch) — alpha(1->4)-D-glucan",
     "OC[C@H]1O[C@H](*)[C@H](O)[C@@H](O)[C@@H]1O*", ALPHA_D_GLUCOSE, None),
    ("Chitosan — beta(1->4)-2-amino-2-deoxy-D-glucan",
     "OC[C@H]1O[C@@H](*)[C@H](N)[C@@H](O)[C@@H]1O*", BETA_D_GLUCOSAMINE, None),
    ("PHB — poly[(R)-3-hydroxybutyrate]",
     "*O[C@H](C)CC(=O)*", None, "R"),
    ("PLLA — poly[(S)-lactic acid]",
     "*O[C@@H](C)C(=O)*", None, "S"),
]


def cip_labels(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"SMILES 解析失败: {smiles}")
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
    rdCIPLabeler.AssignCIPLabels(mol)
    return mol, {a.GetIdx(): a.GetProp("_CIPCode")
                 for a in mol.GetAtoms() if a.HasProp("_CIPCode")}


def uncap(smiles):
    """把重复单元的链接点还原成端基：碳上的哑原子 → OH，氧上的哑原子 → H。

    只改变取代基的种类，不触碰任何 @/@@，所以还原后的分子与重复单元
    在手性中心上是同一个空间排布。
    """
    mol = Chem.RWMol(Chem.MolFromSmiles(smiles))
    to_remove = []
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() != 0:
            continue
        (neighbour,) = atom.GetNeighbors()
        if neighbour.GetAtomicNum() == 8:
            to_remove.append(atom.GetIdx())      # 糖苷氧上的链接点 → 变回 OH 的 H
        else:
            atom.SetAtomicNum(8)                 # 端基碳上的链接点 → 变回 OH
    for idx in sorted(to_remove, reverse=True):
        mol.RemoveAtom(idx)
    out = mol.GetMol()
    Chem.SanitizeMol(out)
    return Chem.MolToSmiles(out)


def main():
    failures = []

    print("=" * 78)
    print("第 1 步 · 单体构型与文献比对")
    print("=" * 78)
    for name, smiles, reference, expected in MONOMERS:
        _, labels = cip_labels(smiles)
        ok = all(labels.get(idx) == want for idx, want in expected.items())
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"       参考   : {reference}")
        print(f"       实测CIP: {dict(sorted(labels.items()))}")
        if not ok:
            failures.append(f"{name} (单体构型)")
            print(f"       期望   : {expected}")

    print()
    print("=" * 78)
    print("第 2 步 · 重复单元回溯到单体  /  第 3 步 · 链中手性碳")
    print("=" * 78)
    for name, smiles, target, expected_cip in REPEAT_UNITS:
        print(f"  {name}")
        print(f"       SMILES : {smiles}")
        if target is not None:
            got = uncap(smiles)
            want = Chem.CanonSmiles(target)
            ok = got == want
            print(f"       回溯   : [{'PASS' if ok else 'FAIL'}] {got}")
            if not ok:
                failures.append(f"{name} (回溯不符)")
                print(f"       期望   : {want}")
        if expected_cip is not None:
            _, labels = cip_labels(smiles)
            got_cip = set(labels.values())
            ok = got_cip == {expected_cip}
            print(f"       链手性 : [{'PASS' if ok else 'FAIL'}] "
                  f"{dict(sorted(labels.items()))}，期望 ({expected_cip})")
            if not ok:
                failures.append(f"{name} (链中手性碳)")

    print()
    if failures:
        raise SystemExit("立体化学核对未通过：\n  - " + "\n  - ".join(failures))
    print("全部通过：单体构型与文献一致，重复单元未在改写中翻转构型。")


if __name__ == "__main__":
    main()
