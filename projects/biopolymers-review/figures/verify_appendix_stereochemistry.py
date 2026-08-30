from rdkit import Chem
from rdkit.Chem import rdCIPLabeler

import verify_stereochemistry as _base

BETA_D_GLUCOSE = "OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"

BETA_D_GLUCURONIC = "OC(=O)[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
BETA_D_MANNURONIC = "OC(=O)[C@H]1O[C@@H](O)[C@@H](O)[C@@H](O)[C@@H]1O"
GULURONIC_CANDIDATE = "OC(=O)[C@@H]1O[C@@H](O)[C@@H](O)[C@@H](O)[C@@H]1O"

M_REPEAT = "OC(=O)[C@H]1O[C@@H](*)[C@@H](O)[C@@H](O)[C@@H]1O*"
G_REPEAT = "OC(=O)[C@@H]1O[C@@H](*)[C@@H](O)[C@@H](O)[C@@H]1O*"

NR_CIS_ISOPRENE = r"*C/C(C)=C\C*"

FREE_L_PROLINE = "OC(=O)[C@@H]1CCCN1"
FREE_TRANS_HYP = "OC(=O)[C@@H]1C[C@@H](O)CN1"
SILK_GLY_ALA_REPEAT = "*NCC(=O)N[C@@H](C)C(=O)*"
COLLAGEN_GLY_PRO_HYP_REPEAT = (
    "*NCC(=O)N1[C@H](C(=O)N2[C@H](C(=O)*)C[C@@H](O)C2)CCC1"
)

def cip_labels(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"SMILES failed to parse: {smiles}")
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
    rdCIPLabeler.AssignCIPLabels(mol)
    return mol, {a.GetIdx(): a.GetProp("_CIPCode")
                 for a in mol.GetAtoms() if a.HasProp("_CIPCode")}

def bond_stereo(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"SMILES failed to parse: {smiles}")
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
    rdCIPLabeler.AssignCIPLabels(mol)
    return {(b.GetBeginAtomIdx(), b.GetEndAtomIdx()): str(b.GetStereo())
            for b in mol.GetBonds() if b.GetStereo() != Chem.BondStereo.STEREONONE}

def epimer_diff(smiles_a, smiles_b):
    _, a = cip_labels(smiles_a)
    _, b = cip_labels(smiles_b)
    return {idx for idx in a if a.get(idx) != b.get(idx)}

def main():
    failures = []
    warnings = []

    print("=" * 78)
    print("Step 1 - alginate M/G epimerisation chain (one stereocentre flipped per step)")
    print("=" * 78)

    mol_glc, cip_glc = cip_labels(BETA_D_GLUCOSE)
    mol_glcA, cip_glcA = cip_labels(BETA_D_GLUCURONIC)
    print(f"  D-glucose CIP        : {cip_glc}")
    print(f"  D-glucuronic acid CIP: {cip_glcA}  (C6 oxidised; labels may shift with "
          f"substituent priority, which does not change the spatial configuration)")

    diff_glcA_to_manA = epimer_diff(BETA_D_GLUCURONIC, BETA_D_MANNURONIC)
    print(f"  glucuronic -> mannuronic: stereocentres flipped = {diff_glcA_to_manA} "
          f"(expect exactly 1, at C2)")
    if len(diff_glcA_to_manA) != 1:
        failures.append(f"glucuronic->mannuronic flipped {len(diff_glcA_to_manA)} centres, expected 1")

    diff_manA_to_gulA = epimer_diff(BETA_D_MANNURONIC, GULURONIC_CANDIDATE)
    print(f"  mannuronic -> guluronic candidate: stereocentres flipped = {diff_manA_to_gulA} "
          f"(expect exactly 1, at C5)")
    if len(diff_manA_to_gulA) != 1:
        failures.append(f"mannuronic->guluronic flipped {len(diff_manA_to_gulA)} centres, expected 1")

    warnings.append(
        "The absolute configuration of alginate G (guluronic acid) is only checked "
        "as 'the C5 epimer of M'; there is no independent literature CIP string to "
        "compare against, unlike the other structures here. Re-check with ChemDraw "
        "or a literature structure before submission."
    )

    got_M = _base.uncap(M_REPEAT)
    want_M = Chem.CanonSmiles(BETA_D_MANNURONIC)
    ok_M = got_M == want_M
    print(f"  M repeat unit trace-back: [{'PASS' if ok_M else 'FAIL'}] {got_M}")
    if not ok_M:
        failures.append(f"M repeat unit trace-back mismatch, expected {want_M}")

    got_G = _base.uncap(G_REPEAT)
    want_G = Chem.CanonSmiles(GULURONIC_CANDIDATE)
    ok_G = got_G == want_G
    print(f"  G repeat unit trace-back: [{'PASS' if ok_G else 'FAIL'}] {got_G}")
    if not ok_G:
        failures.append(f"G repeat unit trace-back mismatch, expected {want_G}")

    print()
    print("=" * 78)
    print("Step 2 - natural rubber cis-1,4-polyisoprene: main-chain cis geometry")
    print("=" * 78)
    stereo = bond_stereo(NR_CIS_ISOPRENE)
    print(f"  bond geometry: {stereo}")
    is_cis = any(v == "STEREOCIS" for v in stereo.values())
    print(f"  [{'PASS' if is_cis else 'FAIL'}] chain-continuing atoms are cis "
          f"(natural rubber = cis; gutta-percha = trans)")
    if not is_cis:
        failures.append("natural rubber repeat unit not identified as cis")

    print()
    print("=" * 78)
    print("Step 3 - amino-acid backbone stereocentres (final SMILES after @/@@ calibration)")
    print("=" * 78)

    _, cip_pro_free = cip_labels(FREE_L_PROLINE)
    print(f"  free L-proline CIP: {cip_pro_free}  expected (S)")
    if set(cip_pro_free.values()) != {"S"}:
        failures.append("free L-proline configuration does not match literature (S)")

    _, cip_hyp_free = cip_labels(FREE_TRANS_HYP)
    print(f"  free trans-4-hydroxy-L-proline CIP: {cip_hyp_free}  expected {{alpha:S, gamma:R}}")
    if sorted(cip_hyp_free.values()) != sorted(["S", "R"]):
        failures.append("free trans-4-hydroxy-L-proline does not match literature (2S,4R)")

    _, cip_silk = cip_labels(SILK_GLY_ALA_REPEAT)
    print(f"  silk fibroin Gly-Ala repeat unit CIP: {cip_silk}  expected {{Ala-alpha: S}}")
    if set(cip_silk.values()) != {"S"}:
        failures.append("silk fibroin Gly-Ala repeat: Ala stereocentre does not match L-Ala (S)")

    mol_col, cip_col = cip_labels(COLLAGEN_GLY_PRO_HYP_REPEAT)
    print(f"  collagen Gly-Pro-Hyp repeat unit CIP: {cip_col}  "
          f"expected the three ring stereocentres to be {{S, S, R}} (Pro-alpha=S, Hyp-alpha=S, Hyp-gamma=R)")
    if sorted(cip_col.values()) != sorted(["S", "S", "R"]):
        failures.append("collagen Gly-Pro-Hyp repeat: ring stereocentres do not match (2S,4R)-Hyp")

    print()
    if failures:
        raise SystemExit("appendix stereochemistry check failed:\n  - " + "\n  - ".join(failures))
    print("all passed (epimer relationships, cis geometry and amino-acid backbone all as expected).")
    if warnings:
        print()
        print("notes (not failures, but read before generating figures):")
        for w in warnings:
            print("  * " + w)

if __name__ == "__main__":
    main()
