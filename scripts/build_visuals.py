#!/usr/bin/env python3
"""Build deterministic public graphics from the approved mascot asset."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
NAVY = "#162033"
NAVY_LIGHT = "#29364C"
ORANGE = "#F24B22"
GOLD = "#FFB423"
CREAM = "#FFF3E8"
MUTED = "#DDE5F0"


def font(size: int, bold: bool = False, cjk: bool = False) -> ImageFont.FreeTypeFont:
    candidates = []
    if cjk:
        candidates.extend(
            [
                Path("/System/Library/Fonts/Hiragino Sans GB.ttc"),
                Path("/System/Library/Fonts/STHeiti Medium.ttc"),
                Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
            ]
        )
    candidates.extend(
        [
            Path(
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
                if bold
                else "/System/Library/Fonts/Supplemental/Arial.ttf"
            ),
            Path("/System/Library/Fonts/Helvetica.ttc"),
            Path("/System/Library/Fonts/PingFang.ttc"),
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size=size)


def gradient(width: int, height: int) -> Image.Image:
    image = Image.new("RGB", (width, height), NAVY)
    draw = ImageDraw.Draw(image)
    start = (22, 32, 51)
    end = (43, 54, 76)
    for y in range(height):
        mix = y / height
        color = tuple(round(a * (1 - mix) + b * mix) for a, b in zip(start, end))
        draw.line((0, y, width, y), fill=color)
    return image


def mascot(max_size: tuple[int, int]) -> Image.Image:
    image = Image.open(ROOT / "assets" / "mascot-transparent.png").convert("RGBA")
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    return image


def build_social_preview() -> None:
    width, height = 1280, 640
    image = gradient(width, height)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((68, 58, 324, 108), radius=25, fill=NAVY_LIGHT)
    draw.text((94, 70), "OPEN AGENT SKILL", font=font(22, True), fill=GOLD)
    draw.text((68, 158), "Grounded", font=font(76, True), fill="white")
    draw.text((68, 242), "AI Tutor", font=font(76, True), fill="white")
    draw.multiline_text(
        (74, 354),
        "Starts with what you know.\nExplains the step you are missing.",
        font=font(31),
        fill=MUTED,
        spacing=10,
    )
    draw.rounded_rectangle((72, 510, 666, 566), radius=28, fill=CREAM)
    draw.text(
        (96, 525),
        "No technical background required.",
        font=font(21, True),
        fill="#B83B1D",
    )
    character = mascot((500, 500))
    character_position = (width - character.width - 48, 82)
    glow = Image.new("RGBA", character.size, (242, 75, 34, 0))
    glow.putalpha(character.getchannel("A").filter(ImageFilter.GaussianBlur(14)))
    image.paste(glow, character_position, glow)
    image.paste(character, character_position, character)
    image.save(ROOT / "assets" / "social-preview.png", optimize=True)


def comparison_card(
    destination: Path,
    *,
    title: str,
    subtitle: str,
    left_label: str,
    right_label: str,
    left_text: str,
    right_text: str,
    cjk: bool = False,
) -> None:
    width, height = 1200, 675
    image = Image.new("RGB", (width, height), "#F7F9FC")
    draw = ImageDraw.Draw(image)
    draw.text((60, 42), title, font=font(38, True, cjk), fill=NAVY)
    draw.text(
        (60, 92),
        subtitle,
        font=font(21, cjk=cjk),
        fill="#516070",
    )

    cards = [
        (50, 150, 570, 620, left_label, left_text, "#FFFFFF", "#D8DEE9"),
        (630, 150, 1150, 620, right_label, right_text, CREAM, ORANGE),
    ]
    for left, top, right, bottom, label, body, fill, outline in cards:
        draw.rounded_rectangle(
            (left, top, right, bottom), radius=28, fill=fill, outline=outline, width=3
        )
        draw.text((left + 36, top + 34), label, font=font(31, True, cjk), fill=NAVY)
        draw.multiline_text(
            (left + 36, top + 100),
            body,
            font=font(25, cjk=cjk),
            fill="#344054",
            spacing=24,
        )
    image.save(destination, optimize=True)


def build_comparisons() -> None:
    comparison_card(
        ROOT / "assets" / "before-after.png",
        title="The same port question, with the missing step added",
        subtitle="The first answer was correct. The Tutor adds the missing idea and a check.",
        left_label="Regular answer",
        right_label="With Grounded AI Tutor",
        left_text=(
            "• Explains ports directly\n"
            "• Gives a safe read-only command\n"
            "• Asks the learner to inspect output"
        ),
        right_text=(
            "• Explains why programs need ports\n"
            "• Shows where incoming data goes\n"
            "• Asks you to predict, then find it"
        ),
    )
    comparison_card(
        ROOT / "assets" / "before-after.zh-CN.png",
        title="同一个“端口”问题，学习过程有什么不同",
        subtitle="基线回答已经准确；这里展示 Skill 增加的学习步骤",
        left_label="普通回答",
        right_label="启用 Tutor Skill",
        left_text="• 直接解释端口\n• 给出安全的只读命令\n• 请用户观察结果",
        right_text=(
            "• 先补“正在运行的程序”\n"
            "• 先画出数据到程序的路径\n"
            "• 观察前预测，观察后定位"
        ),
        cjk=True,
    )


if __name__ == "__main__":
    build_social_preview()
    build_comparisons()
    for name in ("social-preview.png", "before-after.png", "before-after.zh-CN.png"):
        print(ROOT / "assets" / name)
