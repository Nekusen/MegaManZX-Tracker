# Room art sources (`rooms/`)

One PNG per room, 1:1 game pixels, exactly `screens_wide * 256` by
`screens_high * 192`. These are the SOURCES of the pack: the images in
`images/` (one per area and one per room, scaled and annotated) are composed
from them by the toolkit, and every check, door and player-position marker
is a pixel coordinate inside this grid.

Every room was rebuilt by hand on this grid from the level maps ripped by
X GOD, HIVOLT and rmexesaito (RockMan Memorial Hall – Extra Hall, hosted on
VGMaps.com), so each screen shows what the game shows; the two hub rooms
(`z01`, `z02`) still come from the Mega Man ZX Editor's rendering. Screens the
layout declares but the game never shows (the outer ring, unreachable copies
of a level) are left in the margin colour: the toolkit trims them when it
composes the pack (`tools/data/room_crops.json` in the lab), so a room never
needs padding here. Local reference material lives in `../reference/` (not
part of the repository).

The lab checks every source against the game's own geometry
(`tools/check_room_art.py`, using the collision silhouettes and the ROM
renderer): a room whose art is shifted with respect to the collision is
reported with the exact correction, and pure translations can be applied by
the tool.

Editing rules:

- Keep the file name, the PNG format and the EXACT pixel size. Do not crop,
  pad, rotate or rescale; the toolkit refuses renders whose size changed.
- Do not move level geometry: tiles must stay where the game has them, only
  their look may change.
- 8x8 tiles on an 8-pixel grid, 16x16 metatiles on a 16-pixel grid; screens
  are 256x192 cells.
