import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    return pd.read_csv("spiderman_movies.csv")


def summary_statistics(df):
    print("\n========== SUMMARY ==========\n")
    print(df.describe())

    average_budget = df["Budget"].mean()
    print(f"\nAverage movie budget: ${average_budget:.1f} million")


def highest_grossing_movie(df):
    print("\n========== HIGHEST GROSSING MOVIE ==========\n")

    highest = df.loc[df["Worldwide"].idxmax()]

    print(
        f"{highest['Movie']} earned "
        f"${highest['Worldwide']} million worldwide."
    )


def highest_rated_movie(df):
    print("\n========== HIGHEST RATED MOVIE ==========\n")

    highest = df.loc[df["IMDb"].idxmax()]

    print(
        f"{highest['Movie']} has an IMDb rating of "
        f"{highest['IMDb']}."
    )


def lowest_budget_movie(df):
    print("\n========== LOWEST BUDGET MOVIE ==========\n")

    lowest = df.loc[df["Budget"].idxmin()]

    print(
        f"{lowest['Movie']} had a budget of "
        f"${lowest['Budget']} million."
    )


def character_analysis(df):
    print("\n========== MILES MORALES MOVIES ==========\n")
    print(df[df["Character"] == "Miles Morales"])

    print("\n========== PETER PARKER MOVIES ==========\n")
    print(df[df["Character"] == "Peter Parker"])

    print("\n========== CHARACTER RATING COMPARISON ==========\n")

    ratings = df.groupby("Character")["IMDb"].mean()

    for character, rating in ratings.items():
        print(f"{character}: Average IMDb rating = {rating:.2f}")


def profit_analysis(df):
    print("\n========== BUDGET VS REVENUE ==========\n")

    df["Profit"] = df["Worldwide"] - df["Budget"]

    highest_profit = df.loc[df["Profit"].idxmax()]

    print(
        f"{highest_profit['Movie']} generated the highest profit "
        f"with ${highest_profit['Profit']} million."
    )


def create_charts(df):

    print("\n========== CREATING CHARTS ==========\n")

    # -------------------------
    # Chart 1: Worldwide Revenue
    # -------------------------

    df_sorted = df.sort_values(by="Worldwide")

    plt.figure(figsize=(14, 7))

    plt.barh(df_sorted["Movie"], df_sorted["Worldwide"])

    plt.title("Worldwide Box Office Revenue of Spider-Man Movies")
    plt.xlabel("Worldwide Revenue (Million USD)")
    plt.ylabel("Movie")

    plt.tight_layout()

    plt.savefig("worldwide_box_office.png")

    plt.show()

    # -------------------------
    # Chart 2: Budget vs Revenue
    # -------------------------

    plt.figure(figsize=(8, 6))

    plt.scatter(df["Budget"], df["Worldwide"])

    plt.title("Budget vs Worldwide Revenue")
    plt.xlabel("Budget (Million USD)")
    plt.ylabel("Worldwide Revenue (Million USD)")

    plt.tight_layout()

    plt.savefig("budget_vs_worldwide.png")

    plt.show()


def main():
    print("Spider-Man Box Office Analysis")

    df = load_data()

    print(df)

    summary_statistics(df)
    highest_grossing_movie(df)
    highest_rated_movie(df)
    lowest_budget_movie(df)
    character_analysis(df)
    profit_analysis(df)
    create_charts(df)


if __name__ == "__main__":
    main()