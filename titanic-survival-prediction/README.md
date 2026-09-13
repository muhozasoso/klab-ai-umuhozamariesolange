# Titanic Survival Prediction

Assignment for ML Fundamentals class. The original assignment was to predict
car prices using Linear Regression and Random Forest, but I used the Titanic
dataset instead. Survived is 0/1 (not a continuous number like price), so I
used Logistic Regression instead of plain Linear Regression - same idea
though, it's the linear model side of the comparison, just for
classification.

## Files

```
titanic-survival-prediction/
├── data/
│   └── titanic.csv
├── results/
│   └── results.json
├── titanic_survival_prediction.py
├── requirements.txt
└── README.md
```

## How to run

```bash
pip install -r requirements.txt
python titanic_survival_prediction.py
```

## What it does

1. Loads `titanic.csv`, checks for missing values and the overall survival rate
2. Picks a handful of features (Pclass, Sex, Age, SibSp, Parch, Fare,
   Embarked), fills in missing Age/Fare with the median, missing Embarked
   with the most common value
3. Trains a Logistic Regression model on an 80/20 split
4. Trains a Random Forest (200 trees) on the same split
5. Compares accuracy and saves everything to `results/results.json`

## Results

| Model | Accuracy |
|---|---|
| Logistic Regression | 80.5% |
| Random Forest | 82.1% |

Logistic Regression's coefficients make it pretty easy to see what's going
on - being female is by far the biggest factor (makes sense, "women and
children first"), followed by Pclass (higher class number = worse odds) and
Age (older = slightly worse odds).

Random Forest ranks Fare, Sex, and Age as roughly equally important, with
Pclass way down the list. My guess is it's catching some interaction
between Fare and Pclass/Cabin that Logistic Regression can't since it just
draws a straight line through the data.

Random Forest won by about 1.7 points, but that's a pretty small gap on a
dataset this size - it could easily flip with a different train/test split.
If I had to pick one to actually explain to someone, I'd go with Logistic
Regression since the coefficients are so much easier to interpret.

## Things I'd try next time

- Add an interaction term between Sex and Pclass in the logistic model
- Use cross-validation instead of one train/test split, since accuracy
  probably bounces around a bit run to run
- Try Gradient Boosting as a third model to compare against
