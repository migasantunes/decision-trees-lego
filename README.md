# Decision Trees with LEGO - Machine Learning Project
This project explores the use and explanation of decision trees in a fun and engaging way using LEGO bricks as a visual representation of the decision-making process.

## Group Members
- Ricardo Tavares - No. 2026133913
- André Leão - No. 2023210870
- José Antunes - No. 2023211288

## Repository Structure

```
decision-trees-lego/
├── markdown/
│   ├── challenge_brief.md
│   ├── project_plan.md
│   └── report.md            # Final project report
├── notebooks/
│   ├── demo.ipynb           # Final notebook used in the presentation
│   ├── dev_a.ipynb          # Dev A notebook
│   ├── dev_b.ipynb          # Dev B notebook
│   └── dev_c.ipynb          # Dev C notebook
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
4. Run the cells in the notebooks

## Additional Information

- To be able to use the `src` module in the notebooks, we added \_\_init\_\_.py to the src directory, making it importable. Then, we used the following code snippet at the beginning of each notebook:

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd().parent))
```

- If any changes are made to the src module, restart the kernel to ensure the changes are reflected in the notebooks.