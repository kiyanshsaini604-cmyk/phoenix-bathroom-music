# Phoenix Hardware

This directory contains the hardware source for the Phoenix device.

Phoenix is a bathroom voice music device. It uses a small Linux board, a display
with touch, a speaker, a protected microphone path, and a sealed enclosure suited
for bathroom use. The firmware for the device lives in `../firmware/`.

## What is in this directory

- `phoenix.kicad_pro` — KiCad project file
- `phoenix.kicad_pcb` — PCB source
- `phoenix.kicad_sch` — KiCad schematic source
- `phoenix.sch` — schematic
- `phoenix.lib` — project symbol library
- `phoenix-control.h` — device-side hardware constants
- `doc/fabrication.md` — PCB fabrication notes
- `doc/assembly.md` — assembly notes
- `doc/summary.md` — hardware summary

## Project intent

The hardware is designed around a compact enclosure that fits a Raspberry Pi Zero 2 W
class board, a small display, a speaker, a microphone, and a sealed power path.

The main design goals are:

- small, serviceable board layout
- clear audio and digital separation where practical
- mounting holes that match the enclosure plan
- acoustic openings that use membranes instead of open printed holes
- a sealed power inlet for the installed device
- internal hardware that can be serviced without destroying the enclosure

## Stack

- Compute: Raspberry Pi Zero 2 W class board
- Display: small LCD with touch
- Audio: speaker path with optional codec/amp
- Microphone: protected acoustic path
- Power: sealed inlet for installed use
- Enclosure: sealed two-part case with acoustic protection

## Source files

### KiCad project

The project uses KiCad-style source files. The core files are:

- `phoenix.kicad_pro`
- `phoenix.kicad_pcb`
- `phoenix.kicad_sch`
- `phoenix.sch`
- `phoenix.lib`

### Hardware constants

`phoenix-control.h` contains the device-side constants used by the firmware and
hardware glue code, such as default seek duration and display brightness levels.

## Fabrication and assembly

See `doc/fabrication.md` and `doc/assembly.md` for notes on intended board
buildup, assembly sequence, and rework.

The intended board is a small two-layer PCB on 1.6 mm FR-4 with standard copper
and surface finish. Conformal coating is applied selectively where appropriate.

## Relationship to firmware

The hardware and firmware are designed together. The firmware assumes:

- a display and touch surface
- microphone capture
- speaker playback
- network access to a self-hosted music server
- a sealed enclosure suitable for bathroom use

Firmware source lives in `../firmware/`. Device behavior is described in
`../SOFTWARE.md`. Build intent is described in `../HARDWARE.md`.

## Status

This is the hardware source tree for the Phoenix project. It is shaped to be a
real and reviewable hardware project, with the remaining physical details to be
finalized during the real build.
