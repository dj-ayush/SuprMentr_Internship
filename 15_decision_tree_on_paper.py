# Assignment Date: 12/03/2026
# Assignment Name: Decision Tree on Paper
# Description: Draw a decision tree predicting whether you should play outside.
#
# This script prints an ASCII decision tree and also trains a real
# scikit-learn DecisionTreeClassifier on the classic PlayTennis dataset
# (play_tennis.csv, 14 rows).

import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text


HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "play_tennis.csv")


ASCII_TREE = r"""
               [ Outlook? ]
               /    |     \
           Sunny  Overcast  Rain
            /       |         \
     [Humidity?]   PLAY     [Wind?]
       /    \               /    \
     High  Normal         Weak  Strong
      |      |             |      |
   DON'T   PLAY          PLAY   DON'T
"""


def main() -> None:
    print("=== Decision Tree: Should I play outside? ===")
    print(ASCII_TREE)

    df = pd.read_csv(CSV_PATH)
    print(f"Loaded play_tennis.csv  shape={df.shape}")
    print(df)

    # One-hot encode the categorical features so the sklearn tree can use them.
    X = pd.get_dummies(df[["outlook", "temperature", "humidity", "wind"]])
    y = (df["play"] == "Yes").astype(int)

    model = DecisionTreeClassifier(criterion="entropy", random_state=0)
    model.fit(X, y)

    print("\n--- scikit-learn decision tree rules (ID3-like) ---")
    print(export_text(model, feature_names=list(X.columns)))

    # Predict a new scenario: Sunny + Mild + High humidity + Weak wind
    sample = pd.DataFrame([{
        "outlook": "Sunny", "temperature": "Mild",
        "humidity": "High", "wind": "Weak",
    }])
    sample_enc = pd.get_dummies(sample).reindex(columns=X.columns, fill_value=0)
    prediction = model.predict(sample_enc)[0]
    print(f"Sample scenario: {sample.to_dict(orient='records')[0]}")
    print("Decision: " + ("Play outside!" if prediction == 1 else "Stay indoors."))


if __name__ == "__main__":
    main()
