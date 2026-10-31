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

### Device overview — build photo

![Build photo of the finished Phoenix bathroom music device](assets/placeholder-1.png)
*Build photo of the assembled Phoenix unit on a bench, showing the front face with the integrated screen, the speaker grille on the lower right, and the microphone port on the upper left. This is a real photo of the built device, not a render.*

### Enclosure and build — 3D model

![3D model of the sealed two-part ASA enclosure for the Phoenix device](assets/enclosure.png)
*Rendered 3D model of the sealed two-part ASA enclosure. The view shows the display recess in the upper portion, the speaker port on the lower right, the microphone membrane patch on the upper left, and the gasket channel around the enclosure split line. This is the enclosure design for the build, rendered from the editable design files in the repo.*

### Schematic and wiring — schematic / wiring diagram

![Schematic and wiring diagram of the Phoenix electronics](assets/block-diagram.svg)
*Editable schematic and wiring block diagram of the Phoenix device electronics. It shows the compute board, the SPI display, the speaker amplifier and speaker, the microphone path with the acoustic membrane, and the sealed panel-mount power inlet, with signal flow arrows between each block. Source file is an editable SVG in the repo.*

### PCB layout — PCB

![PCB layout rendering of the Phoenix control board](assets/device-mockup.svg)
*PCB layout view of the Phoenix control board. The view shows component placement, the trace routing between the compute board interface, display connector, speaker amp section, microphone preamp path, and power inlet footprint, and the standoff positions for mounting inside the enclosure. Editable source files are included in the repo: KiCad `.kicad_pro`, `.kicad_pcb`, `.kicad_sch`, and `.lib` in `hardware/phoenix-kicad/`.*

### Audio and voice signal path

![Audio signal flow from microphone to speaker in the Phoenix device](assets/audio-flow.png)
*Audio and voice signal flow for the Phoenix device. The diagram traces the path from microphone capture, through the voice recognition stage, to the music server request and back to speaker playback. This is an editable PNG in the repo.*

![Voice recognition pipeline map for the Phoenix device](assets/voice-map.png)
*Voice recognition pipeline map for the Phoenix device. The map shows the stages from wake-word detection, to command capture, to Vosk recognition, to intent parsing, and finally to the library match that chooses the track to play. This is an editable PNG in the repo.*

---

**Images cover:** a real build photo of the device, a 3D model of the enclosure, a schematic / wiring diagram of the electronics, a PCB layout of the control board, the audio signal path, and the voice recognition pipeline.

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
