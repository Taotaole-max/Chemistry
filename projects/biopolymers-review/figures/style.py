import io

import matplotlib as mpl
import matplotlib.pyplot as plt

MM = 1 / 25.4

FIG_W_MM = 170.0
FIG_W = FIG_W_MM * MM

H_S = 34.0
H_M = 52.0
H_L = 64.0

FS_PANEL_TITLE = 8.0
FS_PANEL_SUB = 6.3
FS_ANNOT = 6.5
FS_TAG = 6.0

C_POLYSACCHARIDE = "#2a78d6"
C_POLYESTER = "#eb6834"
C_PROTEIN = "#1baf7a"
C_PETRO = "#4a3aa7"
C_OTHER = "#8a8a85"

CLASS_COLOR = {
    "polysaccharide": C_POLYSACCHARIDE,
    "polyester": C_POLYESTER,
    "protein": C_PROTEIN,
    "petro": C_PETRO,
    "other": C_OTHER,
}

INK = "#1a1a19"
INK_SECONDARY = "#52514e"
INK_MUTED = "#8a8a85"
SURFACE = "#ffffff"

FONT_STACK = ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"]

def apply_style():
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": FONT_STACK,
        "font.size": 8,
        "axes.labelsize": 8,
        "axes.titlesize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": INK_SECONDARY,
        "xtick.color": INK_SECONDARY,
        "ytick.color": INK_SECONDARY,
        "axes.linewidth": 0.6,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "lines.linewidth": 1.4,
        "grid.color": "#e2e2de",
        "grid.linewidth": 0.5,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
    })

def new_fig(height_mm, nrows=1, ncols=1, constrained=True, **subplot_kw):
    apply_style()
    layout = "constrained" if constrained else None
    fig, axes = plt.subplots(nrows, ncols, figsize=(FIG_W, height_mm * MM),
                             layout=layout, **subplot_kw)
    return fig, axes

_MOL_PX_W = 760
_MOL_PX_H = 520
_MOL_BOND_WIDTH = 3
_MOL_FONT = 38

def _trim_white(arr, pad_px=8):
    import numpy as np
    mask = np.any(arr[..., :3] < 0.97, axis=-1)
    if not mask.any():
        return arr
    rows, cols = np.any(mask, axis=1), np.any(mask, axis=0)
    r0, r1 = np.where(rows)[0][[0, -1]]
    c0, c1 = np.where(cols)[0][[0, -1]]
    r0, c0 = max(0, r0 - pad_px), max(0, c0 - pad_px)
    r1, c1 = min(arr.shape[0] - 1, r1 + pad_px), min(arr.shape[1] - 1, c1 + pad_px)
    return arr[r0:r1 + 1, c0:c1 + 1]

def draw_mol(smiles, annotate_cip=False, px_w=_MOL_PX_W, px_h=_MOL_PX_H, trim=True):
    from rdkit import Chem
    from rdkit.Chem import rdDepictor
    from rdkit.Chem.Draw import rdMolDraw2D
    import matplotlib.image as mpimg

    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DCairo(px_w, px_h)
    opts = drawer.drawOptions()
    opts.dummiesAreAttachments = True
    opts.addStereoAnnotation = annotate_cip
    opts.bondLineWidth = _MOL_BOND_WIDTH
    opts.fixedFontSize = _MOL_FONT
    opts.padding = 0.06
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    arr = mpimg.imread(io.BytesIO(drawer.GetDrawingText()), format="png")
    return _trim_white(arr) if trim else arr

def panel_title(ax, tag, name, colour, sub=None):
    label = f"({tag}) {name}"
    if sub:
        label += f"\n{sub}"
    ax.set_title(label, fontsize=FS_PANEL_TITLE, fontweight="bold",
                 color=colour, loc="left", pad=3.0, linespacing=1.3)
    ax.set_anchor("N")

def save(fig, stem, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / f"{stem}.svg", bbox_inches=None, pad_inches=0.0)
    fig.savefig(outdir / f"{stem}.png", dpi=600, bbox_inches=None, pad_inches=0.0)
    plt.close(fig)
    print(f"  wrote {stem}.svg + {stem}.png")
