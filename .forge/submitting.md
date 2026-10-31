# Submitting for Phoenix

This project is a bathroom voice music device that plays from a self-hosted music server by voice request, with onboard screen animations and built-in speakers.

## What belongs in the repo

- `README.md` — project overview, photos/diagrams, and links into the deeper docs
- `JOURNAL.md` — build journal with dated entries and progress photos
- `SPEC.md` — full design spec
- `HARDWARE.md` — hardware and build plan
- `SOFTWARE.md` — software architecture
- `PARTS.md` — parts and materials direction
- `BOM.md` — bill of materials
- `assets/` — screenshots, diagrams, photos, and editable design files

## Submitting checklist

### README
- [x] README has images (6 images covering PCB, schematic/wiring, 3D model, and build photo)
- [x] Bill of Materials is present (BOM table in README.md + BOM.md with vendor links)
- [x] Hardware/PCB/CAD source files are in the repo in editable form (KiCad .kicad_pro/.kicad_pcb/.kicad_sch/.lib, SVG diagrams in assets/, SVG firmware diagrams)

### Journal
- [x]  Devlog entries have images (243/243 entries reference assets/)

- [x]  Journal entries log time in a parseable format (243/243 entries have **Total time: Xh 0m**)


### Project readiness
- [x] The project tells a complete story from concept through build, software, and enclosure
- [x] The repo has enough substance that someone can follow what was built and why

## Verified counts (as of latest commit)

- JOURNAL.md: 243 entries, 243 time lines, 1 total-time footer (**Total time spent: 240h**)
- README.md: 6 images, BOM section present
- BOM.md: vendor links present
- assets/: 216 files, all referenced images exist

## Repo conventions

- Editable design files use common source formats such as SVG.
- Photos and diagrams live in `assets/` and are referenced from the journal and README.
- BOM is a Markdown table in `BOM.md`.
- Build journal is the long-form record of the project in `JOURNAL.md`.
