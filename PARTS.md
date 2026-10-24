# Phoenix — Parts and Materials Direction

## 1. How to read this file

This is a parts direction list, not a final bill of materials locked to one vendor. The goal is to define the classes of parts needed and the reasoning behind each choice. Exact part numbers can change during sourcing.

## 2. Compute board

Class:

- small Linux board with Wi-Fi

Example direction:

- Raspberry Pi Zero 2 W or a comparable compact board

Selection criteria:

- small form factor
- Wi-Fi for server access
- enough compute for voice, playback, and display
- available audio and display interfaces
- easy to source and develop on

If the board’s audio path is weak, plan to add a codec, HAT, or external audio module.

## 3. Display

Class:

- small LCD with a simple interface

Example direction:

- small SPI-driven LCD in the smartphone-smaller or sub-smartphone range

Selection criteria:

- easy to drive from the main board
- enough resolution for simple UI and abstract visuals
- small enough to stay integrated in the enclosure
- low enough power and complexity for a compact device

The display should be recessed or shielded so it does not become the weakest waterproof point.

## 4. Speaker

Class:

- small built-in speaker with adequate output for a bathroom

Selection criteria:

- audible over shower noise
- fits the enclosure and acoustic opening
- compatible with the amp/codec path
- acceptable sound for casual music playback

Speaker and enclosure volume should be designed together. A good speaker in a bad box still sounds bad.

## 5. Microphone

Class:

- mic or mic array suitable for voice pickup in a noisy room

Selection criteria:

- good voice pickup
- protected acoustic path
- fits the enclosure geometry
- not exposed to direct water spray

A waterproof acoustic membrane or vent over the mic port is a strong idea for a bathroom device.

## 6. Audio interface / amp

Class:

- audio codec, DAC, or small amplifier if the main board needs help

Selection criteria:

- clean enough audio output
- can drive the chosen speaker
- manageable power and thermal needs
- easy to integrate mechanically

## 7. Enclosure material

Primary direction:

- ASA for the final enclosure if printability and bathroom durability both matter

Fallback direction:

- PETG if ASA is not available, with the understanding that UV and long-term weatherability are weaker

Notes:

- the enclosure should not rely on the printed material alone for waterproofing
- sealing, membranes, and geometry are the real waterproofing work

## 8. Sealing and acoustic protection

Class:

- gaskets, o-rings, acoustic membranes, vent covers, adhesive sealing where needed

Selection criteria:

- maintains sound transmission where needed
- blocks water ingress at openings
- fits the enclosure design
- reliable over time in humidity

This is one of the most important part groups because it determines whether the device can live in a wet room.

## 9. Power

Class:

- wired power for the final bathroom install
- sealed inlet or panel-mount connector if the device is installed permanently
- battery only for development or portable testing

Selection criteria:

- clean, safe power path
- no exposed connectors in the final install
- manageable cable routing
- charging path if battery is used during development

The final device should not look like it has a dangling USB cable in the shower.

## 10. Mounting hardware

Class:

- bracket, suction, adhesive, or other mounting option depending on install surface

Selection criteria:

- works on common bathroom surfaces
- holds the device securely
- does not create a water trap
- works with the enclosure geometry

The device should support more than one mounting style if possible, since bathrooms vary.

## 11. Fasteners and internals

Class:

- screws, inserts, standoffs, and other internal hardware

Selection criteria:

- allow the enclosure to be opened for service
- hold the internals securely
- do not create unnecessary water paths
- work with the chosen enclosure material

## 12. Protective finishes

Class:

- conformal coating, potting, or similar protection for the electronics where appropriate

Selection criteria:

- protect vulnerable parts without making future service impossible
- used selectively, not as a substitute for good enclosure design

## 13. Sourcing priority

Priority order:

1. compute board
2. display
3. speaker and amp/codec
4. microphone
5. enclosure material and sealing parts
6. power hardware
7. mounting hardware

This order reflects what drives the rest of the project. The enclosure, sealing, and mechanical fit should be planned around the electronics, not chosen first and forced later.

## 14. What is intentionally not specified

This file does not lock exact vendor SKUs, exact enclosure dimensions, exact speaker size, or exact software libraries. Those decisions should come from what is available, what fits the enclosure, and what the builder wants to use.

The one thing this file does assert is the overall direction: compact Linux device, small integrated display, built-in speaker, protected mic, sealed bathroom enclosure, and a self-hosted music server as the source.
