# Mega Man ZX — tracker pack

Map images for the [Mega Man ZX Archipelago world](https://github.com/Nekusen/Archipelago-MegaManZX),
used by **Universal Tracker**'s map tab. A full PopTracker pack (item tracking
and access logic usable without Universal Tracker) is planned on top of these
files.

## Using it with Universal Tracker

1. Download one of the two zips from the [Releases](https://github.com/Nekusen/MegaManZX-Tracker/releases)
   page and keep it zipped:
   - `mmzx_tracker.zip`: **collision silhouettes** (default). Light =
     walkable space, dark = solid, thin lines = platforms you can drop
     through, ochre = ladders, red = spikes, blue = water. No game artwork.
   - `mmzx_tracker_renders.zip`: the same maps drawn with **the game's own
     level art** (renders of every room). Pick this one if you prefer to see
     the levels as they look in the game.
2. The first time Universal Tracker opens the map tab of a Mega Man ZX slot it
   asks for the zip: pick the file. You can also set the path in `host.yaml`
   under `mmzx_settings` → `ut_pack_path`. To switch flavours, point it at
   the other zip.

The map layout (which map is which, where every check sits) ships inside the
world itself (`tracker/maps.json`, `tracker/locations.json`); both zips share
it, so this pack does not need updating when the logic changes.

## Contents of this repository

- `images/`: one map per area (`area_*.png`) and one per room (`room_*.png`)
  as collision silhouettes, plus `player.png`, the player position marker.
  Generated from the game's level data by the tools of the private
  development toolkit.
- `var_renders/images/`: the same maps over 1:1 room renders drawn from the
  game's level data by the toolkit's own renderer (background layers with
  their real parallax, video registers and alpha blending as measured in
  the game; animations frozen on their first frame). These contain the
  game's artwork, which is © Capcom Co., Ltd., and are provided for
  personal use with the randomizer only.
- `build_pack.py`: builds both release zips.

Mega Man ZX is © Capcom Co., Ltd. This is a fan project, not affiliated with
or endorsed by Capcom or Inti Creates.

## License

Everything in this repository that is our own work (the generated map
layouts, marker artwork, scripts and documentation) is released under the MIT
License, see `LICENSE`.
