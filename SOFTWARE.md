# Phoenix — Software Architecture

## 1. System roles

The device software is split into a few clear responsibilities:

- boot and network
- audio capture and playback
- voice wake and recognition
- music server client
- screen visuals and status
- touch input
- device behavior and glue logic

Keeping these separate makes the project easier to test and easier to journal.

## 2. Startup and network

On boot, the device should:

- bring up Wi-Fi or wired networking
- reach the music server
- start the audio path
- start the display and touch input
- start listening for the wake word

The device should be usable headless after setup, without a monitor and keyboard in daily life.

## 3. Audio path

Audio has two directions:

- input from the microphone for voice
- output to the speaker for music

If the board’s built-in audio is not good enough, add a codec, HAT, or external audio interface. The important thing is that the device can capture speech and play music at the same time, or switch cleanly between them.

## 4. Voice pipeline

The voice pipeline has three stages:

1. Wake-word detection
2. Command capture
3. Speech-to-text and intent parsing

Wake word:

- a lightweight wake-word engine such as Porcupine or openWakeWord
- "Hey Phoenix" as the device wake phrase if that matches the product identity

Recognition:

- Vosk for offline-capable recognition
- a small model size if on-device performance matters

Intent parsing:

- "play X by Y" style extraction
- "pause", "play", "back", "forward" handling
- back/forward with optional time, otherwise default to 15 seconds
- best-match lookup against library metadata
- clear fallback when confidence is low or no match is found

The voice path should degrade gracefully. If the device is unsure, it should indicate uncertainty rather than guessing wildly.

## 5. Music server client

The device acts as a Subsonic-compatible client.

Core operations:

- authenticate with the server
- search for songs by artist and title
- fetch song metadata and stream URL or path
- start playback
- seek within a track
- report current track status

The practical API shape is REST-like with XML or JSON depending on the server and client choices. The device should handle authentication in the recommended modern way for the server being used.

## 6. Playback controls

The device should support one unified playback behavior space, whether the command comes from voice or touch.

Voice commands:

- "play"
- "pause"
- "back"
- "forward"
- "back 10 seconds"
- "forward 30 seconds"
- and similar natural variations

Touch commands:

- play/pause
- back
- forward
- optional seek control if the screen UI wants it

Seek behavior:

- back and forward move playback by a requested amount if one is given
- if no amount is given, default to 15 seconds
- the device should show what it is doing on screen so the user understands the seek

This makes the device usable as a real music controller, not just a play/pause trigger.

## 7. Library matching

Matching is the part that makes voice requests feel real.

Approach:

- normalize artist and title text
- search the server for likely candidates
- prefer exact or near-exact matches
- fall back to broader search if needed
- choose the best candidate and play it

This is not a global music database. It is a personal library search, so the matching can be simpler and the results can be more predictable.

## 8. Visual layer

The screen layer should support:

- idle state
- listening state
- recognized-command state
- playing state
- paused state
- no-match or error state
- seek feedback
- music-reactive visuals during playback if desired

Good visual behavior:

- calm colors and motion in idle
- clear state changes when voice or touch is used
- simple feedback for request results
- playback-reactive motion if it looks good and does not distract

The screen is part of the product personality. It should feel like a small appliance display, not a phone.

## 9. Touch input design

Touch should be treated as a real control path, not an afterthought.

Design notes:

- keep targets large enough for wet-hand use
- avoid relying on tiny precise taps unless the UI is built around them
- make state obvious so a quick tap has obvious effect
- if the screen is also the visual display, merge UI and input cleanly
- if a separate touch surface is used, seal it and place it where it is easy to reach

The goal is bathroom-friendly touch: fast, obvious, and forgiving.

## 10. Feedback and sound design

The device should communicate state without being noisy.

Good inputs to feedback:

- wake detected
- command heard
- match found
- playback started
- playback paused
- seek action taken
- playback failed
- mute or off state

Feedback can be a mix of screen behavior and simple audio/visual cues. Keep it subtle. In a bathroom, too much noise or brightness becomes irritating fast.

## 11. Config and persistence

The device should store:

- server address and credentials
- library settings
- default seek time if the builder wants to change it
- default behavior choices
- mounted state if relevant

Configuration should be easy to change during development and stable in daily use.

## 12. Error handling

The device should handle common failure modes:

- server unreachable
- authentication failure
- no match for a voice request
- audio playback failure
- mic or network interruption
- touch misrecognition or accidental input

In each case, the device should show something on the screen and remain usable, not freeze or act dead.

## 13. Development order

A sensible software build order is:

1. get the board running headless
2. get audio capture and playback working
3. get the display working
4. get touch input working
5. get the music server client working
6. add wake word detection
7. add speech recognition
8. add music request matching
9. add unified voice and touch playback controls
10. add seek behavior with the 15-second default
11. add visuals and state feedback
12. polish behavior and edge cases

This order matters because playback, display, touch, and voice are each a whole path. Trying to build them all at once tends to bury the actual problems.

## 14. What is left for real assembly

This document covers software architecture and implementation direction.

What is left for real-life assembly:

- installing and configuring the software on the actual device
- tuning the mic, speaker, and touch behavior with the real enclosure
- adjusting wake word sensitivity and recognition to the bathroom environment
- fitting the device physically and testing it where it will be used
- finishing the enclosure, sealing, and mounting

Everything else is designed here.
