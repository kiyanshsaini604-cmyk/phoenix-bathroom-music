# Phoenix — Design Spec

## 1. What it is

Phoenix is a dedicated bathroom voice music device. It lives in the wet area, stays out of the way, and lets you request music by voice without bringing a phone into the shower every time.

The core interaction is:

- You say something like "Hey Phoenix, play X by Y"
- The device understands the request, pulls the track from your self-hosted music server, and plays it
- A small screen shows visual feedback instead of a phone UI
- Speakers built into the device give you the sound

It is meant to feel like a small appliance, not a laptop or a phone clone.

## 2. Why this shape

The interesting parts of the project are:

- voice input as the primary control
- a personal music library as the source
- visual feedback on a small screen
- a form factor that actually works in a bathroom

This keeps the project focused. The device is not trying to be a universal music service. It is a physical object for one specific ritual: music in the shower or bath, controlled by voice, with no phone in the wet zone.

## 3. Product language

The design language should feel calm, minimal, and slightly playful, but not like a toy.

Good reference points to steal from:

- small shower speakers that feel like sealed objects
- compact voice assistants with a single clear status indicator
- music players that use light and motion instead of dense menus

Phoenix should look like one object, not a sandwich of exposed boards and wires. The screen should feel integrated, the speaker opening should feel intentional, and the mic should feel present without shouting "microphone."

## 4. Physical form

### Overall shape

- A small rounded rectangle or soft cylinder, sized to sit on a shelf, ledge, or wall mount
- Not too big. Think "small music object," not "tablet with a speaker"
- Edges should be soft enough to feel friendly in a bathroom setting
- Top or front should read as the main face

### Screen

- A small LCD, roughly smartphone-small or smaller, depending on how much visual presence you want
- The display should be recessed a little or shielded so it does not become the weakest waterproof point
- Use the screen for:
  - album/artist art or abstract visuals
  - music-reactive animation
  - simple status: listening, playing, idle, error
- Do not cram dense UI onto it. This is not a phone screen

### Speaker

- Built-in speaker(s) aimed to sound decent in a small room, not audiophile grade
- The speaker path should be acoustically open but physically protected
- The speaker grill can double as part of the visual identity

### Microphone

- One or more microphones placed where they can hear voice over bathroom noise
- The mic path should be protected by an acoustic membrane or vent cover so water does not get in
- The mic area should be visually subtle but not invisible; people should know where to talk to

### Controls

- No physical buttons unless there is a very good reason
- Primary control is voice
- A small hardware state indicator or one tactile control can help for wake, mute, or emergency off
- The device should still be usable if voice is imperfect

### Mounting

The device should support more than one way to live in the bathroom:

- shelf placement
- wall mounting
- possibly suction or bracket mounting for shower areas

That matters because bathrooms are not all the same. A good bathroom object should adapt without needing to become a different product.

## 5. Waterproofing approach

This is a wet-room device, so the enclosure needs real thought.

### Target

Aim for something like IP65 or better in practice, meaning dust-tight and protected against water jets/splash, with extra care around the speaker and mic openings.

### How to achieve it

- Use a sealed enclosure with gasket or o-ring closure where the case splits
- Protect acoustic openings with waterproof acoustic membranes or vents
- Recess or cover any ports, buttons, and seams
- Use conformal coating or potting where needed on the electronics
- Keep the display window and speaker path as the main design challenges, not afterthoughts

### Important detail

Waterproofing is not just a box with tape. The tricky part is letting sound out and air/moisture behavior stay controlled while keeping water out. That is where membranes, vents, sealing, and geometry all matter.

## 6. Electronics architecture

### Compute

A small single-board computer style device is the simplest path for a project like this because it can:

- run the voice stack
- talk to the music server
- drive a display
- play audio
- handle the app-level logic in one place

A compact board with Wi-Fi and enough graphics/audio capability is the right class of hardware. The device should be able to run headless, without a monitor keyboard setup in daily use.

### Audio

- Output path to the built-in speaker
- Input path from the microphone
- If the board does not have great built-in audio I/O, add a small audio interface or codec hat/module
- The audio pipeline should support playback from the music server and capture from the mic for voice

### Display

- Driven by the main board over the appropriate display interface
- Chosen for small size, low power, and simple integration
- Should be good enough for abstract animation and clear status, not necessarily rich video playback

### Connectivity

- Wi-Fi to talk to the music server
- Optionally wired power in the final bathroom install
- If battery is used, there should be a charging path and power management plan

### Sensors

- Microphone is the main sensor
- Optionally a simple status LED or small indicator array
- Optionally a physical mute/ wake control

## 7. Software architecture

### Music source

The music source is a self-hosted server serving a personal library.

Best-fit options:

- Airsonic-Advanced as the primary choice
- Navidrome as a lighter Subsonic-compatible alternative
- Any Subsonic-compatible server if it is easier to run locally

The device acts as a client to that server.

### Voice flow

The intended flow is:

1. Device listens for the wake phrase
2. After wake, it captures the command
3. Speech is turned into text locally when possible
4. The text is interpreted as a music request
5. The request is matched against the music library
6. The right track is played

A good practical stack:

- Vosk for offline-capable speech recognition
- A local wake-word detector if you want true hands-free behavior
- A simple intent parser for "play X by Y" style requests
- Fallback behavior when recognition is uncertain

The voice path does not need to be perfect. It needs to be believable and useful.

### Music playback

The device should:

- search the library by artist/title
- pick the best match
- start streaming or playing the track
- show feedback on screen while playback happens

The Subsonic API family gives a reasonable client model:
- authenticate
- search
- fetch song metadata
- stream the track

This is the part that makes "play song by name" actually work against a real library.

### Visuals

The screen should not be decoration. It should communicate:

- listening
- recognized command
- now playing
- library match or no match
- basic playback state

A good visual strategy is a mix of:

- calm ambient animation when idle
- music-reactive motion during playback
- clear state changes when voice is heard
- simple text or art when useful

The goal is "nice to look at while bathing," not "dense app interface."

## 8. What makes it original

The original part is not any single technology. It is the combination:

- a dedicated physical device
- voice-first control
- personal library source
- bathroom-first design
- screen visuals instead of a phone UI
- built-in speakers so the phone can stay out of the wet area

That is a real product-shaped idea rather than a generic showcase build.

## 9. Build sequence

A sensible order:

1. Enclosure concept and dimensions
2. Speaker and mic placement
3. Waterproofing strategy for acoustic openings
4. Main board, display, audio, and power layout
5. Basic playback from the music server
6. Voice wake and recognition
7. Music request matching
8. Screen visuals and status behavior
9. Mounting and install experience
10. Iterate on look, sound, and interaction

This order matters because the hard parts are scattered across mechanical, electrical, and software domains. If you start with the enclosure and the acoustic path first, the rest is easier to fit inside it.

## 10. Success criteria

The project is successful if:

- you can request songs by voice and get the right track most of the time
- the music actually comes from your self-hosted library
- the device feels like an object, not a breadboard in a box
- the screen adds something instead of just being there
- the device can live in a bathroom without feeling fragile
- the whole thing makes sense as a Forge/Fabricate project: original, buildable, and funded for real parts and fabrication

## 11. What this is not

- Not a phone app
- Not a licensed streaming service
- Not a magic all-songs catalog
- Not a full assistant platform
- Not a pure media player with buttons

It is a bathroom voice music object built around your own music and your own hardware.

## 12. Name

"Phoenix" works as the device name and wake word. It gives the project identity without needing a separate branding exercise.
