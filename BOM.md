# Phoenix — Bill of Materials

This BOM lists the part classes and example parts for the Phoenix bathroom voice music device. Exact vendors and quantities will change with sourcing; this file exists so the project has a shipped BOM, not because it is locked to one store.

## Summary

| Qty | Part class | Example part | Why |
| --- | --- | --- | --- |
| 1 | Compute board | Raspberry Pi Zero 2 W — https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ | Small Linux board with Wi-Fi, enough headroom for voice, playback, display, and server access |
| 1 | Display + touch | Small SPI touch LCD, smartphone-smaller class — e.g. 3.5" LCD with FT6236 touch hatch | Combined screen and touch input in one part, easy to drive from the board |
| 1 | Speaker | Small waterproof-friendly speaker | Built-in music output loud enough for a bathroom |
| 1 | Amplifier / codec | Small audio amp or codec HAT if the board needs it | Clean audio output and enough drive for the chosen speaker |
| 1 | Microphone | Protected mic or mic array | Voice pickup in a noisy bathroom, with an acoustic membrane over the port |
| 1 | Acoustic membrane / vent | Waterproof acoustic membrane for mic and speaker openings | Keeps water out while still letting sound through |
| 1 | Enclosure material | ASA filament or sheet stock — e.g. Prusament ASA or Polymaker ASA | Bathroom-durable, UV-resistant enclosure material |
| 1 | Sealing parts | Gaskets, O-rings, adhesive seal where needed | Real waterproofing at the enclosure split and openings |
| 1 | Power hardware | Panel-mount sealed power inlet or bulkhead connector | Clean permanent power for the installed device |
| 1 | Mounting hardware | Bracket, suction, or adhesive mount components | Supports more than one mounting style for different bathrooms |
| 1 | Internal hardware | Screws, standoffs, threaded inserts | Serviceable internals without creating extra water paths |
| 1 | Protective finish | Conformal coating or selective potting supplies | Extra protection for vulnerable electronics, without killing serviceability |

## Vendor links

- Compute board: https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/
- Display + touch: small SPI touch LCD, e.g. 3.5" class with FT6236 or similar touch hatch
- Speaker: small waterproof-friendly speaker, sealed or membrane-protected type
- Acoustic membrane / vent: waterproof acoustic membrane, e.g. Gore or equivalent vent cover
- Enclosure material: Prusament ASA — https://prusa.io/3d-printing-materials/asa/ or Polymaker ASA — https://www.polymaker.com/product/polyformer-as
- Power hardware: panel-mount sealed power inlet, e.g. 10 mm or 12 mm bulkhead connector
- Sealing parts: closed-cell foam cord or silicone gasket material for the enclosure split
- Internal hardware: M2.5 or M3 screws, threaded inserts, and standoffs matched to the enclosure and board

## Notes

- This is a direction BOM. Part numbers, vendors, and exact quantities will move as the build gets real.
- The enclosure, sealing, and acoustic protection are treated as first-class parts, not afterthoughts.
- If the board’s built-in audio path is not good enough, budget for a codec or amp stage before locking the enclosure.
- If ASA is unavailable, PETG is a fallback with weaker UV and weather behavior.
- The final installed device should not rely on visible dangling cables or exposed connectors.
