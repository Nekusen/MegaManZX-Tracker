# Room art sources (`rooms/`)

One PNG per room, 1:1 game pixels, exactly `screens_wide * 256` by
`screens_high * 192`. These are the SOURCES of the pack: the images in
`images/` (one per area and one per room, scaled and annotated) are composed
from them by the toolkit, and every check, door and player-position marker
is a pixel coordinate inside this grid.

The base is the room rendering of the Mega Man ZX Editor, flattened to this
grid; rooms are then retouched by hand where that rendering falls short
(missing platforms, wrong or noisy backgrounds). Local reference material for
the retouching lives in `../reference/` (not part of the repository).

Editing rules:

- Keep the file name, the PNG format and the EXACT pixel size. Do not crop,
  pad, rotate or rescale; the toolkit refuses renders whose size changed.
- Do not move level geometry: tiles must stay where the game has them, only
  their look may change.
- 8x8 tiles on an 8-pixel grid, 16x16 metatiles on a 16-pixel grid; screens
  are 256x192 cells.
