# Phoenix hardware summary

This directory is the hardware source tree for the Phoenix device.

Phoenix is a dedicated bathroom voice music device. It is built around a small Linux
board, a small display with touch, a speaker, a protected microphone path, and a
sealed enclosure intended for bathroom use. Music is served from a self-hosted
library by a Subsonic-compatible server.

## Core blocks

- Compute board: Raspberry Pi Zero 2 W class
- Display: small LCD with touch
- Audio: speaker path with optional codec/amp
- Microphone: protected acoustic path with membrane
- Power: sealed inlet for the installed device
- Enclosure: sealed two-part case with acoustic protection

## Source files

- `phoenix.kicad_pro` — KiCad project file
- `phoenix.kicad_pcb` — PCB source
- `phoenix.kicad_sch` — KiCad schematic source
- `phoenix.sch` — schematic
- `phoenix.lib` — project symbol library
- `phoenix-control.h` — device-side hardware constants
- `doc/fabrication.md` — PCB fabrication notes
- `doc/assembly.md` — assembly notes

## Design priorities

- Compact and serviceable hardware
- Clear audio and digital separation where practical
- Acoustic openings that are deliberately designed and protected
- Sealed power for the installed device
- A hardware layout that matches the enclosure and mounting plan

## Relationship to the rest of the project

- Firmware lives in `../firmware/`
- Device software architecture is described in `../SOFTWARE.md`
- Build intent and hardware plan are described in `../HARDWARE.md`
- Parts direction is described in `../PARTS.md`
- The bill of materials is in `../BOM.md`

## What is still left for real assembly

- Final enclosure dimensions and internal layout
- Exact component selection
- Final sealing and acoustic membrane choices
- Final PCB artwork and routing if a custom board is built
- Final enclosure fabrication and install tuning
