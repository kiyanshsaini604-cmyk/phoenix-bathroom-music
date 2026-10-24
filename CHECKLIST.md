# Phoenix — Project Readiness Checklist

Use this as a quick self-check before publishing the project.

## Concept
- [ ] The project has a clear device idea: bathroom voice music device
- [ ] The source of music is clearly defined: self-hosted library via Airsonic-Advanced or Navidrome
- [ ] Voice control is clearly defined: local wake word + Vosk, with server fallback where needed

## Documentation
- [ ] `README.md` explains what the device does and why it exists
- [ ] `SPEC.md` captures the full design intent
- [ ] `HARDWARE.md` covers enclosure, sealing, audio, mic, power, and mounting
- [ ] `SOFTWARE.md` covers startup, audio, voice, music client, visuals, touch, and config
- [ ] `PARTS.md` gives parts direction rather than a fake final order
- [ ] `BOM.md` gives a shipped bill of materials

## Assets
- [ ] README includes images or diagrams
- [ ] Journal entries include progress images
- [ ] Editable diagram files are present in `assets/`

## Build story
- [ ] The journal shows a believable progression from concept to readiness
- [ ] Journal entries log time in a parseable format
- [ ] The project describes what is left for real physical assembly

## Presentation
- [ ] The project reads as one coherent device, not scattered notes
- [ ] The waterproofing and bathroom-use story is coherent
- [ ] Voice, touch, playback, and visuals all have a defined role

## Final check
- [ ] A reviewer can tell what was built, how it works, and what files exist
- [ ] The repo presents the project as finished enough to ship
