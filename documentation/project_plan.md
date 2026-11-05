# AC Challenge — Decision Trees: Project Plan

Nov 4, 2026 · @José Miguel Luís Antunes

## Overview

We have 5 days. Submission closes Monday 9 November at 13:00 and the demo runs the same day from 14:00 to 18:00. The PDF says 2027, which is almost certainly a typo; confirm it with the professor.

**What we deliver**

- A runnable Python notebook (scikit-learn) on a small synthetic 2D dataset, with executed outputs kept.
- A ZIP with the notebook, data-generation script, `requirements.txt` and a short README.
- A PDF report of at most 4 pages, in English, with contribution statements and an AI use declaration.
- A 30-minute presentation, PowerPoint plus the live notebook, with Q&A woven in rather than saved for the end. Every member is questioned individually.

**What is graded**

| Component | Weight | What earns it |
| --- | --- | --- |
| Experimental design and interpretation | 25% | Predictions written before each run, clean protocol, honest analysis |
| Individual understanding | 25% | Each of A, B, C can explain any part of the work |
| Demo clarity | 20% | A clear storyline that links mechanism to behaviour |
| Reproducibility and material quality | 15% | Seeds, train/test split, README that runs first time |
| Live prediction in Q&A | 15% | Predicting the effect of a parameter change before rerunning it |

**Rules we cannot break**

- Every prediction is written before the experiment runs and stays in the final notebook, even when it was wrong.
- Test data is touched only for final evaluation. Depth or leaf size is chosen by cross-validation on training data.
- No AI help during Q&A. Each person answers alone, so everyone must know the whole notebook.

## Demo storyline

The 30 minutes are one story with Q&A inside it: the audience races the clock to sort bricks, then watches the tree do the same on the matching dataset. Slides carry the concepts and the notebook carries the evidence. After each experiment we pause about 1 minute for questions and for "change a parameter, predict, rerun."

| Time | Block | Presenter | Medium | What the audience sees |
| --- | --- | --- | --- | --- |
| 0:00–1:30 | Hook | A | Slides | The question: how would you decide with only yes/no questions? |
| 1:30–7:00 | Lego race | B (A and C hand out kits) | Slides with countdown | Build a tree that sorts bricks into the picky builder's Accepted and Rejected boxes, using colour, stud rows and stud columns, before the timer ends; one mislabeled brick forces an extra question; quick debrief |
| 7:00–11:00 | How a tree works | A | Slides | Bricks map to the dataset; thresholds, entropy / information gain, leaf majority vote |
| 11:00–15:30 | Favourable case + Q&A | A | Notebook | Shallow tree, decision regions, tree diagram, one point traced root to leaf |
| 15:30–20:30 | Controlled failure + Q&A | B | Notebook | Prediction slide first, then label noise on a small training set with a deep tree: train high, test drops, extra leaves built around noisy bricks |
| 20:30–25:30 | Improvement + Q&A | C | Notebook | Depth and min leaf size chosen by CV; train/test curves; stability across reseeds |
| 25:30–28:00 | Three lessons | C | Slides | Three practical rules for using trees |
| 28:00–30:00 | Buffer | All | Either | Open questions, or absorbs any overrun |

The Lego race is not on a rigid clock. An on-screen countdown sets the pace, and when it hits zero we debrief with whatever trees exist. Plan the content for about 28 minutes, so the Q&A pauses and the buffer can absorb interruptions. Switching between slides and notebook should be one keystroke: keep both open side by side and rehearse the swaps.

## Experiment design

The three experiments share one dataset generator and one fixed evaluation protocol. Only the condition under test changes.

**Dataset.** The story is a **picky builder** who sorts every brick into one of two boxes: **Accepted** (goes into the build) or **Rejected** (back in the bin). Three features describe each brick: `stud_rows` (the short side, 1–2), `stud_cols` (the long side, 1–8) and `colour` (6 colours). These ranges are placeholders until B counts the kits and confirms them. Orientation is fixed, with rows always the short side, so a 2×4 is never recorded as 4×2. Use about 300 bricks, `random_state=42`, and a stratified 70/30 train/test split.

**The builder's rule (placeholder).** The class rule is the hidden formula that decides Accepted or Rejected. It is **TBD**, fixed by B once the kit pieces are counted. Requirements for the rule:

- It uses **all three features**, so each one has a reason to appear in the tree.
- `max_depth=3` can represent it exactly, so Exp. 1 can show the tree recovering it.
- Accepted and Rejected each hold roughly half the bricks, given the sizes and colours in our kits.

In code it is one line in `make_data()`, for example `y = rule(colour, stud_rows, stud_cols)`. Use a dummy rule until B confirms.

**Why these features.** Stud count alone would merge different bricks: a 1×8 and a 2×4 both have 8 studs. Rows and columns together define the brick. `stud_cols` carries the threshold splits, such as "cols ≥ 6?". `stud_rows` is nearly binary, so expect one split on it at most. Colour carries real signal and should appear near the root, which is the same "is it red?" question people will ask in the Lego race.

**Encoding and plots.** Colour is one-hot encoded, with the encoder fitted on training data only, so splits read "is\_red = 1". Numbering colours would allow meaningless splits like "colour ≤ 1.5". The main visual is a grid of small panels, one per colour, each showing `stud_cols` × `stud_rows` with its decision regions. Each panel is 2D, as the brief asks. With many colours, show the colours in the rule plus two or three others, and keep the full grid in the notebook only. The tree diagram and feature importances show all three features. Since the features are whole numbers, add a small jitter to the scatter points so identical bricks don't hide each other (for display only).

**Watch the small feature space.** The number of distinct bricks is only rows × cols × colours, 2 × 8 × 6 = 96 with the placeholder ranges, so 300 points contain many duplicates. Recheck this once B confirms the ranges. With that much data, even a deep tree can take a majority vote per brick type and shrug off noise. The failure therefore uses a **small training set** (about 60 bricks) on top of label noise, so many brick types are seen once and the tree memorises whichever label they carry. Duplicates with conflicting labels also mean training accuracy can stay below 100%, so don't promise 100% on the slide.

**Protocol, fixed for all runs.** Entropy criterion. Accuracy is the main metric, since classes are roughly balanced; macro-F1 is reported alongside. Train and test scores are shown for every run, and CV uses 5 folds on training data only.

| Experiment | Condition | Prediction to write first | What to show |
| --- | --- | --- | --- |
| 1. Favourable case | Clean labels, full training set, `max_depth=3` | Near-perfect test accuracy, because the builder's rule is a few axis-aligned questions that a depth-3 tree can express | Tree diagram next to the true rule, per-colour decision regions, root-to-leaf trace for one brick, `export_text`, feature importances |
| 2. Controlled failure | 15% label noise, about 60 training bricks, `max_depth=None` | Train well above test; extra leaves appear to isolate noisy bricks | Same plots side by side with Exp. 1, leaf count, train/test gap, feature importances shifting away from the true rule |
| 3. Attempted improvement | Same noisy, small data; depth and `min_samples_leaf` chosen by CV | Test recovers most of the gap, though not to Exp. 1 levels | Train/test curve over depth, CV-chosen tree, regions; stability check over 5 seeds |

**Stability add-on.** Refit the deep tree on 5 bootstrap resamples and show how the root split and region shapes move. This covers the "stability of the learned tree" point the topic asks for.

**Optional extras.** A small training set (n=30) as a second failure, or a diagonal boundary to show the staircase effect. Add these only if Monday morning has slack.

## Work breakdown

Each person owns one experiment end to end and reviews another's, so nobody can only know their own part. Reviews rotate A → B → C → A.

| # | Task | Owner | Reviewer | Depends on | Due |
| --- | --- | --- | --- | --- | --- |
| 1 | Repo, folder layout, `requirements.txt`, README skeleton | A | C | — | Thu 5 |
| 2 | Data generator (`make_data()` with stud\_rows, stud\_cols, colour, noise and n parameters; sizes taken from our kits) | A | B | 1; ranges and rule from task 6 (build with placeholders first) | Thu 5 |
| 3 | Shared plotting helpers (decision regions, tree diagram, train/test curve, feature importances) | A | C | 1, 2 | Thu 5 |
| 4 | PowerPoint template and slide outline for the 30 minutes | A | B | — | Thu 5 |
| 5 | Exp. 1 favourable case and root-to-leaf trace of one observation | A | B | 2, 3 | Fri 6 |
| 6 | Count kit pieces, confirm feature ranges and fix the builder's rule; Lego race script and Accepted/Rejected stickers | B | A | Kits in hand | Fri 6 |
| 7 | Exp. 2 controlled failure (label noise, small training set, deep tree) | B | C | 2, 3, 5 (same protocol, side-by-side plots) | Fri 6 |
| 8 | Stability check over bootstrap resamples | B | A | 7 | Sat 7 |
| 9 | Exp. 3 improvement (CV over `max_depth` and `min_samples_leaf`) | C | A | 7 (noisy setup); scaffold can start on dummy data | Sat 7 |
| 10 | Slides: A's hook and "how a tree works" | A | C | 4, 5 | Sat 7 |
| 11 | Slides: Lego race with countdown, and failure prediction slide | B | A | 4, 6, 7 | Sat 7 |
| 12 | Slides: improvement summary and three lessons | C | B | 4, 9 | Sat 7 |
| 13 | Reproducibility check: fresh environment, Restart & Run All | C | A | 5, 7, 8, 9 merged into `demo.ipynb` | Sun 8 |
| 14 | Report: model explanation and data | A | B | 5 | Sun 8 |
| 15 | Report: experimental design and failure analysis | B | C | 7, 8 | Sun 8 |
| 16 | Report: results, limitations, lessons, AI declaration | C | A | 9, 13 | Sun 8 |
| 17 | Lego kits packed and counted (one per spectator, plus spares) | B | — | 6 | Sun 8 |
| 18 | Final report edit, ZIP, and InforEstudante submission | A | C | 10–16 | Mon 9, 12:00 |

**Critical path.** A's tasks 1–3 block both experiments, so they must be merged by Thursday evening. Until then, B works on the Lego script (6) and C builds the CV scaffold on dummy data. The second bottleneck is Exp. 2 (7): Exp. 3, the stability check and two slide blocks all wait on it, so B should push it by Friday night. B should also confirm the kit ranges and the builder's rule by Thursday, so the generator and the written predictions use the real values.

Each person writes their own contribution statement. Everyone logs AI use as it happens in a shared note, so the declaration is not reconstructed on Sunday.

## Schedule

The notebook is frozen by Saturday night, the report is done by Sunday night, and Monday morning is for rehearsal only.

| Day | Goal | A | B | C | Group sync |
| --- | --- | --- | --- | --- | --- |
| Wed 4 | Kickoff | Set up repo | Draft Lego race script | Read the brief, draft the lessons | 30 min: agree on this plan, write all predictions |
| Thu 5 | Foundations | Data generator, plot helpers, slide template | Brick-to-feature mapping | CV scaffold on dummy data | 15 min: generator works for everyone |
| Fri 6 | Exp. 1 and 2 done | Exp. 1 and the trace | Exp. 2 | Start Exp. 3 | 30 min: cross-explain Exp. 1 and 2 |
| Sat 7 | Notebook and slides frozen | Review Exp. 3; own slides | Stability check; own slides | Finish Exp. 3; own slides | 1 h: full dry run of slides and notebook |
| Sun 8 | Report and rehearsal | Report: model and data | Report: design and failure; pack kits | Report: results, AI declaration; fresh-environment test | 1 h 15: timed 30-min run with Lego, swap Q&A drills |
| Mon 9 | Submit and present | Final edit, ZIP, submit by 12:00 | Kits to the room | Laptop, slides as PDF backup | 13:00 rehearsal, 14:00 presentation |

The predictions for all three experiments are written on Wednesday, before any code runs. That is the only way they stay honest, and the grade depends on it.

If a progress checkpoint falls before Monday, bring the data setup, the three experiments and the predictions table.

## Workflow and conventions

We use one GitHub repo with one final notebook and shared code in a `src/` module, so three people never edit the same cells at once.

```
ac-decision-trees/
  src/data.py        # make_data(n, noise, seed)
  src/plots.py       # plot_regions, plot_tree, plot_curves
  notebooks/dev_A.ipynb, dev_B.ipynb, dev_C.ipynb
  notebooks/demo.ipynb   # final, assembled Saturday
  report/
  requirements.txt
  README.md
```

- **Branches.** Each person works in their own dev notebook and opens a pull request to `main`. Merging requires the reviewer's approval.
- **Parameters cell.** At the top of `demo.ipynb`, put `SEED`, `N`, `NOISE`, `MAX_DEPTH`, `MIN_SAMPLES_LEAF` and `TEST_SIZE`. Changing a live parameter in Q&A then means editing one cell and rerunning.
- **Seeds.** Every generator, split and model takes `random_state=SEED`.
- **Cell pattern per experiment.** Markdown *Prediction* → code → plots → markdown *What happened and why*. The prediction cell is never edited after the first run.
- **Speed.** The whole notebook must rerun in under 1 minute on a laptop.
- **Clear output before commit** in the dev notebooks; `demo.ipynb` is committed with outputs, as the brief requires.

## Q&A readiness

Individual answers are 40% of the grade, and questions can now land at any point in the 30 minutes, not only at the end. Whoever is asked answers, even if it's another person's block. On Sunday, take turns quizzing each other with the changes below: predict out loud, then run.

| Likely live change | Expected effect | Why |
| --- | --- | --- |
| `max_depth` 3 → 1 | Only the strongest question remains; train and test drop | Underfitting: one question can't express a rule built on three features |
| `max_depth` → None on clean data | Test stays high | No noise to memorise, so the extra splits are mostly harmless |
| Raise noise 15% → 30% | Bigger train/test gap for the deep tree; CV picks a shallower tree | More noise to memorise |
| `min_samples_leaf` 1 → 10 | Fewer leaves, smaller gap | Each leaf must average over more bricks |
| Training set 60 → 300 bricks | Deep tree's gap mostly closes | Duplicates let each leaf take a majority vote that outvotes the noise |
| Drop one feature (e.g. colour) | Test drops clearly | The part of the rule that used it can't be learned from the others |
| Remove a feature from the builder's rule | Its importance falls to near 0 | A feature only matters if the label depends on it |
| Swap rows and columns for some bricks | Noisier tree, more leaves | Orientation errors act like noise in the features |
| Rescale `stud_cols` ×10 | Nothing changes | Trees split on thresholds per feature, so scale is irrelevant |
| Change the seed | Root split likely stays; deep branches change | Deep trees have high variance |

Also prepare short answers to: what entropy measures, why a leaf predicts by majority, how the root split is chosen, why test data is not used to pick depth, and what one fix would be beyond pruning (bagging or a random forest).

## Risks and final checklist

| Risk | Fallback |
| --- | --- |
| Lego race runs long | The countdown on the slide decides; at zero we debrief with whatever trees exist |
| Questions mid-talk eat the time | Content is planned for about 28 min with a 2-min buffer; drop the stability plot first, then the optional extras |
| Noise doesn't hurt the deep tree enough | Raise noise or shrink the training set; record the original prediction anyway |
| Notebook or slides break on the demo laptop | Submitted ZIP and slides as PDF on a USB stick, plus a second laptop with outputs already rendered |
| One person falls behind | Saturday's dry run is the checkpoint; the reviewer takes over unfinished cells or slides |
| Report runs over 4 pages | Figures go 2 per row; move extras to the notebook only |

**Before submitting (Mon 9, by 12:00)**

- [ ] Deadline year confirmed with the professor
- [ ] `demo.ipynb` runs top to bottom in a fresh environment with outputs saved
- [ ] All three predictions are present and unedited
- [ ] README setup steps tested by someone who didn't write them
- [ ] Report is 4 pages or less, in English, with contribution statements, AI declaration and citations
- [ ] Slides final and exported to PDF as a backup
- [ ] ZIP contains notebook, `src/`, `requirements.txt`, README and the data script
- [ ] Lego kits packed, one per spectator plus 2 spares
- [ ] Everyone has done at least one timed run of the full 30 minutes, slides and notebook, with mock questions
