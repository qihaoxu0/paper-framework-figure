---
name: paper-framework-figure
description: Design, generate and iteratively review a publication-quality framework or study-design figure (Fig. 1 style) for a scientific paper, from manuscript text to code-rendered PDF with real-data thumbnails, review checklist and caption.
---

# Paper framework figure

Build the framework / study-design figure of a scientific paper (usually Fig. 1) the way an
experienced author and a picky reviewer would: faithful to the Methods, readable in three
seconds, code-rendered (no generative images), and checked round by round until nothing in
the figure can be misread.

The workflow has nine stages (0–8). Do them in order; stages 6 and 7 loop, and stage 7
(iterative visualization refinement) is where most of the quality comes from — run it until
a full pass changes nothing and the user is satisfied.

Reference files: `references/visualization_iteration.md` (the refinement loop, decision
test, worked and failed conversions), `references/review_checklist.md` (A/B/C checks),
`references/prompt_templates.md` (generation, revision, thumbnail export, caption,
cohort flow), `assets/fig_style.py` (shared style).

## Stage 0 — Read the paper and decide what kind of paper it is

1. Read Abstract, Introduction, Methods and the existing figure captions in full.
2. List every element of the framework that the Methods define: data and splits, shared
   steps, the intervention or model components, estimators, outputs, evaluation endpoints,
   and controls/variants.
3. Classify the paper:
   - **Method paper** (proposes a network/algorithm): an architecture figure is appropriate.
   - **Evaluation / controlled-comparison paper**: never call the figure "proposed",
     "architecture" or "network". Title it e.g. "Controlled comparison framework".
4. Write down the paper's hard constraints before drawing anything (examples: do not show
   results in Fig. 1; repeated observations are not patients; no new experiments or numbers;
   no effect directions implied by colour or arrows).

## Stage 1 — Refine the framework statement

Produce two texts the figure must agree with:
- a **one-sentence version** (for the Introduction or the first line of the caption);
- a **~150-word paragraph** (for the start of the Methods), naming each symbol once and
  stating which step each control/variant changes.

Every element must be traceable to the Methods; add nothing.

## Stage 2 — Choose the figure form

- Default layout for double-column journals (190 mm wide): **top panel (a) overview flow,
  left-to-right; a row of detail panels (b)–(e) below**, each a zoom-in on one step of (a).
- For a controlled comparison, make the two arms **visually symmetric**: one shared trunk,
  two identical arms, one difference highlighted. Symmetry itself communicates control.
- Give the key data path its own visual (e.g. a dashed line for withheld/held-out data that
  runs from the data box to the endpoint it feeds, never near the steps it must not enter).
- Show each output that matters as its own path (e.g. a mask that applies to one arm only
  is drawn feeding that arm only).
- Use a dashed-border legend box (one line) when symbols repeat.

If the user supplies reference figures, list what to borrow from each (e.g. tinted detail
panels, stacked coil thumbnails, pseudo-3D slabs, serif LaTeX typography, bracket
annotations over thumbnails, span arrows labelling stages, a long "global" connection line)
and what must differ for this paper (e.g. no "proposed network" framing, muted colours).

## Stage 3 — Style rules (apply to every figure of the paper)

- Serif font matching LaTeX (`STIXGeneral`, `mathtext.fontset='stix'`); body text >= 7 pt at
  final width; subscripts ideally >= 6 pt (enlarge only subscripted labels if needed).
- Neutral greys for shared operations; colour only the elements that differ (e.g. arm C blue
  `#0072B2`, arm F orange `#E69F00`, Okabe–Ito) and keep those colours identical in all later
  figures. Add a second cue (hatching, marker shape) so grayscale printing still works.
- No red/green "good/bad" semantics, no gradients, shadows, 3D clip-art or icons of people.
- All formulas via mathtext (`$S_C=qH$`, `$\Delta E_{\mathrm{RSS}}$`), same font size as
  neighbouring text.
- Output vector PDF with embedded TrueType fonts (`pdf.fonttype=42`) + 600-dpi PNG,
  `bbox_inches='tight', pad_inches=0.02`.
- `assets/fig_style.py` contains a ready shared style module for the paper's data figures.

## Stage 4 — Write the generation prompt or script spec

Generate the figure **with code** (matplotlib), either directly or by giving another
assistant a precise prompt. Generative image models garble text and many publishers
(e.g. Elsevier) do not allow AI-created images. Use the skeleton in
`references/prompt_templates.md`. The prompt must specify: canvas size, fonts, colours,
every box text verbatim, layout and connections, thumbnail sources, and STRICT RULES
(no added data/numbers/results/effect directions; forbidden words; no reconstruction
outputs in a design figure).

Render first with **grey placeholders** for thumbnails to settle the layout.

## Stage 5 — Real-data thumbnails with provenance

When layout is stable, export thumbnails from the project (see the export prompt in
`references/prompt_templates.md`):
- one example chosen by a **fixed rule**, never by appearance (reuse a rule already stated
  in the supplement if one exists);
- only inputs and intermediate quantities (sampling masks, maps, crops, reference image) —
  never outputs being compared;
- reuse the project's own pipeline functions; read-only on results;
- a provenance JSON: source file, selection rule, seeds, parameters, shapes, SHA256 and
  consistency checks (e.g. mask counts match the paper's rule; crop equals threshold).
Review the JSON against the manuscript before the thumbnails are used (version names,
counts, thresholds). Paired thumbnails that should differ only by one operation must use
**identical intensity limits**, and the script must print a numerical check
(e.g. `np.allclose(C[H], F[H])`).

## Stage 6 — Review round (repeat until clean)

Review every render with `references/review_checklist.md`, in this priority order:
1. **Scientific misreading** — anything that changes what the design appears to be
   (aggregated endpoints, data paths touching forbidden steps, arms merging, missing
   reference links, results shown, causal or "better" cues).
2. **Layout defects** — overlaps, labels far from their objects, clipped elements, broken
   subscripts, asymmetric arrows, inconsistent fonts, text below minimum size.
3. **Polish** — whitespace, line weights, legend spacing.

Rules for each round:
- Report findings as A (must fix) / B (should fix) / C (optional), then give **one merged
  English instruction block** for the drawing assistant.
- Always **carry over unapplied fixes** from the previous round into the new block.
- Check for **regressions** introduced by the last edit (e.g. subscripts broken, line moved
  off-canvas, font sizes changed).
- Ask the drawing assistant to **report numbers** (smallest font size, numerical checks)
  instead of trusting the picture.
- If a screenshot may be cropped, confirm with a full-canvas view before calling something
  clipped.

## Stage 7 — Iterative visualization refinement (the core loop)

This is where a correct figure becomes a good one. Follow
`references/visualization_iteration.md` in full; summary:

1. **Structural pass.** Turn every detail panel that reads like a list of definitions or
   formulas into a structural diagram built from the figure's existing vocabulary
   (sampling strips, slabs, ⊖, arm colours). Long formulas and method numbers move to the
   caption/Methods.
2. **Text inventory pass.** List every remaining text item panel by panel and classify it:
   name · symbol/key formula · needed parameter values · the one core message (all kept,
   shortest form) · explanation or detail (→ caption, or encode structurally) · graphic
   candidate.
3. **Decision test** for each graphic candidate — convert only if all four hold:
   information gain (shows where/what/which that text does not) · legible at final size ·
   net simplification · reuses existing visual vocabulary. Otherwise keep a short phrase
   and **shrink the container**; never fill a large box with glyphs.
4. **"Same idea elsewhere" sweep.** After one successful conversion, audit the whole figure
   for analogous items and report which pass the test and which stay text, with reasons.
5. **Restraint pass.** When a visualised element looks worse (user verdict or own render),
   roll it back at once, keep only parts that carried information, resize the box, and
   record the anti-pattern.
6. **Regression + numbers** after every render (subscripts, formula size, clipping, label
   adjacency, carry-over items applied, reported minimum font, thumbnail checks).

Worked conversions: definition lists → sampling strip + destination boxes; variant
sentences → mini pipeline with tags on the modified step; endpoint formulas → domain-thumbnail
lanes each with its own ⊖; "solved separately" → two coloured lines with separate output
squares; crop in text → crop thumbnail feeding one arm only; long labels → symbols under
objects.
Failed (roll back): icons inside a shared-step box; parameter values as a ruler/slider/bars;
good/bad colour encodings; compared outputs as thumbnails.

## Stage 8 — Finalise

1. Export at final width; report smallest font size and numerical checks.
2. LaTeX: double-column figures use `figure*` with `width=\textwidth`. In single-column
   review layouts where the figure would shrink below legibility, place it on its own
   landscape page (`rotating` package, `sidewaysfigure`) and also upload the PDF as artwork.
3. Rewrite the caption (template in `references/prompt_templates.md`) so it absorbs every
   detail removed from the figure (definitions, counts of the example, what is solved
   separately, what is fixed before scoring, evaluation domains, sign convention, noise
   caveats, thumbnail provenance). Every caption statement must be traceable to Methods.
4. Update text that refers to the figure (e.g. an Introduction sentence describing panels
   that no longer exist).
5. Keep the script, thumbnails and provenance JSON in the submission folder.

## Optional companions

- **Cohort / data-flow diagram** (CONSORT style, usually supplementary): only numbers already
  in the manuscript; observation unit and evidence role tags; thick border for the
  prespecified confirmation set; quote the manuscript's exact wording for selection rules;
  add "Fig. X / Table Y" reference tags to terminal boxes.
- **Data figures**: reuse `assets/fig_style.py`; read original-precision CSVs and cross-check
  them against the manuscript tables, stopping on mismatch rather than plotting.
