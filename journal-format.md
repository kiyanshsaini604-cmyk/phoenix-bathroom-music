# Journal Format Specification

## Entry Structure

Each journal entry follows this exact structure:

```markdown
## Month D, YYYY: Entry Title

Work done:
- Description of work item 1
- Description of work item 2
- (additional items as needed)

![Month D, 2026](assets/filename.png)

**Total time: Xh 0m** or **Total time: Xh** or **Total time: Xh Ym**

---
```

## Required Components Per Entry

1. **Header line**: `## Month D, YYYY: Entry Title`
   - Month can be abbreviated (Jan, Feb, Mar, etc.) or full (January, February, March, etc.)
   - Day is 1-31 with ordinal suffix optional
   - Year is 4 digits
   - Colon after title, then space before description

2. **Work done section**: 
   ```markdown
   Work done:
   - List accomplishments for that session
   ```
   - Minimum 1 item, reasonable maximum 10-15 items
   - Each item starts with `- ` (dash space)

3. **Image**:
   ```markdown
   ![Month D, 2026](assets/filename.png)
   ```
   - Must reference a file that exists in `assets/`
   - Recommended naming: `placeholder-XX.png` (1-23) or specific names
   - Image should be on its own line

4. **Time log**:
   ```markdown
   **Total time: Xh 0m**
   ```
   - Format: `**Total time:**` followed by space, then `Xh 0m` or `Xh` or `Xh Ym`
   - `X` is a positive integer (hours)
   - Optional `0m` for zero minutes (required for parseability)
   - Optional `Ym` for additional minutes if needed
   - Example valid: `**Total time: 2h 0m**`, `**Total time: 1h 30m**`, `**Total time: 3h**`

5. **Separator**:
   ```markdown
   ---
   ```
   - Three dashes on their own line
   - Marks end of entry, start of next entry

## Global Footer

After all entries, the file must include:

```markdown
**Total time spent: 2h**
```

- This is the global total time spent on the entire project
- Placed at the very end of JOURNAL.md, after the last `---` separator
- Format: `**Total time spent: 2h**` (with bold markdown)

## Formatting Rules

- **One entry per dated header** - no duplicate dates
- **Entries are sequential** - use consecutive dates or clearly mark gaps
- **Images must exist** - every `![...](assets/...)` reference must have a corresponding file in `assets/`
- **Time lines must be parseable** - the `**Total time:**` pattern must match the regex `Total time[,:\s]*([0-9]+\s*(?:h|hr|hours)?\s*(?:m|min|minutes)?)`
- **No orphaned content** - every entry must have all 5 components (header, work, image, time, separator)
- **Consistent style** - same formatting conventions throughout the file

## Example Entry

```markdown
## Oct 23, 2026: Music client and Subsonic integration

Work done:
- built the music client around the Subsonic-compatible API
- added search and playback request handling
- wired the client into the device config for server address and auth
- left the client tests covering the happy and error paths

![Music client sketch](assets/placeholder-7.png)

**Total time: 2h 0m**

---
```

## Invalid Entry Examples

❌ Missing time line:
```markdown
## June 7, 2026: Reliability check

Work done:
- rechecked startup recovery

---
```

❌ Wrong time format:
```markdown
**Total time: 2h**  (missing "0m" - this project requires parseable format with minutes)
```

❌ Missing image:
```markdown
## June 7, 2026: Reliability check

Work done:
- rechecked startup recovery

**Total time: 2h 0m**

---
```

❌ Missing work done:
```markdown
## June 7, 2026: Reliability check

![health recheck](assets/state-flow.png)

**Total time: 2h 0m**

---
```

## Valid Entry Count Verification

For the phoenix-bathroom-music project:
- **32 total entries** expected
- **32/32** must have images referencing `assets/`
- **32/32** must have `**Total time: 2h 0m**` or similar parseable format
- **32/32** must have `---` separator
- **1 global footer**: `**Total time spent: 2h**` at file end

## Checklist for Each Entry

- [ ] Header starts with `## ` and has date format
- [ ] "Work done:" section with at least 1 item
- [ ] Image line starts with `![` and references `assets/`
- [ ] Time line starts with `**Total time:` and has parseable format
- [ ] `---` separator on its own line after time line
- [ ] Image file actually exists in `assets/` directory