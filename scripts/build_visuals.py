#!/usr/bin/env python3
"""Build deterministic repository graphics from the approved mascot asset."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = 1600, 900


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/System/Library/Fonts/Helvetica.ttc"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size=size)


def build_hero() -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), "#162033")
    draw = ImageDraw.Draw(image)
    for y in range(HEIGHT):
        mix = y / HEIGHT
        color = tuple(round(a * (1 - mix) + b * mix) for a, b in zip((22, 32, 51), (35, 46, 67)))
        draw.line((0, y, WIDTH, y), fill=color)

    draw.rounded_rectangle((85, 82, 360, 132), radius=25, fill="#29364C")
    draw.text((112, 93), "OPEN-SOURCE AGENT SKILL", font=font(22, True), fill="#FFB423")
    draw.text((85, 205), "Grounded", font=font(92, True), fill="white")
    draw.text((85, 310), "AI Mentor", font=font(92, True), fill="white")
    draw.text((92, 450), "Learn computing and AI through the", font=font(34), fill="#DDE5F0")
    draw.text((92, 498), "real project in front of you.", font=font(34), fill="#DDE5F0")

    pills = ["Project-grounded", "Evidence-aware", "Privacy-first"]
    left = 88
    for label in pills:
        bounds = draw.textbbox((0, 0), label, font=font(23, True))
        pill_width = bounds[2] - bounds[0] + 44
        draw.rounded_rectangle((left, 620, left + pill_width, 674), radius=27, fill="#FFF3E8")
        draw.text((left + 22, 632), label, font=font(23, True), fill="#B83B1D")
        left += pill_width + 16

    draw.text((90, 795), "Built by Weike Zhang", font=font(24), fill="#9EABBC")
    mascot = Image.open(ROOT / "assets" / "mascot-transparent.png").convert("RGBA")
    mascot.thumbnail((680, 680), Image.Resampling.LANCZOS)
    image.paste(mascot, (890, 125), mascot)
    image.save(ROOT / "assets" / "hero.png", optimize=True)


if __name__ == "__main__":
    build_hero()
    print(ROOT / "assets" / "hero.png")
