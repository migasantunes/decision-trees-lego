# ML Challenge Report
> This report contains the group members names, assigned topic, explanation of the model, experimental design, key results and figures, limitations, three practical lessons, contributions of each team member and the AI use in the project. 

## Team Members
- Ricardo Tavares - No. 2026133913
- André Leão - No. 2023210870
- José Antunes - No. 2023211288

## Assigned Topic
Decision Trees with LEGO - Machine Learning Project

## Explanation of the Model

## Experimental Design

<!-- Draft notes by André (Exp. 2). To be rewritten as prose for the final report. -->

**Shared protocol (all experiments)**
- Synthetic LEGO bricks: `stud_rows` (1-2), `stud_cols` (2-10) and `colour` (8 colours, one-hot encoded), matching the physical kits used in the class activity.
- Builder's rule: Accepted if (yellow AND cols >= 4) OR (not yellow AND rows == 2); about 51% of brick types are Accepted.
- N = 300 bricks, stratified 70/30 split (210 train / 90 test), seed 42, entropy criterion.
- Each experiment changes **one** aspect relative to the previous one.

**Exp. 2: Controlled failure**
- Change: 15% label noise (flipped labels on the whole dataset). Everything else is identical to Exp. 1: same 300 bricks, same split (stratified on the true label, checked with an assert), `max_depth=None`.
- Prediction written before running: training accuracy close to (but not exactly) 100%; test accuracy lower than Exp. 1, with a ceiling of about 85% against the noisy test labels; many more leaves, created to isolate noisy bricks.
- Two test scores: against the stickers (`accepted`, what we would have in real life) and against the truth (`accepted_true`, only available because the data is synthetic).
- Extra measurements: brick types with conflicting labels, wrong brick types ("islands"), memorised noisy bricks, one root-to-leaf trace, feature importances, and 10 seeds for robustness.

## Key Results and Figures

<!-- Draft notes by André (Exp. 2). Seed 42 unless stated otherwise. -->

**Exp. 2 vs Exp. 1**

| | Exp. 1 (clean) | Exp. 2 (15% noise) |
|---|---|---|
| Training accuracy | 1.000 | 0.900 |
| Test accuracy (vs stickers) | 0.989 | 0.778 (ceiling 0.811) |
| Test accuracy (vs truth) | 0.989 | 0.900 |
| Test accuracy vs truth, 10 seeds | 1.000 ± 0.000 | 0.916 ± 0.044 |
| Leaves / depth | 6 / 3 | 48 / 12 |
| Brick types predicted against the rule | 1 of 80 | 10 of 80 |

- Training accuracy stays at 0.900 (prediction partly wrong): most brick types have several copies, so a flipped brick is usually outvoted by its correct twins (13 of 28 noisy bricks). 19 brick types have conflicting labels.
- Islands: 15 of 28 noisy bricks were memorised (5 through tied leaves). 9 of the 10 wrong brick types contain a flipped brick; the 10th (yellow 1×4) is the same missing-data boundary as in Exp. 1.
- Trace: a light green 1×4 with a flipped label needs 7 questions instead of 2 and ends in a leaf holding only itself.
- Feature importances: every colour gains importance and `colour_yellow` drops from 0.22 to 0.04, so the tree loses track of which colour matters.
- Robustness: the failure appears in all 10 seeds (43 to 55 leaves); the std of Exp. 2 is much larger than in Exp. 1, a first sign of instability.
- Figures to include: decision regions Exp. 1 vs Exp. 2 (with flipped bricks marked), feature importances side by side.

## Limitations

<!-- Draft notes by André (Exp. 2). -->
- Synthetic data with one known rule; label noise is random and symmetric, while real noise is often systematic.
- The "test vs truth" score is only possible with synthetic data; in practice only the noisy labels are available.
- The size of the failure depends on how many copies of each brick type exist: with more data, part of the noise is outvoted.
- Changing the seed also changes the test set, so the 10-seed std mixes model instability with test sampling; the bootstrap stability check isolates the first.

## Three Practical Lessons

<!-- Candidate lessons from Exp. 2 (the group picks three overall). -->
- An unrestricted tree fits label noise: always limit `max_depth` or `min_samples_leaf`, chosen by cross-validation.
- Compare training and test scores, and look at the tree size: a large gap with many small leaves signals overfitting.
- Feature importances from an overfitted tree are misleading: noise spreads importance over features the rule never uses.

## Contributions

### Ricardo Tavares

- 
- 
- 

### André Leão

- Experiment 2 (controlled failure): design, prediction, implementation in `dev_b.ipynb` and analysis
- Experimental protocol: redesign so that Exp. 2 changes only one aspect (label noise), with the same bricks and split as Exp. 1 and `max_depth=None` in Exp. 1
- Physical LEGO kit for the class activity (pieces, special colour, noisy kits, mystery bricks), with `src/data.py` aligned to the kit, and the resulting fixes in `dev_a.ipynb`

### José Antunes

- Repository Setup
- Data Generation & Checks(synthetic LEGO dataset)
- Plotting helpers

## AI Use
> Tools: Claude, Google, GitHub Copilot, Gemini

- Image creation for the presentation slides
- Creation of the Project Plan to organize the work by tasks and responsibilities delegated to each team member
- Code review, generation and improvement suggestions
- Code generation for the plotting helpers
- Explanations of decision tree concepts (entropy, information gain, overfitting, cross-validation) used to prepare Exp. 2 and the Q&A (Claude)
- Code for the Exp. 2 cells in `dev_b.ipynb` and the kit-related changes to `src/data.py` and `dev_a.ipynb`, proposed cell by cell, then run and checked by the group (Claude)
- Simulations to check that the physical LEGO kit produces the intended tree, and English proofreading of the Exp. 2 prediction and analysis (Claude)
- Verification / correction (TODO, choose one): the original plan for Exp. 2 changed three settings at once (noise, a 60-brick training set and depth); after checking it against the brief ("change one relevant aspect"), it was redesigned so that only label noise changes / an `assert` checks that Exp. 1 and Exp. 2 use exactly the same split