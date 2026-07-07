print("Spider-Man Box Office Analysis")

import pandas as pd

df = pd.read_csv("spiderman_movies.csv")

print(df)

print("\n========== SUMMARY ==========\n")
print(df.describe())

print("\nAverage Budget:")
average_budget = df["Budget"].mean()

print(f"Average movie budget: ${average_budget:.1f} million")

print("\nHighest Worldwide Gross:")
print(df["Worldwide"].max())

print("\n========== HIGHEST GROSSING MOVIE ==========\n")

highest_gross = df.loc[df["Worldwide"].idxmax()]

print(
    f"{highest_gross['Movie']} earned "
    f"${highest_gross['Worldwide']} million worldwide."
)

print("\n========== HIGHEST RATED MOVIE ==========\n")

highest_rating = df.loc[df["IMDb"].idxmax()]

print(
    f"{highest_rating['Movie']} has an IMDb rating of "
    f"{highest_rating['IMDb']}."
)

print("\n========== LOWEST BUDGET MOVIE ==========\n")

lowest_budget = df.loc[df["Budget"].idxmin()]

print(
    f"{lowest_budget['Movie']} had a budget of "
    f"${lowest_budget['Budget']} million."
)

print("\n========== MILES MORALES MOVIES ==========\n")

miles_movies = df[df["Character"] == "Miles Morales"]

print(miles_movies)

print("\n========== Peter Parker MOVIES ==========\n")

peters_movies = df[df["Character"] == "Peter Parker"]

print(peters_movies)

print("\n========== CHARACTER RATING COMPARISON ==========\n")

character_rating = df.groupby("Character")["IMDb"].mean()

for character, rating in character_rating.items():
    print(f"{character}: Average IMDb rating = {rating:.2f}")

print("\n========== BUDGET VS REVENUE ==========\n")

df["Profit"] = df["Worldwide"] - df["Budget"]

most_profitable = df.loc[df["Profit"].idxmax()]

print(
    f"{most_profitable['Movie']} generated the highest profit "
    f"with ${most_profitable['Profit']} million."
)
