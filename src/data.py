import numpy as np
import pandas as pd

COLOURS = ["red", "blue", "yellow", "green", "black", "white"]
BRICK_SHAPES = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)]
FEATURES = ["stud_rows", "stud_cols","colour"]
TARGET = "accepted"

def builder_rule(stud_rows, stud_cols, colour):
    """
    This function implements the builder's rule for accepting or rejecting a Lego brick.
    
    The rule needs to achieve almost 50% acceptance rate within the dataset
    """
    return (colour == "red" and stud_cols >=4) or (colour != "red" and stud_rows == 2)

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
    ss = np.random.SeedSequence(seed)
    feat_rng, noise_rng = [np.random.default_rng(s) for s in ss.spawn(2)]

    stud_rows, stud_cols = zip(*feat_rng.choice(BRICK_SHAPES, size=n))

    colours = feat_rng.choice(COLOURS, size=n)

    accepted_true = np.array([builder_rule(sr, sc, c) for sr, sc, c in zip(stud_rows, stud_cols, colours)])

    accepted = accepted_true.copy()
    flipped = np.zeros(n, dtype=bool)

    # Add noise
    if noise > 0:
        flip_indices = noise_rng.choice(n, size=round(n * noise), replace=False)
        accepted[flip_indices] = ~accepted[flip_indices]
        flipped[flip_indices] = True

    data = {"stud_rows": stud_rows, 
            "stud_cols": stud_cols, 
            "colour": colours, 
            "accepted": accepted, 
            "accepted_true": accepted_true, 
            "flipped": flipped}

    return pd.DataFrame(data)

def make_encoder():
    return 0
