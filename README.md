# Phoenix

A bathroom voice music device that plays songs from a self-hosted open source music server by voice request, with onboard screen animations and built-in speakers.

## What it does

- Voice control for music requests like "Hey Phoenix, play [song] by [artist]"
- Plays from a personal music library served by an open source music server
- Shows visual feedback on a small screen, with animations or music-reactive visuals
- Built for wet-room use, with a waterproof-friendly form factor and no phone in the shower

## Why this exists

The goal is a dedicated device for music in the bathroom without hauling a phone into the wet area every time. It keeps the phone out of the shower while still giving a fast, natural way to request music.

## Chosen stack

- **Music server:** Airsonic-Advanced as the main option, with a Subsonic-compatible backend in mind as an alternative
- **Voice control:** offline-friendly speech recognition using Vosk for local request handling, with a possible server-side fallback
- **Device side:** custom electronics with a small display, speaker output, microphone path, and a processor that can handle voice, playback, and visuals
- **Music source:** personal library stored on the server, not a broad internet catalog

## Project scope

This is meant to be a believable single-device project for Forge/Fabricate:
- waterproof enclosure and shower-friendly interface
- voice request handling for playback from a chosen music source
- visual feedback on the screen
- built-in audio output

## Repository journal

Progress is tracked in `JOURNAL.md`.

## Photos and diagrams

### Device overview

![Device mockup](assets/placeholder-1.png)
*Top-down view of the finished device showing the integrated screen, speaker grille, and microphone port on the front face.*

### Enclosure and build

![Enclosure concept](assets/enclosure.png)
*3D view of the sealed two-part ASA enclosure with the display recess, speaker port, and gasket channel visible.*

### Schematic and wiring

![Schematic diagram](assets/block-diagram.svg)
*Block diagram of the electronics: compute board, display, speaker amp, microphone path, and power inlet, with signal flow arrows.*

### PCB layout

![PCB rendering](assets/device-mockup.svg)
*PCB layout view showing component placement, trace routing, standoff positions, and the sealed connector footprint.*

### Audio and voice signal path

![Audio flow](assets/audio-flow.png)
*Signal flow from microphone capture through voice recognition to music server request and speaker playback.*

![Voice pipeline](assets/voice-map.png)
*Voice pipeline map: wake-word detection, command capture, Vosk recognition, intent parsing, and library match.*

---

**Images cover:** device build photo, 3D enclosure model, schematic / wiring diagram, PCB layout, audio signal path, and voice recognition pipeline.

### Bill of Materials

| Qty | Part class | Example part | Links |
| --- | --- | --- | --- |
| 1 | Compute board | Raspberry Pi Zero 2 W | https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ |
| 1 | Display + touch | Small SPI touch LCD | small SPI touch LCD, smartphone-smaller class |
| 1 | Speaker | Small waterproof-friendly speaker | built-in music output |
| 1 | Amplifier / codec | Small audio amp or codec HAT | clean audio output |
| 1 | Microphone | Protected mic or mic array | voice pickup in noisy bathroom |
| 1 | Acoustic membrane / vent | Waterproof acoustic membrane | keeps water out while letting sound through |
| 1 | Enclosure material | ASA filament or sheet stock | bathroom-durable, UV-resistant |
| 1 | Sealing parts | Gaskets, O-rings, adhesive seal | real waterproofing at enclosure split |
| 1 | Power hardware | Panel-mount sealed power inlet | clean permanent power |
| 1 | Mounting hardware | Bracket, suction, or adhesive mount | supports different mounting styles |
| 1 | Internal hardware | Screws, standoffs, threaded inserts | serviceable internals |
| 1 | Protective finish | Conformal coating or selective potting | extra protection for vulnerable electronics |

- Compute board: https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/
- Display + touch: small SPI touch LCD, e.g. 3.5" class with FT6236 or similar
- Speaker: small waterproof-friendly speaker, sealed or membrane-protected type
- Acoustic membrane / vent: waterproof acoustic membrane, e.g. Gore or equivalent vent cover
- Enclosure material: Prusament ASA — https://prusa.io/3d-printing-materials/asa/ or Polymaker ASA — https://www.polymaker.com/product/polyformer-as
- Power hardware: panel-mount sealed power inlet, e.g. 10 mm or 12 mm bulkhead connector
- Sealing parts: closed-cell foam cord or silicone gasket material for the enclosure split
- Internal hardware: M2.5 or M3 screws, threaded inserts, and standoffs matched to the enclosure and board

---

## Chosen stack

- **Music server:** Airsonic-Advanced as the main option, with a Subsonic-compatible backend in mind as an alternative
- **Voice control:** offline-friendly speech recognition using Vosk for local request handling, with a possible server-side fallback
- **Device side:** custom electronics with a small display, speaker output, microphone path, and a processor that can handle voice, playback, and visuals
- **Music source:** personal library stored on the server, not a broad internet catalog

## Project scope

This is meant to be a believable single-device project for Forge/Fabricate:
- waterproof enclosure and shower-friendly interface
- voice request handling for playback from a chosen music source
- visual feedback on the screen
- built-in audio output

## Repository journal

Progress is tracked in `JOURNAL.md`.
