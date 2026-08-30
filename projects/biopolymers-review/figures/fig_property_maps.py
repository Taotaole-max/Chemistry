from pathlib import Path

import matplotlib.pyplot as plt

import fig4_thermal_windows as thermal
import fig5_property_map as mech
from style import FIG_W, FS_PANEL_TITLE, INK, apply_style, save

OUT = Path(__file__).parent / "output"

def main():
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W, 74 / 25.4))
    fig.subplots_adjust(left=0.15, right=0.99, top=0.90, bottom=0.155, wspace=0.14)

    thermal.draw(axes[0])
    axes[0].set_title("(a) Thermal transitions and melt windows",
                      fontsize=FS_PANEL_TITLE, fontweight="bold", color=INK,
                      loc="left", pad=4)

    mech.draw(axes[1])
    axes[1].set_title("(b) Modulus vs. elongation at break",
                      fontsize=FS_PANEL_TITLE, fontweight="bold", color=INK,
                      loc="left", pad=4)

    save(fig, "fig_property_maps", OUT)

if __name__ == "__main__":
    main()
