import importlib
import sys

MODULES = [
    "fig_repeat_units_all",
    "fig_higher_order_all",
    "fig9_dispersity",
    "fig_property_maps",
    "fig6_degradation",
    "fig8_nr_sbr_comparison",
]

def main():
    for name in MODULES:
        print(f"[{name}]")
        module = importlib.import_module(name)
        module.main()
    print("\ndone; output in output/")

if __name__ == "__main__":
    sys.exit(main())
