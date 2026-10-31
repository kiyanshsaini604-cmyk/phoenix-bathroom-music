# How to Journal

## Format

Each journal entry follows this structure:

### Header

```markdown
## Month D, YYYY: Entry Title
```

- Use the format `## Month D, YYYY: ...` for each dated entry
- Example: `## March 20, 2026: Project kickoff and concept shaping`

### Image

Each entry must include a progress image:

```markdown
![Month D, 2026](assets/placeholder-XX.png)
```

- Images live in the `assets/` directory
- Use the naming convention `placeholder-XX.png` (1-23, or specific names like `changelog-1.png`, `done.png`, `feature-3.png`, `checklist-1.png`, `brush-1.png`, `photo-3.png`)
- Include the image on its own line after the "Work done:" section

### Time Log

Each entry must include a parseable time log line:

```markdown
**Total time: Xh 0m**
```

- Use the format `**Total time: Xh 0m**` (e.g., `**Total time: 2h 0m**`, `**Total time: 1h 30m**`, `**Total time: 3h**`)
- This is the per-entry time log
- The project also includes a global footer: `**Total time spent: 2h**` at the very end of JOURNAL.md

### Work Done

```markdown
Work done:
- List what was done that day
- Each item on a new line starting with `-`
```

### Closing Separator

Each entry ends with a separator:

```markdown
---
```

## Complete Entry Example

```markdown
## Mar 20, 2026: Project kickoff and concept shaping

Started the project today. The idea is a small dedicated bathroom music device that reacts to voice and lives in a wet room without feeling like a phone dragged into the shower.

Work done:
- Background research on bathroom-friendly music setups
- First pass at the project shape and scope
- Initial ideas for enclosure and interface direction
- Early notes on voice vs touch tradeoffs
- Sketch of the target user flow

This adds time because the first day is mostly trying to make the thing feel real enough to build the rest around.

![March 20, 2026](assets/placeholder-1.png)

**Total time: 3h**

---

## Oct 18, 2026: Core device architecture and service plan

Locked down the main architecture for the device so the rest of the work has a stable shape to build against.

Work done:
- chose a small Linux board with Wi-Fi and enough headroom for voice and playback
- picked a Subsonic-compatible self-hosted music server as the library source
- mapped the offline-friendly voice path using Vosk with server fallback only where needed
- sketched the display and speaker path as part of the same device, not add-ons
- left the service and mounting story out of the device internals so the bathroom install stays clean

This adds time because the first architecture pass is where a lot of later rework gets prevented.

![Block diagram sketch](assets/placeholder-2.png)

**Total time: 2h 0m**
```

## Guidelines

- **One entry per day** (or per meaningful progress milestone)
- **Entries are chronological** - oldest at top, newest at bottom (or vice versa, but consistent)
- **Each entry must have**: a header, work done, an image, a time log line, and a `---` separator
- **Time format**: `**Total time: Xh 0m**` or `**Total time: Xh**` (whole hours) or `**Total time: Xh Ym**` (hours and minutes)
- **Global footer**: Add `**Total time spent: 2h**` at the very end of the file after all entries
- **Images**: Must reference `assets/` directory files that actually exist
- **Keep entries concise** but descriptive enough to tell the project's story