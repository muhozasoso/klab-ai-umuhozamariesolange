# Titanic assignment - Logistic Regression vs Random Forest
#
# Original assignment was about predicting car prices (Linear Regression vs
# Random Forest) but I used the Titanic dataset instead. Since Survived is
# 0/1 and not a number, I swapped in Logistic Regression instead of plain
# Linear Regression - it's still the "linear model" side of the comparison,
# just for classification instead of regression.

import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

# 1. load the data and take a look
df = pd.read_csv("data/titanic.csv")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum()[df.isnull().sum() > 0])
print("\nSurvival rate:", df["Survived"].mean().round(3))

# 2. pick features + clean them up
# not using every column - Name/Ticket/Cabin need way more preprocessing
# than we covered in class, so sticking to the simple numeric/categorical ones
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
data = df[features + ["Survived"]].copy()

# sklearn wants numbers, not strings
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Age has a bunch of missing values (177 of them), Embarked has 2
# filling Age/Fare with the median, Embarked with whatever's most common
imputer = SimpleImputer(strategy="median")
data[["Age", "Fare"]] = imputer.fit_transform(data[["Age", "Fare"]])
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

X = data[features]
y = data["Survived"]

# 80/20 split, stratify so both sets have a similar survival ratio
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. model 1 - logistic regression
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
logreg_pred = logreg.predict(X_test)
logreg_acc = accuracy_score(y_test, logreg_pred)

print("\n--- Logistic Regression ---")
print("Accuracy:", round(logreg_acc, 4))
print("Coefficients:")
for f, c in zip(features, logreg.coef_[0]):
    print(f"  {f}: {c:.3f}")

# 4. model 2 - random forest
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

print("\n--- Random Forest ---")
print("Accuracy:", round(rf_acc, 4))
print("Feature importances:")
for f, imp in sorted(zip(features, rf.feature_importances_), key=lambda t: -t[1]):
    print(f"  {f}: {imp:.3f}")

# 5. compare the two
print("\n--- Comparison ---")
print(f"Logistic Regression accuracy: {logreg_acc:.4f}")
print(f"Random Forest accuracy:       {rf_acc:.4f}")
winner = "Random Forest" if rf_acc > logreg_acc else "Logistic Regression"
print(f"Winner on this split: {winner}")

# dump results to a file so I don't have to rerun this every time I want the numbers
summary = {
    "logreg_acc": logreg_acc,
    "rf_acc": rf_acc,
    "logreg_coefs": dict(zip(features, logreg.coef_[0])),
    "rf_importances": dict(zip(features, rf.feature_importances_)),
}
with open("results/results.json", "w") as f:
    json.dump(summary, f, indent=2, default=float)
