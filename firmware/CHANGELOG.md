# Changelog

## 0.1.0 - 2026-03-21

Initial firmware scaffold and device service tree for the Phoenix bathroom
voice music device.

### Added
- Device orchestrator with startup, command handling, and shutdown hooks
- Config loading with validation
- Audio manager with capture and playback state
- Voice pipeline with parsing for play, pause, back, and forward commands
- Subsonic-compatible music client stub with library search, play, pause,
  resume, and seek behavior
- Screen and touch layer for device state feedback
- Exception classes for config, server, recognition, playback, and no-match
  failures
- Pytest suite covering config, music client, voice pipeline, audio manager,
  UI, and orchestrator
- Packaging metadata, spec file, Makefile, and changelog
