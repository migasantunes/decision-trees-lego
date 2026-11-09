# Decision Trees with LEGO - Machine Learning Project
This project explores the use and explanation of decision trees in a fun and engaging way using LEGO bricks as a visual representation of the decision-making process.

## Group Members
- Ricardo Tavares - No. 2026133913
- André Leão - No. 2023210870
- José Antunes - No. 2023211288

## Repository Structure

```
decision-trees-lego/
├── documentation/
│   └── report.md            # Final project report
├── notebooks/
│   ├── dev_a.ipynb          # Data checks and Exp. 1: favourable case
│   ├── dev_b.ipynb          # Exp. 2: controlled failure (label noise) + stability check
│   └── dev_c.ipynb          # Exp. 3: attempted improvement (GridSearchCV)
├── src/
│   ├── __init__.py          # Makes src importable
│   ├── data.py              # Synthetic LEGO data generator
│   └── plots.py             # Plotting helpers
├── .gitignore
├── requirements.txt         # Python dependencies
└── README.md
```

## Environment Setup

Create an environment with Python 3.14.3 (Tested on Python 3.14.3) and install the requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Notebooks

1. Activate the virtual environment
2. Open the notebooks in your preferred IDE or Jupyter Notebook
3. Select the kernel from .venv
4. Run the notebooks by clicking `Restart` and then `Run All` in the notebook interface.

> Run them in order: dev_a (Exp. 1), dev_b (Exp. 2 and stability), dev_c (Exp. 3).\
> Each notebook is self-contained and regenerates its own data from src/data.py.

## Additional Information

- To be able to use the `src` module in the notebooks, we added `__init__.py` to the src directory, making it importable. Then, we used the following code snippet at the beginning of each notebook:

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd().parent))
```

- If any changes are made to the src module, restart the kernel to ensure the changes are reflected in the notebooks.