# paper-framework-figure

A Claude skill for designing, generating and reviewing publication-quality framework /
study-design figures (Fig. 1 style) for scientific papers.

## What it does

1. Reads the manuscript and classifies the paper (method vs. evaluation) to set framing rules.
2. Refines the framework statement the figure must agree with.
3. Chooses the layout (overview panel + detail panels; symmetric arms for controlled comparisons).
4. Writes a code-only generation prompt (matplotlib; no generative images).
5. Exports real-data thumbnails with a provenance JSON and numerical checks.
6. Runs review rounds with an A/B/C checklist, merged revision blocks, carry-over fixes and
   regression checks.
7. Iterative visualization refinement (core loop): structural pass, text inventory,
   a four-part decision test before visualising, "same idea elsewhere" sweeps, restraint
   and roll-back when a visual makes the figure worse, regression and number checks.
8. Finalises export, LaTeX placement and a caption that absorbs removed details.

## Layout

```
paper-framework-figure/
├── SKILL.md                     # workflow (stages 0–8)
├── references/
│   ├── visualization_iteration.md  # iterative refinement loop, decision test, worked/failed patterns
│   ├── review_checklist.md      # A/B/C review checklist
│   └── prompt_templates.md      # generation, revision, thumbnail-export, caption, cohort-flow templates
└── assets/
    └── fig_style.py             # shared matplotlib style for the paper's data figures
```

## Install

Copy the `paper-framework-figure/` folder into your skills directory
(e.g. `~/.claude/skills/`), or upload it as a skill in Claude.
