---
title: "Phoenix"
github: "https://github.com/kiyanshsaini604-cmyk/phoenix-bathroom-music"
description: "A bathroom voice music device that plays songs from a self-hosted music server by voice request with onboard animations."
created_at: "2026-03-20"
total_time: "2h"
---

## March 20, 2026: Project kickoff and stack choice

Decided on the core idea: a dedicated bathroom music device that listens for voice requests like "Hey Phoenix, play X by Y" and plays from a self-hosted open source music server, with onboard screen animations instead of a phone.

Chose the software direction first:
- Music server: Airsonic-Advanced as the primary option, with a Subsonic-compatible path in mind in case a lighter server is easier to run locally.
- Voice control: local speech-to-text approach using Vosk for the "play song by name" flow, with a server-side fallback if recognition gets too weak on-device.
- Visuals: small screen with music-reactive or ambient animations rather than a full video player.

One big decision here: this is built around a personal music library, not an all-songs internet catalog. That keeps the project realistic and avoids drifting into a legal/licensing mess.

**Total time spent: 2h**

---

## March 21, 2026: Full design locked, ready for real assembly

Designed the entire device now: product idea, enclosure direction, electronics, software stack, parts direction, and build sequence.

Key decisions:
- Compact Linux device as the core, because it needs to do voice, playback, display, and server access together.
- Built-in speaker and a protected microphone path, because this is a bathroom device, not a bench prototype.
- Small integrated screen for status and visuals, not a phone-style UI.
- Self-hosted music server as the source, with Airsonic-Advanced as the primary choice and Navidrome as the alternative.
- Local-first voice path using a wake-word engine plus Vosk, with simple "play X by Y" intent matching against the library.
- Waterproofing treated as a system: sealed enclosure, acoustic membranes over openings, covered ports, and conformal coating or potting where needed.

Wrote the supporting docs:
- SPEC.md — full design spec
- HARDWARE.md — hardware and build plan
- SOFTWARE.md — software architecture
- PARTS.md — parts and materials direction

Everything is designed except the physical build itself. Left for real-life assembly:
- printing or making the enclosure
- sealing, gasketing, and testing it
- fitting the boards, speaker, mic, and display
- coating/potting and final install
- tuning sound, voice, and enclosure behavior in the actual bathroom

**Total time spent: 3h**

---

## March 22, 2026: Added voice and touch playback controls

Added the full control behavior to the design.

Now the device supports:
- voice commands for play, pause, back, and forward
- touch controls for the same actions
- back/forward with an optional time like "back 10 seconds" or "forward 30"
- a default seek of 15 seconds when no time is given

This makes the device feel like a real music controller instead of just a play/pause box.

Updated the spec and both the hardware and software docs to match:
- touch is now a first-class secondary control
- the screen/touch surface is treated as part of the bathroom-friendly UI
- playback behavior is unified across voice and touch
- seek logic is explicit: use the requested time if provided, otherwise default to 15 seconds

**Total time spent: 2h**
