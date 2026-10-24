# Phoenix PCB fabrication notes

This document describes the intended fabrication approach for the Phoenix hardware
source tree.

## Board approach

The Phoenix hardware is a compact board set intended to fit a bathroom music device.
The main interconnect board is a two-layer PCB built around a Raspberry Pi Zero 2 W
class compute board, a small display + touch path, a speaker output path, a
microphone input path, and a sealed power inlet.

The board is not intended to be a generic breakout. It should be designed so the
enclosure, display, speaker, microphone, and power path can all be integrated
cleanly.

## Intended stackup

- 1.6 mm FR-4
- two-layer board for the main interconnect
- 1 oz copper
- standard surface finish
- selective conformal coating after assembly where appropriate

## Mechanical intent

- Keep the board small enough to fit the enclosure
- Provide mounting holes that align with the enclosure drilling and mounting plan
- Leave room for the display window, speaker port, and microphone port
- Keep the acoustic openings deliberate and protected
- Keep service loops and connectors accessible where rework is likely

## Design intent

- Separate audio and digital paths where practical
- Keep sensitive audio paths away from noisy digital lines where possible
- Make the main connectors oriented and accessible for assembly and service
- Design the power path so there is no exposed connector in the final install
- Treat acoustic protection as part of the electrical design, not just the enclosure

## Assembly considerations

- Verify compute board connector orientation before soldering
- Check microphone and speaker polarities against the schematic
- Install acoustic membranes before any water-adjacent testing
- Verify panel-mount connector fit before final enclosure assembly
- Confirm the main board mounts cleanly before potting or coating critical sections

## Rework

- Keep heat shrink and connectors accessible
- Do not pot parts that may need later service
- Apply conformal coating selectively rather than everywhere
- Make sure the sealed power inlet remains serviceable at the enclosure level
