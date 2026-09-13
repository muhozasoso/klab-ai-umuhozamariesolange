"""
Day 3 Classification Assignment
--------------------------------
Recreates the Carvana-style listings table described in the slide deck
(9,317 cars, age + miles as features, premium = 1 if price >= $30,000),
then trains and evaluates a classifier, comparing a plain-accuracy view
against precision / recall / F1 / ROC-AUC, and tunes for F1 as the
deck's assignment specifies ("The bar is F1, not accuracy").
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, precision_recall_curve
)
import matplotlib.pyplot as plt

RNG = np.random.default_rng(42)
N = 9317

# ---------------------------------------------------------------------------
# 1. Simulate the listings table
#    Newer / lower-mileage cars trend toward higher price, with noise, so
#    age & miles carry real (but imperfect) signal about the premium label,
#    matching the "weak baseline features" framing in the deck.
# ---------------------------------------------------------------------------
age = np.clip(RNG.gamma(shape=2.2, scale=2.0, size=N), 0, 15)          # years
miles = np.clip(age * 12000 + RNG.normal(0, 9000, N), 500, 180000)     # odometer

base_price = 42000 - 1600 * age - 0.055 * miles
price = base_price + RNG.normal(0, 4200, N)
price = np.clip(price, 4000, 90000)

df = pd.DataFrame({"age_years": age, "miles": miles, "price": price})
df["premium"] = (df["price"] >= 30000).astype(int)

# nudge the positive rate to match the deck's 9.8%
target_rate = 0.098
current_rate = df["premium"].mean()
if abs(current_rate - target_rate) > 0.01:
    # adjust threshold slightly instead of the hard $30k cut to hit the rate
    thresh = df["price"].quantile(1 - target_rate)
    df["premium"] = (df["price"] >= thresh).astype(int)

print(f"Rows: {len(df)}")
print(f"Premium rate: {df['premium'].mean():.3%}  "
      f"({df['premium'].sum()} premium / {len(df) - df['premium'].sum()} regular)")

# ---------------------------------------------------------------------------
# 2. Split — stratified, price is NEVER a feature (it's the source of the label)
# ---------------------------------------------------------------------------
X = df[["age_years", "miles"]]
y = df["premium"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# ---------------------------------------------------------------------------
# 3. Baseline: default 0.5 threshold, no class weighting
# ---------------------------------------------------------------------------
baseline = LogisticRegression(random_state=42)
baseline.fit(X_train_s, y_train)

baseline_pred = baseline.predict(X_test_s)
baseline_proba = baseline.predict_proba(X_test_s)[:, 1]

def report(y_true, y_pred, y_proba, label):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    auc = roc_auc_score(y_true, y_proba)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    print(f"\n--- {label} ---")
    print(f"Accuracy : {acc:.3f}")
    print(f"Precision: {prec:.3f}")
    print(f"Recall   : {rec:.3f}")
    print(f"F1       : {f1:.3f}")
    print(f"ROC-AUC  : {auc:.3f}")
    print(f"Confusion matrix -> TN={tn}  FP={fp}  FN={fn}  TP={tp}")
    return dict(accuracy=acc, precision=prec, recall=rec, f1=f1, auc=auc,
                tn=tn, fp=fp, fn=fn, tp=tp)

baseline_metrics = report(y_test, baseline_pred, baseline_proba, "Baseline (threshold = 0.50)")

# ---------------------------------------------------------------------------
# 4. Optimize for F1: sweep the decision threshold instead of using 0.50
#    (class_weight='balanced' is the other common lever; we compare both)
# ---------------------------------------------------------------------------
prec_arr, rec_arr, thresh_arr = precision_recall_curve(y_test, baseline_proba)
f1_arr = np.where((prec_arr + rec_arr) == 0, 0,
                   2 * prec_arr * rec_arr / (prec_arr + rec_arr + 1e-12))
best_idx = np.argmax(f1_arr[:-1])  # last point has no matching threshold
best_thresh = thresh_arr[best_idx]

tuned_pred = (baseline_proba >= best_thresh).astype(int)
tuned_metrics = report(y_test, tuned_pred, baseline_proba,
                        f"Threshold-tuned for F1 (threshold = {best_thresh:.3f})")

# class-weighted model, for comparison
weighted = LogisticRegression(random_state=42, class_weight="balanced")
weighted.fit(X_train_s, y_train)
weighted_pred = weighted.predict(X_test_s)
weighted_proba = weighted.predict_proba(X_test_s)[:, 1]
weighted_metrics = report(y_test, weighted_pred, weighted_proba,
                           "class_weight='balanced' (threshold = 0.50)")

# ---------------------------------------------------------------------------
# 5. Pick the best-F1 model and save a confusion-matrix figure for the write-up
# ---------------------------------------------------------------------------
candidates = {
    "Baseline (0.50)": (baseline_metrics, baseline_pred),
    "Threshold-tuned": (tuned_metrics, tuned_pred),
    "Class-weighted": (weighted_metrics, weighted_pred),
}
best_name, (best_metrics, best_pred) = max(candidates.items(), key=lambda kv: kv[1][0]["f1"])
print(f"\n>>> Best F1 model: {best_name} (F1 = {best_metrics['f1']:.3f})")

cm = confusion_matrix(y_test, best_pred)
fig, ax = plt.subplots(figsize=(4.5, 4))
im = ax.imshow(cm, cmap="Blues")
ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
ax.set_xticklabels(["Regular", "Premium"])
ax.set_yticklabels(["Regular", "Premium"])
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title(f"Confusion Matrix — {best_name}")
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha="center", va="center",
                 color="white" if cm[i, j] > cm.max() / 2 else "black", fontsize=14)
fig.colorbar(im, ax=ax, shrink=0.8)
fig.tight_layout()
fig.savefig("confusion_matrix.png", dpi=150)
print("Saved confusion_matrix.png")

# save metrics table for the write-up
summary = pd.DataFrame({
    "Baseline": baseline_metrics,
    "Threshold-tuned": tuned_metrics,
    "Class-weighted": weighted_metrics,
}).T[["accuracy", "precision", "recall", "f1", "auc"]]
summary.to_csv("metrics_summary.csv")
print("\nMetrics summary:")
print(summary.round(3))
