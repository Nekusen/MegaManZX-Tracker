# Room art sources (`var_renders/rooms/`)

One PNG per room, 1:1 game pixels, exactly `screens_wide * 256` by
`screens_high * 192`. These are the SOURCES of the renders flavour: the pack
images in `var_renders/images/` (one per area and one per room, scaled and
annotated) are composed from them by the toolkit, and every check, door and
player-position marker is a pixel coordinate inside this grid.

Editing rules (hand retouching is welcome, this is what the folder is for):

- Keep the file name, the PNG format and the EXACT pixel size. Do not crop,
  pad, rotate or rescale; the toolkit refuses renders whose size changed.
- Do not move level geometry: tiles must stay where the game has them, only
  their look may change (missing platforms, wrong backgrounds, artefacts).
- 8x8 tiles on an 8-pixel grid, 16x16 metatiles on a 16-pixel grid; screens
  are 256x192 cells.
- The renderer's output is the starting point; regenerating it overwrites
  nothing here (it writes to the toolkit's `work/` folder), so edits are safe.
- Most rooms were then overlaid with the RockMan Memorial Hall – Extra Hall
  rips hosted on VGMaps.com (see the credits in the top-level README): where
  a screen of the rip matches our grid, its pixels replace the render, so the
  backgrounds sit where the game puts them. The mappers' credit blocks and
  white margins are never copied. Rooms retouched by hand are kept as they
  are when the overlay tool runs again (`--skip`).
