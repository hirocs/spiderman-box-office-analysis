print("Spider-Man Box Office Analysis")

import pandas as pd

df = pd.read_csv("spiderman_movies.csv")

print(df)

print("\n========== SUMMARY ==========\n")
print(df.describe())

print("\nAverage Budget:")
print(df["Budget"].mean())

print("\nHighest Worldwide Gross:")
print(df["Worldwide"].max())

highest = df.loc[df["Worldwide"].idxmax()]

print("\nHighest Grossing Movie:")
print(f"{highest['Movie']} earned ${highest['Worldwide']} million worldwide.")

