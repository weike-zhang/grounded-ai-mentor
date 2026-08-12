#!/usr/bin/env python3
"""Remove only edge-connected near-white background from the mascot artwork."""

from __future__ import annotations

import argparse
from collections import deque
from pathlib import Path

from PIL import Image


def is_background_candidate(pixel: tuple[int, int, int]) -> bool:
    red, green, blue = pixel
    return min(pixel) >= 210 and max(pixel) - min(pixel) <= 35


def matte_alpha(pixel: tuple[int, int, int]) -> int:
    red, green, blue = pixel
    brightness = (red + green + blue) / 3
    chroma = max(pixel) - min(pixel)
    darkness = max(0.0, min(1.0, (250.0 - brightness) / 35.0))
    color = max(0.0, min(1.0, chroma / 35.0))
    return round(255 * max(darkness, color))


def recover_foreground(pixel: tuple[int, int, int], alpha: int) -> tuple[int, int, int]:
    if alpha <= 8:
        return pixel
    opacity = alpha / 255
    return tuple(
        max(0, min(255, round(255 + (channel - 255) / opacity)))
        for channel in pixel
    )


def find_subject_bounds(image: Image.Image) -> tuple[int, int, int, int]:
    """Find the largest connected, strongly colored region and add a safe margin."""
    width, height = image.size
    pixels = image.load()
    visited = bytearray(width * height)
    largest: list[tuple[int, int]] = []

    def is_subject_seed(pixel: tuple[int, int, int]) -> bool:
        return max(pixel) - min(pixel) >= 45 or min(pixel) <= 175

    for y in range(height):
        for x in range(width):
            index = y * width + x
            if visited[index] or not is_subject_seed(pixels[x, y]):
                continue
            visited[index] = 1
            component: list[tuple[int, int]] = []
            queue: deque[tuple[int, int]] = deque([(x, y)])
            while queue:
                point_x, point_y = queue.popleft()
                component.append((point_x, point_y))
                for next_x, next_y in (
                    (point_x - 1, point_y),
                    (point_x + 1, point_y),
                    (point_x, point_y - 1),
                    (point_x, point_y + 1),
                ):
                    if not (0 <= next_x < width and 0 <= next_y < height):
                        continue
                    next_index = next_y * width + next_x
                    if visited[next_index] or not is_subject_seed(pixels[next_x, next_y]):
                        continue
                    visited[next_index] = 1
                    queue.append((next_x, next_y))
            if len(component) > len(largest):
                largest = component

    if not largest:
        return (0, 0, width, height)
    margin = 6
    left = max(0, min(x for x, _ in largest) - margin)
    top = max(0, min(y for _, y in largest) - margin)
    right = min(width, max(x for x, _ in largest) + margin + 1)
    bottom = min(height, max(y for _, y in largest) + margin + 1)
    return (left, top, right, bottom)


def process(source: Path, destination: Path) -> dict[str, int]:
    source_image = Image.open(source).convert("RGB")
    width, height = source_image.size
    pixels = source_image.load()
    connected = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()

    def enqueue(x: int, y: int) -> None:
        index = y * width + x
        if connected[index] or not is_background_candidate(pixels[x, y]):
            return
        connected[index] = 1
        queue.append((x, y))

    for x in range(width):
        enqueue(x, 0)
        enqueue(x, height - 1)
    for y in range(height):
        enqueue(0, y)
        enqueue(width - 1, y)

    while queue:
        x, y = queue.popleft()
        for next_x, next_y in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y + 1),
        ):
            if 0 <= next_x < width and 0 <= next_y < height:
                enqueue(next_x, next_y)

    result = Image.new("RGBA", (width, height))
    output = result.load()
    transparent = 0
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if connected[y * width + x]:
                alpha = matte_alpha(pixel)
                rgb = recover_foreground(pixel, alpha)
                transparent += alpha == 0
            else:
                alpha = 255
                rgb = pixel
            output[x, y] = (*rgb, alpha)

    result = result.crop(find_subject_bounds(source_image))
    destination.parent.mkdir(parents=True, exist_ok=True)
    result.save(destination, optimize=True)
    return {
        "width": result.width,
        "height": result.height,
        "transparent": transparent,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    stats = process(args.source, args.destination)
    print(
        f"wrote {args.destination} "
        f"({stats['width']}x{stats['height']}, {stats['transparent']} transparent pixels)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
