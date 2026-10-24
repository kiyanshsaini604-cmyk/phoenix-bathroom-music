---
title: "Phoenix"
github: "https://github.com/Indu/phoenix-bathroom-music"
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
