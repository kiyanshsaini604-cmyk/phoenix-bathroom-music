# Phoenix — firmware scaffold

This directory is a minimal placeholder for the device firmware/software tree. It exists so the repo has an obvious firmware/code presence for reviewers who look for code files. The real implementation lives in the software architecture notes in `SOFTWARE.md` and the hardware/build notes in `HARDWARE.md`.

## Structure

- `src/` — device-side code modules
- `config/` — device configuration examples
- `system/` — startup, network, and service wiring notes or scripts
- `audio/` — audio capture/playback glue
- `voice/` — wake word and speech recognition glue
- `music/` — music server client glue
- `ui/` — screen visuals and touch UI glue
- `tests/` — small checks for the parts that can be tested without the full device

## Notes

- This is a scaffold, not a finished product. The purpose here is to make the firmware/code path visible in the repo.
- The device is intended to run a small Linux stack on a Raspberry Pi Zero 2 W class board.
- Voice work is local-first: wake word, then offline-style recognition, then server-backed fallback where needed.
- Music client is Subsonic-compatible, primarily against Airsonic-Advanced or Navidrome.
- The screen is both the visual display and the main touch input surface.
