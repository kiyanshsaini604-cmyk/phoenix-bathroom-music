# Phoenix — system and startup notes

This directory documents the device's system layer: how the board boots,
how services start, and how the environment is configured for a bathroom
install.

## What lives here

- system bringup notes
- service wiring notes
- configuration persistence notes
- bathroom-specific tuning notes

The application logic is in `src/phoenix`. The music client, voice
pipeline, audio manager, and screen layer are all package modules, not
scripts that only live in this folder.

## Startup behavior

The device should bring up in a stable order:

1. Network first — Wi-Fi or wired, with a clear failure path
2. Config load — server address, credentials, preferences
3. Audio subsystem — microphone capture and speaker playback ready
4. Display and touch — screen alive and touchable
5. Music client — authenticated against the self-hosted server
6. Voice pipeline — wake word listening ready
7. Main orchestrator loop — ties the other layers together

A headless device should reach a usable state without a monitor and
keyboard attached in daily life.

## Configuration persistence

Configuration should survive reboots:

- server address, user, and password
- default seek duration
- display brightness preferences
- mounted state if the builder wants it remembered
- any per-environment toggles needed for the bathroom install

Config is loaded from `config/device.json` during development. In the
installed device, that should be replaced with a persistent config
source rather than a checked-in file.

## Service wiring

The device is intended to run a small set of cooperating services:

- an audio service for capture and playback
- a voice service for wake detection and recognition
- a music client service for server communication and playback control
- a screen service for state feedback and touch input
- an orchestrator that merges voice and touch commands into one behavior space

Keeping these separated makes the project easier to debug and easier to
describe in a Hack Club journal. Each layer can be exercised on its own
where possible.

## Bathroom tuning

The bathroom environment changes what "works" means:

- Wake sensitivity should be tuned for the expected noise level
- Microphone placement should favor voice pickup over spray paths
- Touch targets should remain usable with wet hands
- Brightness and sound should stay calm enough for long-term use
- The device should not behave like it has a dangling cable in the shower

## Development vs installed device

For development:

- Wi-Fi credentials are temporary
- config can live in the repo config file
- logs can be verbose
- the audio path can be tested with loopback or desktop audio

For the installed device:

- wired power through a sealed inlet is preferred
- no exposed USB in the final bathroom version
- config is persisted locally
- audio, mic, touch, and visuals are tuned to the actual enclosure
