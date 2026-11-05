import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.tree import plot_tree as sk_plot_tree

from src.data import COLOURS, BRICK_SHAPES, FEATURES, TARGET

CLASS_NAMES = ["Rejected", "Accepted"]
CLASS_COLOURS = ["#d9534f", "#5cb85c"]  # red = Rejected, green = Accepted
REGION_CMAP = ListedColormap(["#f6d5d4", "#d6eed6"])
MAX_ROWS = max(r for r, _ in BRICK_SHAPES)
MAX_COLS = max(c for _, c in BRICK_SHAPES)


def plot_regions(tree, enc, df=None, colours=COLOURS, jitter=0.15, seed=42, title=None):
    """
    One panel per colour: stud_cols (x) vs stud_rows (y), shaded by the tree's prediction.

    tree:    fitted DecisionTreeClassifier (trained on enc-transformed data)
    enc:     encoder already fitted on the training data
    df:      optional data to scatter on top (e.g. the training set); flipped labels drawn as X
    jitter:  display-only noise so duplicate bricks don't hide each other
    """
    cols, rows = np.arange(1, MAX_COLS + 1), np.arange(1, MAX_ROWS + 1)
    cc, rr = np.meshgrid(cols, rows)
    valid = np.array([[(r, c) in BRICK_SHAPES for c in cols] for r in rows])

    fig, axes = plt.subplots(1, len(colours), figsize=(3.2 * len(colours), 2.6), sharey=True, squeeze=False)
    rng = np.random.default_rng(seed)

    for ax, colour in zip(axes[0], colours):
        grid = pd.DataFrame({"stud_rows": rr.ravel(), "stud_cols": cc.ravel(),
                             "colour": pd.Categorical([colour] * rr.size, categories=COLOURS)})
        pred = tree.predict(enc.transform(grid[FEATURES])).astype(float).reshape(rr.shape)
        pred[~valid] = np.nan  # shapes that don't exist (e.g. 2x1, recorded as 1x2)
        ax.pcolormesh(np.arange(0.5, MAX_COLS + 1), np.arange(0.5, MAX_ROWS + 1), pred,
                      cmap=REGION_CMAP, vmin=0, vmax=1, edgecolors="white", linewidth=1)

        if df is not None:
            sub = df[df["colour"] == colour]
            x = sub["stud_cols"] + rng.uniform(-jitter, jitter, len(sub))
            y = sub["stud_rows"] + rng.uniform(-jitter, jitter, len(sub))
            flipped = sub["flipped"].to_numpy() if "flipped" in sub else np.zeros(len(sub), bool)
            c = np.array(CLASS_COLOURS)[sub[TARGET].astype(int)]
            ax.scatter(x[~flipped], y[~flipped], c=c[~flipped], s=18, edgecolors="k", linewidths=0.4)
            ax.scatter(x[flipped], y[flipped], c=c[flipped], s=40, marker="X", edgecolors="k", linewidths=0.6)

        ax.set_title(colour)
        ax.set_xticks(cols)
        ax.set_yticks(rows)
        ax.set_xlabel("stud_cols")
    axes[0, 0].set_ylabel("stud_rows")

    handles = [plt.Line2D([], [], marker="s", ls="", ms=10, color=REGION_CMAP(i), label=f"region: {n}")
               for i, n in enumerate(CLASS_NAMES)]
    if df is not None:
        handles += [plt.Line2D([], [], marker="o", ls="", color=CLASS_COLOURS[i], mec="k", label=n)
                    for i, n in enumerate(CLASS_NAMES)]
        handles.append(plt.Line2D([], [], marker="X", ls="", color="grey", mec="k", label="flipped label"))
    fig.legend(handles=handles, loc="lower center", ncol=len(handles), bbox_to_anchor=(0.5, -0.12), frameon=False)
    if title:
        fig.suptitle(title)
    fig.tight_layout()
    return fig


def plot_tree(tree, enc, ax=None, **kwargs):
    """Tree diagram with feature and class names."""
    if ax is None:
        n_leaves = tree.get_n_leaves()
        _, ax = plt.subplots(figsize=(max(8, 1.6 * n_leaves), 2 + 1.5 * tree.get_depth()))
    sk_plot_tree(tree, feature_names=list(enc.get_feature_names_out()), class_names=CLASS_NAMES,
                 filled=True, rounded=True, impurity=True, fontsize=kwargs.pop("fontsize", 9), ax=ax, **kwargs)
    return ax


def plot_curves(values, train_scores, test_scores=None, cv_scores=None, cv_std=None,
                xlabel="max_depth", ylabel="accuracy", ax=None):
    """
    Train / CV / test score against a hyperparameter (e.g. max_depth or min_samples_leaf).
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 3.5))
    x = np.arange(len(values))
    ax.plot(x, train_scores, "o-", label="train")
    if cv_scores is not None:
        ax.plot(x, cv_scores, "s-", label="CV (train folds)")
        if cv_std is not None:
            cv_scores, cv_std = np.asarray(cv_scores), np.asarray(cv_std)
            ax.fill_between(x, cv_scores - cv_std, cv_scores + cv_std, alpha=0.2, color="C1")
    if test_scores is not None:
        ax.plot(x, test_scores, "^-", label="test")
    ax.set_xticks(x, [str(v) for v in values])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(top=1.02)
    ax.grid(alpha=0.3)
    ax.legend()
    return ax


def plot_importances(tree, enc, group_colour=True, ax=None, title=None):
    """
    Gini feature importances. With group_colour=True the one-hot colour_* columns
    are summed into a single 'colour' bar, so the three original features are compared.
    """
    imp = pd.Series(tree.feature_importances_, index=enc.get_feature_names_out())
    if group_colour:
        is_colour = imp.index.str.startswith("colour_")
        imp = pd.concat([pd.Series({"colour": imp[is_colour].sum()}), imp[~is_colour]])
    imp = imp.sort_values()
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 0.4 * len(imp) + 1))
    ax.barh(imp.index, imp.values, color="C0")
    ax.set_xlabel("importance (Gini decrease)")
    ax.set_xlim(0, 1)
    if title:
        ax.set_title(title)
    return ax
