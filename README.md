# Kanz Carousels

Reusable visual production libraries for Explainers, Books, Websites and Infographics: editable HTML layouts, finished examples, fonts and artwork.

**Use Codex only.** Open this repository in Codex and start with [START-HERE.md](START-HERE.md), [AGENTS.md](AGENTS.md) and the selected library's `HOW-TO.md`; no Claude or Claude plugin is required for this carousel workflow. The Markdown guides cover production and review; supply separately approved copy and source images.

## First run

For optional drafting, [WRITING.md](WRITING.md) contains plain, generic guidance only. Obtain copy approval before rendering; no personal Arabic writing style or formulas are included.

Install Python 3.11+ and the browser renderer:

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium
python render.py libraries/explainer/layouts/explainer-01.html --output exports/example
```

Open `libraries/<lane>/index.html` to browse a library. For a new carousel, duplicate the complete chosen library under `work/<English Title>/` so its relative image/font links stay intact, then edit copies of the layouts and render them in reading order.

## Included libraries

| Library | Guide | Editable layouts |
| --- | --- | --- |
| Explainers | [HOW-TO](libraries/explainer/HOW-TO.md) | 5 |
| Books | [HOW-TO](libraries/books/HOW-TO.md) | 5 |
| Websites | [HOW-TO](libraries/websites/HOW-TO.md) | 4 |
| Infographics | [HOW-TO](libraries/infographics/HOW-TO.md) | 4 |

These are the four reviewed handover source packs, with a renderer and starting instructions. Finished examples are visual references, not approval to publish them unchanged. Hany and the separate news-production system are outside this repository.

## Access and privacy

Keep this repository private. It includes branded assets and fonts; source credits are retained inside each library and no blanket redistribution licence is granted. No API key is needed to render supplied local layouts; Codex needs the operator's own account/access. Private Arabic writing prompts, voice formulas, account credentials and customer data are excluded. Finished Arabic example copy remains as part of the designs.

Video production is separate: [Kanz Motion](https://github.com/yasserr98/kanz-motion) uses Claude with the Codex plugin for the agreed operator workflow.
