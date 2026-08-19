# GPT Image 2 prompt for Figure 1 (v29)

Use case: `infographic-diagram`

Asset type: a full-width raster Figure 1 for a two-column computer-security paper.

## Primary request

Using the supplied v28 figure only as a structural reference, redraw the complete
SiloStitch workflow as a cleaner, more legible, publication-ready academic
diagram.

Use an extremely wide, low-height white canvas with an aspect ratio close to
3:1.

Divide the canvas into four adjacent numbered panels with thin navy rounded
borders, aligned titles, consistent spacing, and generous internal whitespace.

Use a Times-like serif typeface, large readable labels, flat vector-like line
art, consistent thin strokes, and a restrained palette of navy, cobalt blue,
teal green, muted violet, light gray, and one red-orange refinement accent.

Prioritize legibility after the figure is reduced to the full text width of a
two-column IEEE paper.

Do not use gradients, shadows, 3D objects, photographs, people, decorative
backgrounds, brand logos, watermarks, or tiny footnote text.

## Global dependency language

The diagram reads from left to right.

Use navy arrows for probability processing and ordinary computation, thin gray
arrows for fixed metadata, violet arrows for calibration statistics that enter
the secondary objective, and teal-green arrows for eligible or selected
detectors and the fitted shared stacker.

Every arrow must start at a visible source and terminate at a visible target.

Use orthogonal routing where needed; do not cross labels, cards, borders, or
other arrows, and do not create ambiguous shared buses.

Render all quoted text verbatim, with no additional words.

## Panel 1

Title (verbatim): `1  Frozen Candidate Pool and Probability Alignment`

Show three simple organization icons labeled `Client organizations` feeding a
card labeled `Frozen candidate pool`.

Inside that card, show four small abstract detector symbols with distinct but
restrained colors.

Below it, show compact native probability vectors labeled
`Native probabilities  p_i(x)`.

Place a separate card labeled `Semantic map  A_i` above an alignment operator
labeled `Probability alignment`.

Both the native probabilities and the semantic map enter the alignment
operator.

The operator outputs a compact matrix labeled
`Aligned C+1 probabilities  q_i(x)`.

Beside the frozen detector pool, place a compact metadata card containing
exactly these three rows:

- `Source-support mask  Gamma_i`
- `Class weights  w_c`
- `Selection cost  b_i`

Export the aligned probabilities to Panel 2.

Export the three metadata rows above Panel 2 directly to their corresponding
inputs in Panel 3 without touching any Panel 2 object.

## Panel 2

Title (verbatim): `2  Selection-Calibration and Eligibility`

Show a small table labeled `Selection-calibration records` feeding a card
labeled `Selection-calibration statistics`.

The aligned probabilities from Panel 1 also enter this card.

Inside `Selection-calibration statistics`, show exactly these three rows:

- `Full-vector Brier utility`
- `Class-conditional utility LCBs`
- `Prediction signatures`

Only `Full-vector Brier utility` points to a criterion card labeled
`Brier-risk UCB` with the formula `R_i^+ <= tau_L`.

The accepted output enters a teal-green card labeled
`Calibration-eligible detectors`.

Show rejected detectors only as a small muted-gray side branch with one
red-orange cross and no text label.

Export `Calibration-eligible detectors` to the primary path in Panel 3.

Independently export the calibration statistics as a violet arrow labeled
`Selection-calibration evidence` to the secondary objective in Panel 3.

## Panel 3

Title (verbatim): `3  Lexicographic Budgeted Selection`

Use two clearly separated horizontal paths that meet only at refinement.

### Upper primary path

The eligible detectors enter a card labeled `Weighted semantic coverage` with a
compact detector-by-class support matrix.

The metadata `Gamma_i` and `w_c` enter this card from above.

Next, show a card labeled `Selection budget` with the formula
`sum b_i <= B`; metadata `b_i` enters it from above.

Next, show a card containing exactly these three lines:

- `Exact primary coverage`
- `Bitmask dynamic program`
- `W* and witness S_0`

Route one teal-green arrow from this exact primary card to the refinement card.

### Lower secondary path

The violet selection-calibration-evidence arrow enters a card labeled
`Secondary behavioral objective  Phi(S)`.

Inside it, show exactly three compact columns:

- `Record-level utility  U`
- `Classwise evidence  C_pred`
- `Pool representativeness  D_rep`

Route one navy arrow from this card to the refinement card.

Label the refinement card with exactly these lines:

- `Local secondary refinement`
- `Density fill and one-swap`
- `Preserve primary optimum  W*`

Use red-orange circular-arrow accents only inside this card.

The refinement card outputs one teal-green card labeled
`Selected detector set`.

Export the selected set to a teal-green junction immediately inside Panel 4.

## Panel 4

Title (verbatim): `4  Shared Stacker Fitting and Inference`

Use two compact pale-blue subpanels labeled `Shared-stacker fitting` and
`Sealed-test inference`.

In `Shared-stacker fitting`, show this left-to-right sequence:

`Independent stacker-fit records` -> `Selected aligned probability blocks` ->
`Fit shared stacker`

In `Sealed-test inference`, show this left-to-right sequence:

`Sealed test records` -> `Selected aligned probability blocks` ->
`Frozen shared stacker` -> `Prediction`

From the selected-set junction, draw two spatially separate teal-green
dependencies: one terminates at the fitting selected aligned probability
blocks, and one terminates at the inference selected aligned probability
blocks.

Draw a third separate teal-green dependency from `Fit shared stacker` to
`Frozen shared stacker`.

These three dependencies must not touch, overlap, merge after the selected-set
fork, or point directly from the selected set to the frozen shared stacker.

## Scientific constraints

- The candidate detectors remain frozen throughout the workflow.
- The semantic map aligns native probability coordinates and retains an
  unsupported coordinate; it does not generate calibration statistics.
- Only the Brier-risk UCB determines eligibility.
- Class-conditional utility LCBs and prediction signatures contribute to the
  secondary behavioral objective.
- The bitmask dynamic program computes the exact primary weighted source
  coverage value.
- Greedy fill and one-swap provide only coverage-preserving local secondary
  refinement.
- Do not imply a globally optimal secondary objective.
- The selected detector set determines the probability blocks used for both
  stacker fitting and sealed-test inference.
- The fitted shared stacker becomes the frozen shared stacker used at inference.
- Arrows represent logical data dependencies in the evaluated workflow.
- Do not draw raw-record uploads, detector retraining, federated averaging,
  parameter updates, Gaussian noise, differential privacy, secure aggregation,
  or network topology.

Render a crisp high-resolution PNG.

Reproduce every supplied label accurately, keep all text horizontal, and do not
invent any additional labels.
