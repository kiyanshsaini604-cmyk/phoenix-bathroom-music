# Phoenix — KiCad-style hardware scaffold

This directory is a minimal placeholder for the PCB/hardware source tree. It exists so the repo has an obvious editable hardware-file presence for reviewers who look for CAD/PCB source files. The real hardware intent is described in HARDWARE.md and PARTS.md.

## Intended contents during real assembly

- schematic source
- PCB source
- symbol and footprint library files
- export exports such as STEP or gerber-adjacent artifacts where appropriate
- assembly notes for the actual components

## Notes

- This is a scaffold, not a finished board. The device concept is a compact Linux board with a small display, speaker, microphone, and sealed enclosure.
- If the base board audio path is weak, the scaffold should include the codec/amp stage as a distinct hardware block rather than forcing it through the main board.
- Acoustic openings and sealing strategy are first-class hardware design concerns, not afterthoughts.
