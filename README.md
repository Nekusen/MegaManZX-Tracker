# Mega Man ZX — tracker pack

Map images for the [Mega Man ZX Archipelago world](https://github.com/Nekusen/Archipelago-MegaManZX),
used by **Universal Tracker**'s map tab. A full PopTracker pack (item tracking
and access logic usable without Universal Tracker) is planned on top of these
files.

## Using it with Universal Tracker

1. Download `mmzx_tracker.zip` from the [Releases](https://github.com/Nekusen/MegaManZX-Tracker/releases)
   page and keep it zipped. It holds the game's world map, one map per area and
   one per room, drawn with the game's own art.
2. The first time Universal Tracker opens the map tab of a Mega Man ZX slot it
   asks for the zip: pick the file. You can also set the path in `host.yaml`
   under `mmzx_settings` → `ut_pack_path`.

The map layout (which map is which, where every check sits) ships inside the
world itself (`tracker/maps.json`, `tracker/locations.json`), so this pack
does not need updating when the logic changes.

## Contents of this repository

- `rooms/`: the room art SOURCES, one 1:1 PNG per room: the Mega Man ZX
  Editor's rendering of each room, flattened to the tracker's screen grid and
  retouched by hand where it falls short. See the README inside for the
  editing rules (same size, same geometry).
- `overall/`: `ingame_map.png`, the world map of the pause menu's MISSION tab,
  taken from the game with every room, link and Transerver revealed.
- `images/`: the pack images composed from those sources (the world map, one
  map per area, one per room, plus `player.png`, the player position marker).
- `build_pack.py`: builds the release zip.

These folders contain the game's artwork, which is © Capcom Co., Ltd., and are
provided for personal use with the randomizer only. Mega Man ZX is © Capcom
Co., Ltd. This is a fan project, not affiliated with or endorsed by Capcom or
Inti Creates.

## Credits

- Room rendering: the Mega Man ZX Editor community tool (used as a tool; no
  code from it is included here).
- Hand retouching was done with the level maps ripped by X GOD, HIVOLT and
  rmexesaito (RockMan Memorial Hall – Extra Hall, 2010, hosted on
  [VGMaps.com](https://vgmaps.com/Atlas/DS/index.htm#MegaManZX)) as
  reference. Thank you for the years of careful ripping.

## License

Everything in this repository that is our own work (the generated map
layouts, marker artwork, scripts and documentation) is released under the MIT
License, see `LICENSE`.
