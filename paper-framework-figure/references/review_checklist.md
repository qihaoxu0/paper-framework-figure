# Framework figure review checklist

Use on every render. Report as A (must fix) / B (should fix) / C (optional).

## A — Scientific meaning (can mislead a reader or reviewer)

- [ ] The figure shows the design only: no results, effect sizes, effect directions,
      "better/worse" colours, or outputs of the compared conditions.
- [ ] Paper type respected: no "proposed", "architecture", "network" for evaluation papers.
- [ ] Separate outcomes stay separate: one difference operator (e.g. ⊖) per endpoint; no
      line merges several endpoints into one symbol.
- [ ] Compared arms stay visibly separate through every shared step (e.g. two coloured lines
      through one estimator box, each with its own output).
- [ ] Held-out / withheld data path never touches, crosses or runs parallel next to steps it
      must not enter (normalisation, calibration, fitting, selection).
- [ ] Every reference input is connected to every endpoint that uses it — or the endpoint
      label names it (e.g. "HFEN vs. t") when a connecting line would cause clutter.
- [ ] Two lines with different meanings are never within a few pixels of each other.
- [ ] Order of operations is logically correct (parameters and inputs point INTO the step
      that uses them, not after it).
- [ ] Labels give the full role (e.g. input used for "calibration + fitting", not only
      "fitting"; withheld data "scoring only").
- [ ] Paired thumbnails differ only by the intended operation; identical intensity limits;
      numerical check printed.
- [ ] Wording matches the manuscript verbatim for selection rules and cohort statements;
      paraphrases that change meaning are corrected.

## B — Layout and typesetting

- [ ] No overlapping text; no text crossed by lines; labels touch their objects (~1.5 mm).
- [ ] Nothing clipped at the canvas edge; >= 2–3 mm margin for lines and labels.
- [ ] Symmetric, horizontal arrows where the structure is symmetric.
- [ ] Box titles and formulas use consistent line structure (name line, formula line).
- [ ] No awkward line breaks (number split from its unit, single word orphaned).
- [ ] One font family; mathtext subscripts render as subscripts; formula size = label size.
- [ ] Text >= 7 pt at final width (report the smallest size); subscripts not tiny.
- [ ] Boxes sized to their content; no large empty boxes.
- [ ] Cross-panel leader lines do not cross legends or titles (use "→ (b)" tags instead).
- [ ] Panel captions on one line; all detail panels equal height and aligned.
- [ ] Legend on one evenly spaced line; no redundant entries.
- [ ] Hatching/patterns light enough not to dominate.

## C — Polish

- [ ] Tight bounding box; no large bottom/side whitespace.
- [ ] Line weights >= 0.5 pt and consistent.
- [ ] Grayscale print still separates the compared elements.

## Every round

- [ ] Previous round's unapplied fixes carried into the new instruction block.
- [ ] Regressions from the last edit checked (subscripts, positions, sizes, clipping).
- [ ] Drawing assistant asked to report numbers, not just a picture.
- [ ] Caption still matches the figure after changes.
