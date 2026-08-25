"""把 fig4/fig5/fig6/fig8 横向拼成一张 1x4 草稿图，仅供预览排版，不是最终提交件。"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT = HERE / "output"

PANELS = [
    ("a", OUT / "fig4_thermal_windows.png", "Thermal"),
    ("b", OUT / "fig5_property_map.png", "Mechanical"),
    ("c", OUT / "fig6_degradation.png", "Degradation"),
    ("d", OUT / "fig8_nr_sbr_comparison.png", "Elasticity (NR vs SBR)"),
]

TARGET_H = 700
GAP = 25
LABEL_H = 45
BG = (255, 255, 255)


def load_font(size):
    for name in ("arial.ttf", "Arial.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    imgs = []
    for tag, path, caption in PANELS:
        im = Image.open(path).convert("RGB")
        w, h = im.size
        new_w = int(w * TARGET_H / h)
        im = im.resize((new_w, TARGET_H), Image.LANCZOS)
        imgs.append((tag, im, caption))

    total_w = sum(im.width for _, im, _ in imgs) + GAP * (len(imgs) - 1)
    canvas = Image.new("RGB", (total_w, TARGET_H + LABEL_H), BG)
    draw = ImageDraw.Draw(canvas)
    font_label = load_font(24)
    font_caption = load_font(16)

    x = 0
    for tag, im, caption in imgs:
        canvas.paste(im, (x, LABEL_H))
        draw.text((x, 8), f"({tag}) {caption}", fill=(26, 26, 25), font=font_label)
        x += im.width + GAP

    canvas.save(OUT / "combined_1x4.png")
    canvas.save(OUT / "combined_1x4.jpg", quality=92)
    print("wrote combined_1x4.png / .jpg", canvas.size)


if __name__ == "__main__":
    main()
