# Phoenix hardware summary

This is a scaffold for the Phoenix hardware source tree. The project intent is
a compact bathroom voice music device with a self-hosted music library source,
local-first voice control, built-in speaker, protected microphone, small
display + touch, and a sealed enclosure.

## Core blocks

- Compute board: Raspberry Pi Zero 2 W class
- Display: small LCD with touch
- Audio: speaker path with optional codec/amp
- Microphone: protected acoustic path with membrane
- Power: sealed inlet for the installed device
- Enclosure: sealed two-part case with acoustic protection

## Source files in this folder

- `phoenix.sch` — schematic source
- `phoenix.lib` — project symbol library
- `phoenix.kicad_pro` — KiCad project file
- `phoenix.kicad_pcb` — PCB source
- `phoenix.kicad_sch` — KiCad schematic source
- `phoenix-control.h` — device-side hardware constants
- `doc/fabrication.md` — fabrication notes
- `doc/assembly.md` — assembly notes

## What is still left for real assembly

- Final enclosure dimensions and internal layout
- Exact component selection
- Final sealing and acoustic membrane choices
- Final PCB routing if a custom board is built
- Final enclosure fabrication and install tuning
