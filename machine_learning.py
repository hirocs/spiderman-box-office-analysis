print("Spider-Man Machine Learning Project")

import pandas as pd

from sklearn.model_selection import train_test_split


def load_data():
    return pd.read_csv("spiderman_movies.csv")


def main():
    df = load_data()

    print("\n========== DATASET ==========\n")
    print(df)

    # Features (Input)
    X = df[[
        "Budget",
        "OpeningWeekend",
        "IMDb",
        "RottenTomatoes",
        "Runtime"
    ]]

    # Target (Output)
    y = df["Worldwide"]

    print("\n========== FEATURES (X) ==========\n")
    print(X)

    print("\n========== TARGET (y) ==========\n")
    print(y)

    print("\n========== DATA SHAPE ==========\n")
    print(f"Features (X): {X.shape}")
    print(f"Target (y): {y.shape}")

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("\n========== TRAIN / TEST SPLIT ==========\n")

    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    
if __name__ == "__main__":
    main()