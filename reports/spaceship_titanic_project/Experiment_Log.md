# Spaceship Titanic Project - Experiment Log

## Experiment 1: Baseline Logistic Regression

CV Score: 0.7860

What I did:
I trained a Logistic Regression model using the original dataset features.

What I learned:
The model performed well and gave me a baseline score to compare future experiments.

## Experiment 2: Feature Engineering

CV Score: 0.7921

What I changed:
I created new features from PassengerId and Cabin, including:
- Group
- GroupPos
- Deck
- CabinNum
- Side
- TotalSpend
- LogSpend
- GroupSize
- IsAlone

What happened:
The score increased from 0.7860 to 0.7921.

## Experiment 3: Random Forest

CV Score: 0.8020

What I changed:
I replaced Logistic Regression with Random Forest.

What happened:
The score improved because Random Forest captured more complex patterns.

## Experiment 4: Gradient Boosting

CV Score: 0.8085

What I changed:
I tested a Gradient Boosting model.

What happened:
This model achieved a better score than previous models.


## Experiment 5: Tuned Gradient Boosting

CV Score: 0.8123

Best Parameters:
- learning_rate = 0.05
- max_iter = 200
- max_leaf_nodes = 15

What happened:
This produced the highest cross-validation score.

## Final Kaggle Result

Best Leaderboard Score: 0.80547
