# Assignment 2 Report — Titanic Survival Analysis

## Question

Which passenger groups on the Titanic — by class, sex, and age — were most likely to
survive? The dataset (`data/raw/titanic.csv`, 891 passengers, sourced from
[seaborn-data](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv),
BSD-3-Clause) gives class, sex, age, fare, and family-size fields for each passenger,
which is enough to break survival down along more than one axis at once.

## What I found

**Class and sex together were the strongest signal.** After cleaning, first-class women
survived at 96.7%, versus 13.5% for third-class men — a seven-fold gap between the best-
and worst-off groups. Second class tracked the same pattern (92.1% women, 15.7% men).
This is visible in `reports/a2_chart1.png`, built from a `groupby(["pclass", "sex"])`
aggregation (survival rate and average fare) merged back onto every passenger row, then
reshaped into a class-by-sex pivot table for the chart itself.

**Age mattered too, but mostly at the extremes.** Passengers under 10 survived at 59.4%,
against 19.0% for passengers over 60 — more than three times the rate. Survival rates for
every age group from 10 to 60 sit in a narrower 32–45% band, so age is a much weaker
predictor than class or sex outside those two tails. This is `reports/a2_chart2.png`.

**A standardized fare score** (Task 4) confirms the fare distribution is heavily
right-skewed: most passengers cluster tightly (z-scores between about -0.6 and 0), while
a handful of first-class fares reach z-scores above 9 — consistent with the class/sex
survival gap, since fare is a strong proxy for class.

## Limitation

This trimmed version of the dataset keeps no passenger-level identifier (no name, ticket
number, or passenger ID), which left 118 fully-duplicate rows after cleaning that I could
not resolve as either genuine repeat records or distinct passengers who happen to share
every recorded field — I documented this rather than guessing, but it means the true
passenger count could be slightly different from 889. Separately, 177 of the original 891
`age` values were missing and were imputed with their class-and-sex group's median age;
about one in five ages in the analysis is therefore an estimate rather than an observed
value, which could soften the true age-survival relationship somewhat.

## Reflection

See `reports/weekend-a2-reflection.md`.
