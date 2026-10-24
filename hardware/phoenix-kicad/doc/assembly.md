# Phoenix assembly notes

This document describes the intended assembly sequence for the Phoenix hardware
source tree. It is a scaffold for the real build, not a finalized shop floor
instruction set.

## Sequence

1. Verify the schematic and PCB match the parts list
2. Identify compute board connector and mounting locations
3. Install the display connector
4. Install the audio interface / codec / amp if used
5. Install the microphone and speaker components
6. Install the sealed power inlet and any panel-mount hardware
7. Install internal hardware: screws, standoffs, and inserts
8. Install acoustic membranes over the mic and speaker openings
9. Apply conformal coating where intended
10. Perform a pre-enclosure functional check
11. Assemble the enclosure and verify sealing

## Pre-enclosure checks

- Confirm the compute board boots headless
- Confirm the display is readable
- Confirm touch input works as expected
- Confirm audio playback and capture paths are present
- Confirm the music client can reach the self-hosted server during development
- Confirm the voice pipeline detects wake and returns a command shape

## Waterproofing checks

- Confirm gaskets or O-rings are seated at the enclosure split line
- Confirm acoustic membranes are in place over openings
- Confirm no exposed connectors remain in the final install
- Confirm cable routing does not create a water path into the enclosure
- Confirm the device does not trap water behind the speaker or mic openings

## Service notes

- Internal hardware should be serviceable without destroying the enclosure
- Conformal coating and potting should be selective, not total
- Acoustic membranes are replaceable where possible
- Power and mounting hardware should be accessible for install rework
