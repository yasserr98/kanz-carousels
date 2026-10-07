# Kanz / two tactile Assets carousels

Delivered 27 September 2026 for visual selection. Open `index.html` to view two complete sets or compare matching slides. `exports/` contains ten 1080 x 1350 PNGs; `previews/` contains two overview sheets in Arabic reading order. The gallery runs locally.

## Confirmed direction and new candidates

The user selected A1, A2, A3, A4, B4 and C4 in the original study, and the earlier component kit excluding focus corners, step marker, inset fact panel and object stage. On 27 September they endorsed tactile paper and doodled arrows, preferred the original A1 tape size/color, and clarified that the extra elements should come from the earlier component kit.

Tape is restored to **230 x 70 px, #D5ADEF, 90% opacity**. Use `svg/tape-a1-selected.svg`; rotation happens at composition time. The pale/narrow tactile-v2 tape is historical, not the selected tape treatment. Keep the newly selected tactile paper and doodles. This changes the educational template only.

- **P / Paper editorial:** selected A1-A4 composition rhythm, textured paper cards, pencil underline, earlier divider, original tape and F01 closing note.
- **D / Annotated editorial:** deep backgrounds, taped photo/definition, earlier branching connector and offset labels, tactile comparison cards and M01 closing note.

Both full sets and both closings are new review candidates. Rendering does not constitute user approval or publication. The existing supplied Arabic wording and explicit follow/subscribe CTA are preserved. The original sample's literal `:calling:` formatting token remains omitted as in the earlier study. No finance copy was rewritten or independently fact-checked in this design task.

## Editable material

`slides.html` is the editable HTML composition with separate live Arabic text, graphics, photo and wash. The ZIP includes this source, gallery, fonts, assets, SVGs, exports and checks. It can be opened outside the repository. It is not a native Canva master; no Canva creation/import/publication was requested. Typeface and SVG import fidelity in Canva remain untested.

Reusable elements carry the original palette and actual Kanz logo, Thmanyah Display Bold, IBM Plex Sans Arabic, approved grayscale objects and M01/F01 characters. P cover uses the 8% purple photo wash; D cover uses the existing optional edge wash. Texture stays quiet under text. The original four rejected components are absent.

## Verification

All ten slides visually inspected at full size. All three required font faces loaded; zero broken images, out-of-slide text or text-box overlaps. Every supplied copy block is checked on both sets. Gallery controls, local links, mobile overflow and the ZIP are checked separately in `gallery-checks.json`.

Rebuild inside the Kanz repository: `python reports/kanz-tactile-carousels-2026-09-27/build.py`, then `python reports/kanz-tactile-carousels-2026-09-27/render.py`. Building relies on the original Assets study and educational-editorial/tactile-v2 sources; direct editing/rendering of the included `slides.html` does not require those source folders. Playwright/Chromium is required for rendering.

## Provenance

Original study: `reports/kanz-assets-carousel-2026-09-26/`. Selected kit and guideline: `brand/educational-editorial/`. Paper/doodle generator: `brand/educational-editorial/tactile-v2/`. New layouts retain source assets, while paper panels are regenerated at their actual aspect ratios.

Photo: Cairo Skyline by Maher Najm, CC BY 2.0, https://commons.wikimedia.org/wiki/File:Cairo_Skyline.jpg . Cropped, desaturated and tinted; attribution retained. Existing asset/font permissions are unchanged.

Next: user selects preferred slides and closing; combine the chosen pieces into the template. Future missing content roles and any explicitly requested Canva work remain separate.
