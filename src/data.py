import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Colours and shapes match the physical LEGO kits used in the activity (and the mystery bricks).
# Each colour keeps its position in the list, so renaming a colour does not change the generated data.
COLOURS = ["yellow", "blue", "dark_green", "pink", "beige", "brown", "light_green", "black"]
BRICK_SHAPES = [(1, 2), (1, 3), (1, 4), (1, 6), (1, 10), (2, 2), (2, 3), (2, 4), (2, 6), (2, 8)]
SPECIAL_COLOUR = "yellow"   # the colour the picky builder treats differently
FEATURES = ["stud_rows", "stud_cols", "colour"]
TARGET = "accepted"

def builder_rule(stud_rows, stud_cols, colour):
    """
    This function implements the builder's rule for accepting or rejecting a Lego brick.
    
    The rule needs to achieve almost 50% acceptance rate within the dataset
    Rule: 
    - if the brick is of the special color and has 4 or more studs in the column direction, it is accepted.
    - if the brick is not of the special color and has 2 studs in the row direction, it is accepted.
    - otherwise, it is rejected.
    """
    stud_rows, stud_cols, colour = map(np.asarray, (stud_rows, stud_cols, colour))
    is_special = colour == SPECIAL_COLOUR

    return (is_special & (stud_cols >= 4)) | (~is_special & (stud_rows == 2))

def make_data(n=300, noise=0.0, seed=42):
    """
    This function generates a dataset of Lego bricks

    Parameters:
    n: Number of samples to generate
    noise: Proportion of samples to flip the accepted label
    seed: Random seed

    Returns:
    pd.DataFrame containing the generated dataset
    """

    # Validate inputs
    if n <= 0: raise ValueError("n must be positive")
    if not 0 <= noise <= 0.5: raise ValueError("noise must be in [0, 0.5]")

    ss = np.random.SeedSequence(seed)
    feat_rng, noise_rng = [np.random.default_rng(s) for s in ss.spawn(2)]

    shapes = feat_rng.choice(np.array(BRICK_SHAPES), size=n)
    stud_rows, stud_cols = shapes[:, 0], shapes[:, 1]


    colours = feat_rng.choice(COLOURS, size=n)

    accepted_true = builder_rule(stud_rows, stud_cols, colours)

    accepted = accepted_true.copy()
    flipped = np.zeros(n, dtype=bool)

    # Add noise
    if noise > 0:
        flip_indices = noise_rng.choice(n, size=round(n * noise), replace=False)
        accepted[flip_indices] = ~accepted[flip_indices]
        flipped[flip_indices] = True

    data = {"stud_rows": stud_rows, 
            "stud_cols": stud_cols, 
            "colour": pd.Categorical(colours, categories=COLOURS),
            "accepted": accepted, 
            "accepted_true": accepted_true, 
            "flipped": flipped}

    return pd.DataFrame(data)

def make_encoder():
    """
    Unfitted encoder: one-hot for colour, stud counts passed through unchanged.

    Fit it on training data only, then reuse it to transform the test data.
    """
    return ColumnTransformer(transformers=[("colour", OneHotEncoder(categories=[COLOURS], 
                                                                    sparse_output=False,
                                                                    handle_unknown="ignore"), ["colour"]),
                                           ("studs", "passthrough", ["stud_rows", "stud_cols"])],
                             verbose_feature_names_out=False)