import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Abdular Graph 1")

    # Load Excel file
    data = pd.read_excel("/Users/liwalun/Computer_science_workshop_group-main/other_person/data_set/dataset will be use.xlsx")

    # Fix column names
    data.columns = ["year", "game_name", "id", "searches"]

    # Remove bad first row
    data = data.iloc[1:]

    # Convert types
    data["year"] = data["year"].astype(int)
    data["searches"] = data["searches"].astype(int)

    # First two games
    games = data["game_name"].unique()[:2]
    filtered = data[data["game_name"].isin(games)]

    # Plot
    plt.figure()

    for game in games:
        game_data = filtered[filtered["game_name"] == game]
        plt.plot(
            game_data["year"],
            game_data["searches"],
            marker='o',
            linestyle='-',
            label=game
        )

    plt.grid()
    plt.xlabel("Year")
    plt.ylabel("Searches")
    plt.title("This graph shows how search interest for the two games changes over time")
    plt.legend()
    plt.show()

