# Prompt templates

Fill the angle-bracket fields from the manuscript. Keep every box text verbatim.

## 1. Figure generation prompt (for a drawing assistant)

```text
Write one self-contained Python script (matplotlib + numpy only; no external images, no
random data, no generative imagery) that draws a <framework / study-design> figure for
<journal>. Save vector PDF (pdf.fonttype=42) + 600-dpi PNG, <190> mm wide x <~150> mm high,
bbox_inches='tight', pad_inches=0.02.
This is NOT a new network: never write "proposed", "architecture" or "network".   # evaluation papers

STYLE
- Serif: font.family='serif', font.serif=['STIXGeneral'], mathtext.fontset='stix';
  text >= 7 pt at final size; all symbols in mathtext.
- Shared operations: grey pseudo-3D slabs, 0.6 pt outlines. Only <arm A> (<#0072B2>) and
  <arm B> (<#E69F00>, light 45° hatch) are coloured. No red/green, gradients, shadows, icons.
- Thumbnails: grayscale, nearest interpolation, robust 1–99.5 percentile limits, thin frame;
  multichannel data as an offset stack with a bracket label.
- Detail panels: rounded tinted backgrounds (alpha ~0.12).

THUMBNAIL INPUTS (path constants; grey placeholder labelled "thumbnail" if missing)
<NAME> = '<thumbs/....npy>'   # shape, meaning
Do NOT display any output of the compared conditions.

LAYOUT
(a) <overview, left-to-right, numbered steps with exact box texts and connections>
Legend: dashed box, one line: <symbol = meaning; ...>
(b)–(e) <detail panels, exact texts>

STRICT RULES
- Use only the texts above; add no data, numbers, results or effect directions.
- Never write <forbidden words, e.g. "patients">.
- No arrow or colour may imply that one condition is better.
- No text overlap at final width; minimum 7 pt.
REPORT in your reply: smallest font size; <numerical checks>.
```

## 2. Revision block (one per review round)

```text
Revise the script. Keep everything not mentioned unchanged.
CRITICAL (scientific meaning)
1. ...
LAYOUT
2. ...
CARRY-OVER FIXES (not yet applied)
3. ...
GLOBAL: minimum 7 pt at <width>; do not add data, numbers, results or effect directions.
Report: smallest font size; <numerical checks>.
```

## 3. Thumbnail export prompt (for the coding assistant inside the project)

```text
Export illustrative thumbnail arrays for Fig. 1 from ONE example, using the project's
existing pipeline code (do not reimplement).
Example selection (fixed rule, not by appearance): <rule, e.g. same as Supplementary Fig. S1>.
Write to figures/thumbs/ (float32 unless stated), same orientation as <reference display>:
1. <name>.npy — shape (...): <meaning>
...
Also write thumbs_provenance.json: source file, selection rule, seeds, parameters,
shapes/dtypes, SHA256 per file, code version, timestamp, and checks:
<e.g. crop == (map > threshold); mask counts follow the paper's rule; sets disjoint>.
Strict: do NOT load or export any compared outputs or scores; read-only on results;
write only inside figures/thumbs/. Report the checks.
```

Display rule for the drawing assistant when thumbnails arrive:

```text
Before drawing, print each array's shape, dtype, min/max and confirm <checks>.
Paired thumbnails: compute vmin/vmax once and use them for both; print
np.allclose(<A>[<mask>], <B>[<mask>]).
```

## 4. Caption template

```latex
\caption{<Framework title>.
(a) <data and split, with the example's actual counts>. <shared steps use only the input>.
<what feeds both conditions; what applies to one only>. <conditions solved separately with
the same objective at parameter values>; predictions are fixed before scoring. Each endpoint
is reported as <difference definition>; positive values indicate <meaning>.
(b) <detail>. (c) <detail>. (d) <variants and the single step each modifies; caveats>.
(e) <evaluation domains>. <noise / ground-truth caveats>.
Thumbnails are illustrative examples from one <dataset> <slice/sample> selected by a fixed
rule (<Supplementary Section>); no <compared outputs> are shown.}
```

## 5. Cohort / data-flow diagram prompt (optional, supplementary)

```text
CONSORT-style top-to-bottom diagram, <170> mm wide, same style as Fig. 1, greys only.
Columns: <dataset 1> | <dataset 2>; dashed side box for non-participant controls.
Boxes (verbatim): <source> → <grouping> → <sets with counts> → <analyses>.
Thick border: <prespecified confirmation set>.
Grey tags in terminal boxes: "Unit: <unit> · <evidence role>" and "<Fig. X, Table Y>".
Footnote: "<no substitution / exclusion statement>. <units are not patient counts>."
Use only numbers already in the manuscript; quote selection wording exactly.
```
