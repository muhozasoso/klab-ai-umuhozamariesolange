# Python for AI — Day 1 Warm-Up

Assignment repo for the "Python for AI Warm-Up" exercise: environment setup, Python
fundamentals, three utility functions, NumPy/Pandas basics, and one chart.

## 1. Create and activate the virtual environment

From the repo root:

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the smoke test

Either from a terminal:

```bash
python -c "import numpy, pandas, sklearn, matplotlib; print('all good')"
```

or open the notebook (see step 4) and run its first code cell — it does the same import
and prints `all good`.

## 4. Open the assignment notebook

```bash
jupyter notebook notebooks/day01_python_for_ai.ipynb
```

(or open the `notebooks/` folder in VS Code / Cursor and run the notebook from there).

Run **Kernel → Restart & Run All**; the notebook should execute top to bottom with no
errors and reproduce every output shown, including the smoke test and the saved chart.

## 5. Project layout

```
notebooks/   day01_python_for_ai.ipynb — the assignment notebook
src/         utils.py — normalise(), summarise_scores(), safe_divide(), train()
data/raw/    untouched input data (empty for this assignment)
data/processed/  derived data (empty for this assignment)
reports/     day01_chart.png, day01_reflection.md
```

## Secrets

Copy `.env.example` to `.env` and fill in real values locally if you add any secrets
later — `.env` is gitignored and nothing in this repo currently requires one.
