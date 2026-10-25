# Iterative visualization refinement (the core loop)

A first render that is *correct* is rarely *good*. The figure becomes publishable through
repeated passes that replace descriptive text with structure and graphics — but only where
a graphic genuinely carries information — and that roll back immediately when a change
makes the whole figure worse. This file is the playbook for that loop. It is the most
important part of the skill: run it after the scientific content and basic layout are
correct, and keep running it until a full pass finds nothing worth changing.

---

## 1. The loop

```
render ─► inventory text ─► classify each item ─► decide (keep / caption / structure / graphic)
   ▲                                                              │
   │                                                              ▼
 check regressions + numbers ◄── one merged revision block ◄── apply decision test
```

One pass =
1. **Render** the current version at final size (190 mm) and look at it as a reader would.
2. **Inventory every piece of text** in the figure, panel by panel (box titles, sub-labels,
   formulas, parameter values, arrow labels, notes, captions inside panels).
3. **Classify** each item (Section 2).
4. **Apply the decision test** (Section 3) to every item marked as a graphic candidate.
5. Write **one merged revision block**: this pass's changes + every unapplied fix from
   earlier passes (carry-over) + regression fixes.
6. After the new render: **check regressions** and **ask for numbers** (Section 6).
7. Ask the user for their visual judgement; if they say a change looks worse, **roll it
   back** (Section 5) and record why.

Stop when a full pass produces no A/B items and the user is satisfied.

---

## 2. Classify every text item

| Class | Examples | Action |
|---|---|---|
| **Name** | "Shared calibration", "RSS NMSE", "Ridge estimator" | Keep, shortest form, one line |
| **Symbol / key formula** | $M$, $U$, $q$, $H$, $S_C=qH$, $\Delta E_{\mathrm{RSS}}$ | Keep, mathtext, same size as labels |
| **Parameter values the reader needs** | $\lambda = 0.003,\ 0.01$ | Keep as one short line |
| **Core message** (one per figure) | "only spatial extent differs" | Keep; shorten if possible |
| **Explanation of how a step works** | "solved separately for C and F", "predictions fixed before scoring", "not used for normalization, calibration, fitting or selection" | Remove from figure → caption, **or** encode structurally if the structure can say it |
| **Definition / detail / number of the method** | ACS indices, $\lceil |V|/4\rceil$, thresholds, σ of a filter, "hard DC retained" | Caption or Methods |
| **Long formula** | full objective function in a box | Methods equation; figure keeps the name |
| **Graphic candidate** | something that is *where/what/which* rather than *how* | Run the decision test |

Typical end state: boxes contain a name (+ one symbol line); detail panels contain
structure and thumbnails, not sentences.

---

## 3. Decision test before turning text into a graphic

Convert an item into a graphic **only if all four answers are yes**:

1. **Information gain** — does the graphic show something the text does not (a location,
   membership, a domain, a one-to-one vs one-to-many relation, a data path)?
2. **Legibility at final size** — will every part (ticks, mini labels, glyph details) still
   be >= 7 pt and recognisable at 190 mm width?
3. **Net simplification** — does the box/panel become calmer and easier to read, not busier?
4. **Vocabulary fit** — does it reuse symbols already in the figure (same strips, same
   slabs, same ⊖, same colours) instead of introducing a new visual language?

If any answer is no: keep a short phrase and **resize the container to the text** — a
near-empty large box is fixed by shrinking it, never by filling it with glyphs.

---

## 4. Proven conversions (worked) and anti-patterns (failed)

### Worked — structure or graphic carries real information

| Before (text) | After (structure / graphic) | Why it works |
|---|---|---|
| Detail panel as a list of definitions ("ACS lines 120–135; $M$: ⌈\|V\|/4⌉ lines; $U$: withheld") | Sampling-line strip (ACS thick dark, $M$ solid, $U$ light dashed) + two boxes "Input $M$ / calibration + fitting" and "$U$ lines / scoring only" | Shows membership and the two destinations at a glance |
| "Variants" panel as three sentences | Mini pipeline (Map input, Estimator, λ choice) with tags pointing to the step each variant changes; the non-equivalent variant in a dashed tag | Shows *which step* each control modifies — the key argument that they are not generic ablations |
| Endpoint panel as five lines of formulas | Three lanes: domain thumbnail → endpoint name → ⊖ → ΔE (reference image for image-domain error; withheld-lines strip for k-space error; LoG-filtered reference for high-frequency error) | Shows *where* each endpoint is computed; text reduced to the endpoint name |
| "solved separately for C and F" inside the estimator box | Two coloured lines passing through the box, each ending in its own empty outlined square "C" / "F" | The structure states the separation; no sentence needed |
| Crop described in text only | Crop thumbnail $H$ drawn feeding **only** the cropped arm, shared direction $q$ feeding both | Makes $S_C=qH$, $S_F=q$ visible |
| Long note along the withheld-data line | "withheld $U$: scoring only" next to a dashed line that visibly avoids the shared steps | The route proves the claim; the label just names it |
| "ACS" text box in the calibration panel | Small strip of the ACS lines in the same style as the data-split panel | Reuses an existing symbol; links the two panels |
| Labels like "y (acquired lines V)", "pre-crop direction q", "U = V \ M" | $y$, $q$, $U$ placed directly under their objects | Symbols + caption definitions are enough |
| Endpoint boxes "HFEN vs. t / LoG, σ = 1.5 px" | "HFEN" (domain shown in the endpoint panel) | Avoids duplicating the detail panel |

### Failed — forced visualisation that made the figure worse (roll back)

| Attempt | Problem | Correct fix |
|---|---|---|
| Three tiny icons inside the "Shared calibration" box (histogram for $s$, ACS strip → $q$, unit circle for phase) | Unreadable at size; fragmented; duplicates the calibration detail panel | Title only, box shrunk to fit; details stay in the detail panel |
| Two parameter values drawn as a mini log-scale ruler | Tiny tick labels, misaligned, invites "continuous sweep / optimum" reading | One line "$\lambda = 0.003,\ 0.01$"; box height reduced |
| Bars or slider for parameter values | Looks like results / suggests tuning | Plain values |
| Coloured "good/bad" encodings for signs | Implies quality | Neutral grey shading for one sign only, labelled by meaning ("F higher error") |
| Reconstruction outputs as thumbnails in a design figure | Readers compare quality; becomes a results figure | Inputs/intermediates only; outlined empty squares for outputs |

Lesson: when the user says a visualised element "doesn't look good", do not defend it.
Revert, shrink the container, and record the pattern here.

---

## 5. Working with the user's visual judgement

- The user's aesthetic verdict is decisive for *how it looks*; the manuscript is decisive
  for *what it says*. Accept "this looks worse" immediately; argue only about scientific
  correctness.
- When reverting, keep any part of the change that carried real information (e.g. the
  one-arm-only crop thumbnail survived while the in-box icons were removed).
- When the user asks "can X be visualised too?", run the decision test explicitly and say
  which items pass and which should stay as text, with the reason.
- After an over-designed round, state the rule you will apply next time (Section 3).

---

## 6. Regression and number checks after every render

Every edit can break something else. After each render check at least:
- **Subscripts and formulas** still mathtext (not "S C = qH", "ΔE RSS").
- **Formula size** equals neighbouring text (not enlarged).
- **Lines** still inside the canvas with margin; key data path unbroken and not crossing
  labels; no new near-parallel lines with different meanings.
- **Labels** still adjacent to their objects after boxes moved or shrank.
- **Carry-over items** from previous blocks actually applied (they are often skipped —
  repeat them verbatim until done).
- **Reported numbers**: smallest font size at final width; numerical checks on thumbnails
  (e.g. paired thumbnails identical inside the mask). Do not accept "fixed" without the
  printed value — a visible mismatch persisted for three rounds until the check was demanded.
- **Screenshot artefacts**: if something looks clipped, request a full-canvas view before
  reporting it.

---

## 7. Order of passes (what to fix when)

1. Scientific meaning (A items) — merged endpoints, data paths, arm separation, missing links.
2. Basic layout — overlaps, clipping, symmetry, label distances.
3. **Structural pass** — turn text-list detail panels into structure using the existing
   vocabulary (Section 4, worked rows 1–3).
4. **Text-to-visual pass** — inventory every remaining text item; convert only items that
   pass the decision test.
5. **Restraint pass** — remove or revert anything that fails legibility or simplification;
   resize containers to content.
6. Typesetting — fonts, mathtext, minimum sizes, subscripts (enlarge only subscripted labels
   if they fall below ~6 pt).
7. Export and numbers — tight bounding box, embedded fonts, reported minimum font and checks.
8. Caption — absorb everything removed in passes 3–5.

---

## 8. Instruction-writing rules for the drawing assistant

- One merged block per round; sections CRITICAL / LAYOUT / VISUAL / CARRY-OVER / GLOBAL.
- Give exact texts, sizes and routes ("vertical spine below the box with two short branches",
  "vertical segment 2 mm right of all ΔE labels").
- Specify what must NOT change ("keep everything not mentioned unchanged").
- For any visual element, state what it must not imply (no bars, no gradient, no slider, no
  red/green).
- End every block with "Report: smallest font size; <numerical checks>".

---

## 9. When a restyled figure still looks plain: change the encoding, not the colours

Recolouring a weak chart (forest plot in grey -> forest plot in colour) does not fix it.
If the user says a figure is still not good after a style pass:
1. State the figure's one message in a sentence (e.g. "RSS improves while U-NMSE worsens").
2. Search related literature for an established visual form that encodes exactly that
   relation, also outside the field. Examples that worked:
   - two-outcome trade-off -> **agreement plane** adapted from the cost-effectiveness /
     benefit-risk plane: one paired difference per axis, quadrants = both better / both
     worse / disagree, each result a 2-D interval cross;
   - sign change across a parameter -> **dumbbell with an arrow** across the zero line;
   - paired effects with units -> estimation plots (effect size with interval, optional
     unit-level points).
3. Reuse that encoding across figures so the paper has one visual language (results
   figures and the reporting-workflow figure share the same plane).
4. Turn a text flowchart of a decision rule into a **mechanism figure**: draw the space in
   which the decision is made (the plane), place schematic examples A-D in each region,
   link them to short action cards, and add a small worked example with the paper's own
   primary result.
5. Keep labels near the origin or in empty regions; show region labels in one panel only;
   avoid hatching inside data panels.
