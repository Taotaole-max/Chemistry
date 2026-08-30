from rdkit import Chem
from rdkit.Chem import rdCIPLabeler

BETA_D_GLUCOSE = "OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
ALPHA_D_GLUCOSE = "OC[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
BETA_D_GLUCOSAMINE = "OC[C@H]1O[C@@H](O)[C@H](N)[C@@H](O)[C@@H]1O"

MONOMERS = [
    ("beta-D-glucopyranose", BETA_D_GLUCOSE,
     "(2R,3R,4S,5S,6R)-6-(hydroxymethyl)oxane-2,3,4,5-tetrol",
     {4: "R", 6: "R", 8: "S", 10: "S", 2: "R"}),
    ("alpha-D-glucopyranose", ALPHA_D_GLUCOSE,
     "(2S,3R,4S,5S,6R)-6-(hydroxymethyl)oxane-2,3,4,5-tetrol",
     {4: "S", 6: "R", 8: "S", 10: "S", 2: "R"}),
    ("(R)-3-hydroxybutanoic acid", "C[C@@H](O)CC(=O)O",
     "PHB monomer; bacterial synthesis gives only the (R) enantiomer", {1: "R"}),
    ("(S)-lactic acid", "C[C@H](O)C(=O)O",
     "PLLA monomer; L-lactic acid is (S)", {1: "S"}),
]

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
        raise ValueError(f"SMILES failed to parse: {smiles}")
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
    rdCIPLabeler.AssignCIPLabels(mol)
    return mol, {a.GetIdx(): a.GetProp("_CIPCode")
                 for a in mol.GetAtoms() if a.HasProp("_CIPCode")}

def uncap(smiles):
    mol = Chem.RWMol(Chem.MolFromSmiles(smiles))
    to_remove = []
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() != 0:
            continue
        (neighbour,) = atom.GetNeighbors()
        if neighbour.GetAtomicNum() == 8:
            to_remove.append(atom.GetIdx())
        else:
            atom.SetAtomicNum(8)
    for idx in sorted(to_remove, reverse=True):
        mol.RemoveAtom(idx)
    out = mol.GetMol()
    Chem.SanitizeMol(out)
    return Chem.MolToSmiles(out)

def main():
    failures = []

    print("=" * 78)
    print("Step 1 - monomer configuration vs literature")
    print("=" * 78)
    for name, smiles, reference, expected in MONOMERS:
        _, labels = cip_labels(smiles)
        ok = all(labels.get(idx) == want for idx, want in expected.items())
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"       reference    : {reference}")
        print(f"       measured CIP : {dict(sorted(labels.items()))}")
        if not ok:
            failures.append(f"{name} (monomer configuration)")
            print(f"       expected     : {expected}")

    print()
    print("=" * 78)
    print("Step 2 - repeat unit traced back to monomer  /  Step 3 - chain stereocentres")
    print("=" * 78)
    for name, smiles, target, expected_cip in REPEAT_UNITS:
        print(f"  {name}")
        print(f"       SMILES : {smiles}")
        if target is not None:
            got = uncap(smiles)
            want = Chem.CanonSmiles(target)
            ok = got == want
            print(f"       trace-back   : [{'PASS' if ok else 'FAIL'}] {got}")
            if not ok:
                failures.append(f"{name} (trace-back mismatch)")
                print(f"       expected     : {want}")
        if expected_cip is not None:
            _, labels = cip_labels(smiles)
            got_cip = set(labels.values())
            ok = got_cip == {expected_cip}
            print(f"       chain stereo : [{'PASS' if ok else 'FAIL'}] "
                  f"{dict(sorted(labels.items()))}, expected ({expected_cip})")
            if not ok:
                failures.append(f"{name} (chain stereocentre)")

    print()
    if failures:
        raise SystemExit("stereochemistry check failed:\n  - " + "\n  - ".join(failures))
    print("all passed: monomer configurations match the literature and no repeat "
          "unit was inverted during editing.")

if __name__ == "__main__":
    main()
