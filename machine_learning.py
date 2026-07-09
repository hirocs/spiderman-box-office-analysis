print("Spider-Man Machine Learning Project")

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


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

    # Create the model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    print("\n========== MODEL PARAMETERS ==========\n")

    for feature, coefficient in zip(X.columns, model.coef_):
        print(f"{feature}: {coefficient:.2f}")

    print(f"\nIntercept: {model.intercept_:.2f}")

    print("\n========== MODEL TRAINING ==========\n")
    print("Linear Regression model trained successfully!")

    # Make predictions
    predictions = model.predict(X_test)

    print("\n========== PREDICTIONS ==========\n")

    for actual, predicted in zip(y_test, predictions):
        print(f"Actual: ${actual} million")
        print(f"Predicted: ${predicted:.2f} million")
        print("-" * 30)

    # Evaluate the model
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\n========== MODEL EVALUATION ==========\n")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R² Score: {r2:.2f}")

    # Predict a hypothetical movie
    print("\n========== NEW MOVIE PREDICTION ==========\n")

    new_movie = pd.DataFrame({
        "Budget": [250],
        "OpeningWeekend": [180],
        "IMDb": [8.7],
        "RottenTomatoes": [95],
        "Runtime": [145]
    })

    print(new_movie)

    prediction = model.predict(new_movie)

    print(f"\nPredicted Worldwide Revenue: ${prediction[0]:.2f} million")

    # Compare with existing movies
    print("\n========== COMPARISON WITH EXISTING MOVIES ==========\n")

    comparison = df[["Movie", "Worldwide"]].copy()

    comparison.loc[len(comparison)] = [
        "Hypothetical Spider-Man: Brand New Day",
        prediction[0]
    ]

    comparison = comparison.sort_values(
        by="Worldwide",
        ascending=False
    )

    # Format the Worldwide revenue for better readability
    comparison["Worldwide"] = comparison["Worldwide"].map(
        lambda x: f"${x:2f} million"
    )

    print(comparison)

    # Conclusion
    print("\n========== CONCLUSION ==========\n")

    if prediction[0] < 0:
        print(
            "The model predicted a negative worldwide revenue, which is unrealistic."
        )
        print(
            "This indicates that the model is not reliable due to the "
            "small dataset and limited training examples."
        )
    else:
        print(
            "The predicted worldwide revenue is positive. "
            "However, the prediction should still be interpreted with caution "
            "because the model was trained on a very small dataset."
        )


if __name__ == "__main__":
    main()