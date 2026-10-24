# Phoenix PCB fabrication notes

This folder contains the scaffold for the Phoenix hardware source. The real
PCB is intended for a compact enclosure that fits around a Raspberry Pi Zero 2 W
class board, a small display, a speaker, a microphone, and a sealed power path.

## Intended stackup

- 1.6 mm FR-4, two-layer board for the main interconnect
- 1 oz copper, standard surface finish
- Conformal coating applied after assembly where appropriate

## Design intent

- Keep the board small and serviceable
- Separate audio and digital paths where practical
- Provide mounting holes that align with the enclosure drilling/mounting plan
- Leave room for the display, speaker, and microphone in the enclosure layout

## Assembly notes

- Verify orientation of the compute board connector before soldering
- Check mic and speaker polarities against the schematic
- Verify that acoustic membranes are installed before testing with water present
- Verify panel-mount connector fit before final enclosure assembly

## Rework

- Keep heat shrinks and connectors accessible
- Do not pot parts that may need later service
- Conformal coat selectively rather than everywhere
