# Four image-first Kanz infographic candidates

Review set, 2026-09-27. Four completed compositions, not yet approved masters.

## Construction

1. **Image group:** a newly generated reference-inspired scene; full-bleed crop; 8% `#38104D` wash; a local contrast veil. `images/` preserves the original generated plates. `exports/*-base.png` includes the wash and veil.
2. **Information group:** real Kanz logo; live Arabic text and numbers; thin rules, callouts and the proportional bar. `A.html`–`D.html` and `poster.css` retain all these elements independently editable. `exports/*-information.png` is a transparent flattened export of this group, not editable text.

Each `*-final.png` combines those two groups at 1080 × 1920. The gallery toggles all four between final, treated image and information-only views. The transparent information layer and treated base can be stacked at identical size/position. The generated originals are 940/941 × 1672 and scaled to the export canvas; do not claim native 1080p photography.

## Fixed brand settings

- Headlines: Thmanyah Display Bold. Supporting Arabic and numerals: IBM Plex Sans Arabic. Never simulate Arabic letter spacing.
- White `#FFFFFF` for principal text; lavender `#D5ADEF` for emphasis and numbers; muted `#EEE6F2` for secondary text.
- Logo: actual asset; never generated. Margins: typically 82–90 px; the window has narrower interior content bounds.
- Common wash: `#38104D`, opacity 0.08. This is a candidate inherited from the liked subtle photo-wash direction, not approval of every new image or local gradient.
- Generated scenes already contain restrained purple grading and fine photographic grain. Do not add another heavy texture automatically.
- Local contrast is separate from the common wash; use soft transitions and preserve visible material detail. Full exact gradients and coordinates are in `poster.css`.

## Four reusable compositions

| Example | Image brief and reference relationship | Information structure | Best future use |
|---|---|---|---|
| A · Window | Reference 1's photographed frame; newly generated cabin window, clouds and wing | One leading metric, two supporting metrics, remainder, takeaway | Industry summaries and a few related statistics |
| B · Ship | Reference 2's narrow central subject and open side columns; new overhead ship scene | Four numbered cost components with delicate connectors | Process, cost components, product journey |
| C · Ice | Reference 3's visual metaphor above explanatory information; new money-in-melting-ice concept | Price comparison, purchasing-power result, proportional bar | Abstract financial concepts with one worked example |
| D · City | Reference 4's integrated skyline and information in the sky; a new fictional city | Matching rows in two columns, then takeaway | Comparisons, before/after, matched scenarios |

## Local contrast recipes

- A: top black veil 22%, middle purple-black 20%, clear lower scene, bottom black 45%. Protect the window's curved rim and wing.
- B: top black 45%, bottom black 65%; left purple-black 38% fading to clear at 42%; clear middle until 60%; right purple-black 40%. Keep the ship unobstructed wherever possible.
- C: top black 35%, clear hero from 18–45%, lower purple-black 22% at 64%, bottom black 50%. Keep ice highlights readable.
- D: top purple-black 32%, 24% at 52%, clear at 70%, bottom black 78%. Preserve the warm horizon and integrated buildings.

These are precise starting values for these four plates. A new image needs its own legibility check; identical opacity is not proof of identical contrast.

## Rules for the next subject

Choose the information structure first, then generate a scene with intentional space for that structure. The image prompt must prohibit text, numbers, logos and charts. Keep real data and hypothetical examples distinct. Preserve source and period beside claims. A scene can be illustrative; a claimed real person or location requires verified reference handling. None of these generated scenes is evidence of an actual event or place.

Do not reuse a statistical bar as decoration. C's bar uses `100/110 = 90.909…%`; B's 01–04 numbers are ordinal labels, not quantities. Do not force icons, tape, paper cards or doodles into these image-first compositions.

## Editable source and reproduction

`build.py` contains the candidate copy and generates four HTML layouts plus the gallery. `poster.css` contains live layout and treatment settings. `render.py` produces three exports per example and verifies fonts, loaded images, text bounds and gallery toggles. `PROMPTS.json` holds the exact four image-generation prompts. The user supplied reference copies are in `references/` for private review only.

No Canva file was created. No social publishing occurred. The next decision is which images, layouts and overlay strengths the user wants to develop.
