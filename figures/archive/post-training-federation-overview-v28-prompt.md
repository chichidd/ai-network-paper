# GPT Image 2 prompt for Figure 1 (v28)

Use case: `infographic-diagram`

Asset type: a full-width raster Figure 1 for a two-column computer-security paper.

Create a compact, publication-ready overview of the complete SiloStitch method. Use a very wide, low-height white canvas with an aspect ratio close to 3:1. Use four adjacent numbered panels with thin cobalt-blue rounded borders. Let every border hug its contents, keep narrow and even gaps, and use almost all available canvas space. Use Times-like serif text, restrained flat 2D line logos, and consistent thin strokes. Do not use gradients, shadows, 3D objects, photographs, characters, watermarks, SVG, or brand logos.

The whole figure reads from left to right. Use dark navy arrows for ordinary computation and metadata, green arrows for eligible or selected objects and the trained stacker, purple arrows only for calibration evidence entering the secondary score, and red-orange marks only inside the local-refinement card. Every arrow begins at a visible source border or port, and every arrowhead touches its intended target. No arrow ends in whitespace, crosses text, crosses another arrow, travels behind a card, or forms an ambiguous shared bus.

## Panel 1: `1  Frozen Pool and Alignment`

- At upper left, show three generic organization icons labeled `Clients 1 ... J`.
- Point one short navy arrow to a card labeled `Frozen candidates` containing four reusable detector logos: a green tree, a purple connected-node model, a red rule grid, and a cyan bar model.
- From the frozen candidates, expose native detector probabilities `p_i(x)`. Show three compact native-output plots in the corresponding detector colors under the label `Native outputs`.
- Place a separate card labeled `Map A_i` above an `Align` logo.
- Both the native probabilities and `Map A_i` must enter `Align`: native probabilities enter its left edge, while `Map A_i` enters its top edge.
- Point `Align` to a compact matrix labeled `C+1 outputs`, and export one navy arrow labeled `aligned q_i(x)` from that matrix to Panel 2.
- Beside the frozen candidates, place one compact `Selection metadata` card containing `A_i-mapped support Gamma_i`, `Weights w_c`, and `Cost b_i`.
- Export one thin black metadata bus from this card. Route it above Panel 2 without touching any Panel 2 object. Continue it into Panel 3, where `Gamma_i, w_c` feed the support matrix and `b_i` feeds the budget gauge.

## Panel 2: `2  Calibration Eligibility`

- Place a small table labeled `Calibration records` above a card labeled `Evidence`.
- Draw a separate downward navy arrow from `Calibration records` to `Evidence`.
- Let the incoming `aligned q_i(x)` arrow enter the left edge of `Evidence`.
- Inside `Evidence`, show three icon-led rows labeled `Brier utility`, `Class LCBs`, and `Signatures`.
- Only the Brier row sends a navy arrow labeled `risk UCB` to a gauge card labeled `Risk gate`, with the condition `R_i^+ <= tau_L`.
- Split the gate output into a green `Eligible pool` card and a gray `Excluded` card with one restrained red cross.
- Export one short green arrow labeled `eligible pool` from the eligible card to Panel 3.
- Independently, export one purple bottom arrow labeled `calibration evidence` from the Evidence card to the secondary-score card in Panel 3. Class LCBs and Signatures do not enter the risk gate.

## Panel 3: `3  Coverage-First Selection`

Use two vertically separated paths that meet only at refinement.

Upper primary path:

- The incoming eligible-pool arrow enters the support-matrix stage.
- Show a detector-by-class `Support matrix` receiving `Gamma_i, w_c` from the metadata bus above.
- Point the matrix to a `Budget gauge` receiving `b_i` from above and displaying `sum b_i <= B`.
- Point the gauge to a card labeled `Exact maximum coverage`, `Bitmask dynamic program`, and `W* + witness S_0`.
- Draw one green orthogonal arrow from this card to the top edge of `Refine`.

Lower secondary path:

- The purple calibration-evidence arrow enters one blue-violet card labeled `Secondary score Phi`.
- Inside it, show exactly three consistent logos representing `U`, `C_pred`, and `D_rep`.
- Point this card directly to the left edge of `Refine`.
- Label the refinement card `Refine`, `fill + one-swap`, `eligible; within B`, and `preserve W*`.
- Point `Refine` to one green selected-detector card.
- Export one green right-facing arrow labeled `selected set` from that card to a green junction just inside Panel 4.

## Panel 4: `4  Shared Stacker and Inference`

- Use two compact pale-blue subcards, `Training` above and `Inference` below. Do not place a horizontal divider across the panel.
- Keep black computation paths inside each subcard.
- Training path: `Fit records` table -> Training `Selected blocks` matrix -> `Fit shared stacker`.
- Inference path: `Test records` table -> Inference `Selected blocks` matrix -> `Frozen stacker` -> `Prediction`.

Draw exactly three spatially separate green dependencies:

1. From the selected-set junction, route one orthogonal branch upward through the far-left gutter and then right. Its arrowhead touches the left border of the Training `Selected blocks` matrix.
2. From the same junction, route a second branch downward through the far-left gutter, right through the bottom gutter, and then upward. Its arrowhead touches the bottom border center of the Inference `Selected blocks` matrix. It stops there.
3. From the bottom edge center of `Fit shared stacker`, route a separate line downward through the far-right gutter, left until aligned with `Frozen stacker`, and then downward. Its arrowhead touches the top border center of `Frozen stacker`.

These three green edges never touch, cross, overlap, or share a segment after the selected-set fork. In particular, do not draw `selected set -> Frozen stacker`, `Training Selected blocks -> Inference Selected blocks`, or any merged green line.

## Scientific constraints

- The detectors remain unchanged throughout.
- The semantic map aligns native probability coordinates; it does not create calibration evidence by itself.
- Only the Brier risk UCB controls calibration eligibility.
- Class LCBs and prediction signatures contribute to the secondary score.
- The bitmask dynamic program computes exact primary weighted support coverage, whereas fill plus one-swap is only a coverage-preserving local secondary refinement.
- The selected set determines both training and inference probability blocks.
- The fitted shared stacker becomes the frozen stacker used for inference.
- Arrows depict logical dependencies in the centralized implementation, not implemented network messages.
- Do not draw differential privacy, Gaussian noise, raw-record uploads, federated averaging, parameter updates, secure aggregation, detector retraining, or a global-secondary-optimum claim.

Render as a crisp high-resolution PNG. Reproduce every supplied label accurately and do not invent additional labels.
