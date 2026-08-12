# Mascot asset notice

The flame mascot was supplied by the project author during development.

The final transparent asset was produced from that supplied image by removing only the near-white background connected to the canvas edge. The character, expression, proportions and eye whites were preserved. `scripts/process_mascot.py` makes that transformation reproducible; `scripts/build_visuals.py` places the approved transparent asset into the repository Hero.

An AI image-edit attempt used the prompt below, but it altered the character and was rejected; no generated pixels from that attempt are included in the final assets:

```text
Edit the supplied flame mascot image only: preserve the character exactly, replace the white background with a uniform chroma green background, do not redraw, resize, crop, or add elements.
```

Before public release, the author must confirm that they own or have permission to publish, modify, and redistribute the original image. Until that confirmation is recorded, the following files are local release candidates and are not granted under the repository's MIT License:

- `mascot-source.png`
- `mascot-transparent.png`
- `hero.png`
- social images or animations derived from the mascot

The simplified `icon.svg` is also derived from the supplied character and follows the same restriction until permission is confirmed.
