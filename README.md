# Classification Assignment — Flagging Premium Carvana Listings

kLab Academy · AI Intensive · Day 3

## What this does

Simulates the 9,317-row Carvana listings table described in the Day 3 slide
deck (age + miles as features, `premium = 1` if price ≥ $30,000, ~9.8%
positive rate), then trains and evaluates a logistic regression classifier
three ways:

1. **Baseline** — default 0.50 decision threshold
2. **Threshold-tuned** — sweeps the threshold to maximize F1
3. **Class-weighted** — `class_weight="balanced"`, default threshold

It prints accuracy / precision / recall / F1 / ROC-AUC for each, saves a
confusion-matrix plot for the best-F1 model, and writes a metrics summary
CSV.

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python build_classifier.py
```

Outputs land in the project root: `confusion_matrix.png` and
`metrics_summary.csv`.

## Files

- `build_classifier.py` — data simulation, training, evaluation
- `Classification_Assignment_Writeup.docx` — 1-page write-up on the metric
  choice (F1) and the business justification
- `requirements.txt` — Python dependencies

## Note on the data

The real Carvana listings CSV from Day 2 wasn't available, so
`build_classifier.py` simulates a table matching the deck's stated shape
(9,317 rows, 9.8% premium, age/miles correlated with price). Swap in the
real CSV and point the script at it if you get access to it — the rest of
the pipeline (split, train, evaluate) doesn't need to change.
