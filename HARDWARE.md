# Phoenix — Hardware and Build Plan

## 1. Build philosophy

This is a single device project, not a platform. Every part should exist to make the bathroom music experience better: voice control, personal music playback, screen feedback, and a sealed form that can live in the wet area.

The build should feel finished, not like a proof of concept stuffed into a housing. That means:

- one coherent enclosure
- intentional speaker and microphone placement
- clean power and connectivity
- a screen that adds value instead of just existing
- electronics that are protected and serviceable enough to build once and trust

## 2. Chosen device core

The device core is a Raspberry Pi Zero 2 W class machine.

Why this class:

- small enough to fit comfortably inside a compact appliance-style enclosure
- capable enough to run the voice stack, the music client, and the display
- familiar enough that the project stays buildable by one person
- easy to run headless once it is set up

This is not a microcontroller-only project. The device needs to do several things at once: listen, parse speech, talk to a music server, play audio, and draw visuals. A small Linux board is the most direct path.

## 3. Core board selection logic

The main board should provide:

- Wi-Fi for talking to the music server
- enough compute for offline speech recognition and basic playback
- a display interface and GPIO for whatever add-ons are needed
- a reasonable audio path, or room to add one

If the base board’s built-in audio I/O is weak, add a small codec or audio HAT/module rather than trying to force bad audio paths. For a bathroom voice music device, mic quality and speaker output matter more than raw spec sheets.

## 4. Display

The display should be small, integrated, and easy to drive.

Good fit characteristics:

- small LCD in the smartphone-smaller or sub-smartphone range
- a driver chip that is easy to talk to from the board
- enough resolution for simple UI, album art, and abstract animation
- not so large that it becomes the weakest point in the enclosure

A SPI-driven small LCD is a sensible class of part for this project. The exact panel can vary, but the design intent is: small, simple, and visually calm.

## 5. Audio output

The speaker path should be chosen for real use in a bathroom, not for bench audio quality.

Design goals:

- built-in speaker(s) that can be heard over shower noise
- a driver or amp stage if the board cannot drive the speaker directly
- a physical opening that is acoustically clear but protected
- enclosure bass/tuning choices that are acceptable for casual music playback

This is one of the places where the enclosure and electronics must be designed together. Speaker size, enclosure volume, and the speaker port all affect the result.

## 6. Microphone path

The microphone path is just as important as the speaker path.

Design goals:

- a mic or mic array that can pick up voice in a noisy bathroom
- protection from direct water exposure
- an acoustic opening that is deliberately designed, not an accidental hole
- placement that favors voice pickup from the front or top of the device

Practical protection approach:

- use a waterproof acoustic membrane or vent over the microphone port
- keep the opening away from direct spray where possible
- design the housing so water does not pool over the mic entrance

## 7. Enclosure material and construction

The enclosure should be durable, water-resistant, and easy to assemble.

Best-fit material direction:

- ASA is the strongest pick for a bathroom device because it has good UV resistance and better weatherability than PETG
- PETG is easier to print and still moisture resistant, so it is a valid fallback if ASA is not available
- whichever material is used, the enclosure should not rely on the print alone for waterproofing

Construction approach:

- sealed two-part enclosure with gasket or o-ring closure
- thin walls in the right places, thicker where strength and sealing matter
- recessed window area for the screen
- a designed acoustic opening for the speaker and mic, not a printed hole left to chance
- mounting features built into the body for shelf, bracket, or wall mounting

If the device will be used long term in a bathroom, the enclosure should feel like it belongs there: easy to wipe, resistant to humidity, and not full of seams that trap water.

## 8. Waterproofing strategy

Waterproofing is a system, not a single gasket.

Layers of protection:

- enclosure sealing at the main split line
- membrane or vent over acoustic openings
- covered or absent external ports in the final device
- conformal coating on the PCB where appropriate
- potting or localized sealing for vulnerable sections if needed
- smart geometry so water runs away from joints and openings

Target behavior:

- dust-tight
- protected against water jets and splash
- able to survive bathroom humidity and accidental spray

Realistic note: the hardest part is usually not the case itself, but the places where sound and air must pass through. That includes the speaker opening, the microphone port, and any venting needed to avoid pressure/trap issues.

## 9. Power and connectivity

For a bathroom install, power should be clean and permanent if possible.

Preferred approach:

- wired power through a sealed inlet
- a panel-mount or bulkhead-style sealed connector if the device is meant to stay installed
- cable routing that does not create a water path into the enclosure
- no exposed USB or loose connectors in the final bathroom version

If battery is used temporarily during development, plan for charging and runtime early. For the final device, built-in speakers and continuous availability suggest a mains-powered install more than a battery-powered gadget.

## 10. Mounting and placement

The device should work in more than one bathroom layout.

Supported mounting options:

- shelf or ledge placement
- wall bracket
- suction-based mounting for smooth surfaces
- adhesive mount only if the surface and adhesive are appropriate

The enclosure should include mounting geometry so the same device can live in different spots without needing a separate accessory product.

Placement considerations:

- keep the microphone out of direct water stream
- keep the screen readable without being directly in the spray
- leave room for sound to exit the speaker
- avoid trapping water behind the device

## 11. Software stack

### Music server

Primary choice:

- Airsonic-Advanced

Strong alternative:

- Navidrome

Both serve a personal music library and expose a Subsonic-compatible API. That makes the device a client rather than a magic catalog.

### Voice stack

Wake word:

- a lightweight wake-word engine such as Porcupine or an open alternative like openWakeWord

Speech recognition:

- Vosk for offline-capable recognition

Intent handling:

- a small parser for commands like "play X by Y"
- fuzzy matching or best-match logic against library metadata
- clear fallback when the request is ambiguous

This stack keeps the voice path local-first and believable. It does not need to be perfect. It needs to work often enough that the device feels useful.

### Music client

The device should behave like a Subsonic client:

- authenticate against the server
- search by artist/title
- retrieve song metadata
- stream or play the matched track

This is the mechanism that turns a voice request into actual music from your library.

### Visuals and UI

The screen should show:

- idle animation or ambient behavior
- listening state
- recognized request
- now playing state
- match/no-match feedback
- simple playback status

Keep the UI sparse. The device is a bathroom object; it should feel calm and readable from a distance, not like a compact phone app.

## 12. Firmware and system software approach

The device software should be split into clear roles:

- system services for networking, audio, and startup
- voice service for waking and recognition
- music client service for server communication and playback
- visual service for screen state and animation

This separation makes the project easier to debug and easier to describe in a Hack Club journal. Each layer can be tested independently.

## 13. Acoustic and mechanical integration

The device’s character comes from how the electronics sit inside the object.

Key integration points:

- speaker position relative to the enclosure volume
- mic position relative to the user and water sources
- screen recess depth and viewing angle
- openable or serviceable enclosure without making it feel fragile
- overall proportions that read as one object

The result should be something you would not mind leaving in a bathroom. That is a higher bar than “it works on the bench.”

## 14. Build sequence

The build should proceed in this order:

1. Define the enclosure size and internal layout
2. Choose board, display, speaker, mic, and power path
3. Design the acoustic openings and sealing strategy
4. Assemble the electronics on a prototype basis if needed
5. Get basic audio playback working
6. Get the display working
7. Get the music server client working
8. Add wake word and voice recognition
9. Add music request matching
10. Add screen visuals and status behavior
11. Finalize enclosure, sealing, and mounting
12. Install and tune for bathroom use

This order keeps the mechanical and electrical decisions from trapping the software, and keeps the software from hiding weak mechanical choices.

## 15. Acceptance criteria

The build is done when:

- the device plays music from your self-hosted library
- voice requests like “play X by Y” work well enough in real use
- the screen shows meaningful state and visuals
- the enclosure is sealed and bathroom-viable
- the device can be mounted and powered cleanly
- the whole thing feels like a finished object, not a lab experiment

## 16. What is intentionally left for real-life assembly

This plan is complete except for the physical build itself.

Left for hands-on assembly:

- printing, machining, or otherwise fabricating the enclosure
- sealing, gasketing, and testing the enclosure
- wiring and fitting the actual boards, speaker, microphone, and display
- conformal coating, potting, or other protection work on the real hardware
- final mounting in the bathroom and practical tuning
- actual sound tuning, mic placement tuning, and enclosure tweaking

Everything else — the device concept, the architecture, the parts direction, the waterproofing approach, the software stack, and the build sequence — is fully designed here.
