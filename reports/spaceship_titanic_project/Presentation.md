# Spaceship Titanic Presentation Notes

## Slide 1: Introduction

My name is Umuhoza Marie Solange.

For this project, I worked on the Spaceship Titanic competition from Kaggle. The goal was to predict whether a passenger was transported to another dimension.

---

## Slide 2: About the Dataset

The dataset contains passenger information such as:

- HomePlanet
- CryoSleep
- Destination
- Cabin
- Spending information

The target variable is Transported.

The training dataset contains 8,693 records and the test dataset contains 4,277 records.

---

## Slide 3: My First Model

I started with Logistic Regression using the original features.

Cross-validation score: 0.7860

This gave me a baseline that I could compare with later experiments.

---

## Slide 4: Feature Engineering

I created additional features from the existing data.

Examples:

- Group
- Deck
- Side
- Cabin Number
- Total Spend
- Group Size
- IsAlone

After adding these features, the score increased to 0.7921.

---

## Slide 5: Model Comparison

I tested different machine learning models:

- Logistic Regression
- Random Forest
- Gradient Boosting

Results:

- Logistic Regression: 0.7921
- Random Forest: 0.8020
- Gradient Boosting: 0.8085

Gradient Boosting performed best.

---

## Slide 6: Model Tuning

I used GridSearchCV to tune the Gradient Boosting model.

Best parameters:

- learning_rate = 0.05
- max_iter = 200
- max_leaf_nodes = 15

The tuned model achieved a cross-validation score of 0.8123.

---

## Slide 7: Kaggle Submission

I trained the final model using all training data and generated predictions for the test dataset.

Best Kaggle leaderboard score:

0.80547

---

## Slide 8: Challenges

Some challenges I faced included:

- Missing values
- Choosing useful features
- Comparing different models
- Understanding hyperparameter tuning

---

## Slide 9: What I Learned

Through this project I learned:

- Data preprocessing
- Feature engineering
- Model evaluation
- Cross-validation
- Hyperparameter tuning
- Kaggle workflow

---

## Slide 10: Conclusion

Feature engineering improved the performance of the model.

Among all models tested, Gradient Boosting achieved the best results.

Final CV Score: 0.8123

Best Kaggle Score: 0.80547

Thank you.
