# Phoenix Device Firmware

This directory contains the Phoenix device firmware and system services.

Phoenix is a dedicated bathroom voice music device. It listens for a wake phrase,
captures a music request, matches that request against a self-hosted music library,
and plays audio from a Subsonic-compatible server. The device also shows status and
visual feedback on a small touch screen.

## What is in this directory

- `src/phoenix/` — device software package
  - `phoenix.py` — top-level orchestrator
  - `config.py` — configuration loader
  - `schemas.py` — configuration validation
  - `audio.py` — microphone capture and speaker playback manager
  - `voice.py` — wake-word and command parsing pipeline
  - `music.py` — Subsonic-compatible music client
  - `ui.py` — screen state and touch input layer
  - `exceptions.py` — domain exceptions
- `config/device.json` — device configuration example
- `system/README.md` — system and startup notes
- `tests/` — pytest test suite
- `Makefile` — common development commands
- `requirements.txt` — Python dependencies
- `pyproject.toml` — packaging metadata
- `phoenix.spec` — source package spec
- `CHANGELOG.md` — release notes
- `LICENSE` — project license

## Architecture

The device software is split into a small number of clear responsibilities:

- startup and configuration
- audio capture and playback
- voice wake and command parsing
- music server client
- screen visuals and touch input
- orchestrator that ties voice and touch commands into one playback behavior space

The voice path is local-first. The music source is a self-hosted library served by
Airsonic-Advanced or a compatible Subsonic server such as Navidrome.

The device is intended to run on a small Linux board with Wi-Fi and enough compute
for voice, playback, display, and server access.

## Command model

Voice and touch share one command model.

Supported actions:

- `play`
- `pause`
- `back`
- `forward`
- `play_song_by_artist_title`

For `back` and `forward`, if no time is given, the default seek is 15 seconds.

Examples:

- "play"
- "pause"
- "back"
- "forward"
- "back 10 seconds"
- "forward 30 seconds"
- "play last nite by the strokes"

## Configuration

Device configuration lives in `config/device.json` during development. The config
covers:

- music server URL, user, and password
- voice wake phrase
- default seek duration
- display brightness preferences

Configuration is validated with a schema layer. Invalid config should fail early
rather than producing confusing runtime behavior.

## Running

From the `firmware/` directory:

```bash
make deps
make test
make lint
python -m phoenix
```

## Testing

The test suite covers configuration loading, music client behavior, voice parsing,
audio manager state, screen/touch behavior, and orchestrator structure.

Run it with:

```bash
make test
```

## Hardware relationship

The firmware is built against the hardware described in
`../hardware/phoenix-kicad/` and `../HARDWARE.md`. The device itself is a compact
enclosed product with a screen, speaker, microphone, and sealed power path. The
firmware assumes:

- a small LCD with touch
- a microphone path
- a speaker output path
- Wi-Fi or wired network access to the music server
- a sealed enclosure suitable for bathroom use

## Development notes

- This is the device software tree for the Phoenix project.
- The code is intended to be runnable, testable, and reviewable as a real project,
  even before the physical build is complete.
- The music client and voice pipeline are written against the same interfaces used
  by the orchestrator, so behavior can be exercised and extended incrementally.
- Hardware-specific drivers and board integration are expected to be filled in as
  the physical device is assembled.
