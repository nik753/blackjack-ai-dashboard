import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import joblib

# LOAD DATASET

df = pd.read_csv(
    "data/blackjack_dataset.csv"
)

# FEATURES

X = df[
    [
        "player_total",
        "dealer_card",
        "running_count"
    ]
]

# TARGET

y = df["result"]

# SPLIT DATA

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2
)

# CREATE MODEL

model = RandomForestClassifier()

# TRAIN MODEL

model.fit(X_train, y_train)

# TEST MODEL

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Model Accuracy:", accuracy)

# SAVE MODEL

joblib.dump(
    model,
    "blackjack_ai.pkl"
)

print("Model Saved Successfully")