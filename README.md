# Mega Man ZX — tracker pack

Map images for the [Mega Man ZX Archipelago world](https://github.com/Nekusen/Archipelago-MegaManZX),
used by **Universal Tracker**'s map tab. A full PopTracker pack (item tracking
and access logic usable without Universal Tracker) is planned on top of these
files.

## Using it with Universal Tracker

1. Download `mmzx_tracker.zip` from the [Releases](https://github.com/Nekusen/MegaManZX-Tracker/releases)
   page. Keep it zipped.
2. The first time Universal Tracker opens the map tab of a Mega Man ZX slot it
   asks for the zip: pick the file. You can also set the path in `host.yaml`
   under `mmzx_settings` → `ut_pack_path`.

The map layout (which map is which, where every check sits) ships inside the
world itself (`tracker/maps.json`, `tracker/locations.json`); this pack only
supplies the pictures, so it does not need updating when the logic changes.

## What the images are

- `images/area_*.png`, `images/room_*.png`: one map per area and one per
  room. They are **collision silhouettes** generated from the game's level
  data by the tools of the private development toolkit: light = walkable
  space, dark = solid, thin lines = platforms you can drop through, ochre =
  ladders, red = spikes, blue = water. They contain no game artwork.
- `images/player.png`: the player position marker.

The silhouettes are rendered from the level geometry of Mega Man ZX, which is
© Capcom Co., Ltd. This is a fan project, not affiliated with or endorsed by
Capcom or Inti Creates.

## License

Everything in this repository that is our own work (the generated map
layouts, marker artwork, scripts and documentation) is released under the MIT
License, see `LICENSE`.
