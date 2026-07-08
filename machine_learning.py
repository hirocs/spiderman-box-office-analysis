print("Spider-Man Machine Learning Project")

import pandas as pd


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

    


if __name__ == "__main__":
    main()