# Start here: Codex carousel production

1. Open this repository in Codex. Read `AGENTS.md`, then the selected library's `HOW-TO.md` and `notes/` source-credit files.
2. Supply the approved slide copy, an English content title, chosen library, intended slide order and any replacement photos/screenshots. If a draft is needed first, use only the neutral basics in `WRITING.md` and obtain approval before design; Yasser's private Arabic writing method is excluded.
3. Copy the entire selected library to `work/<English Title>/` and edit its HTML layouts, keeping fonts, artwork and relative paths together. Match the supplied examples; do not invent a new icon style.
4. Render the selected HTML layouts with `render.py`, passing them in reading order; each `.slide` or `.poster` becomes a numbered PNG. Inspect every exported slide at full size and phone size for Arabic joining, text overflow, crop, missing assets and factual/source accuracy.
5. Use genuine screenshots for featured websites, real book covers where available and retain source credits. Do not add decorative page/slide counters.
6. Deliver final numbered slides under the English content title; the Drive folder and Airtable record name must match. Store approved copy and the delivery link in Airtable, use a first-slide preview, and keep review/approval/publication as separate statuses.

## Request to give Codex

“Read AGENTS.md and START-HERE.md. Use the [chosen] library to produce [English Title] from the approved copy I provide. Follow its HOW-TO.md, preserve the visual identity, render the slides and show me the outputs for review.”

Only Codex is required as the assistant for this workflow. Python, Playwright and Chromium are local export dependencies; external account access and publishing approval are separate.

Historical example images may contain old decorative counters; they are removed from the editable layouts and must not be reintroduced.
