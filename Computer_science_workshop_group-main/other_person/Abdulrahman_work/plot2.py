import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Abdular Graph 2")

    # Load Excel file
    data = pd.read_excel(
        "/Users/liwalun/Computer_science_workshop_group-main/other_person/data_set/dataset will be use.xlsx"
    )

    # Fix column names
    data.columns = ["year", "game_name", "id", "searches"]

    # Remove bad first row
    data = data.iloc[1:]

    # Convert types
    data["searches"] = data["searches"].astype(int)

    # Group by game and sum searches
    total_searches = data.groupby("game_name")["searches"].sum()

    # Top 6 most searched games
    top_6 = total_searches.sort_values(ascending=False).head(6)

    # Plot
    plt.figure(figsize=(10, 5))
    top_6.plot(kind="bar")

    plt.xlabel("Game Name")
    plt.ylabel("Total Searches")
    plt.title("Top 6 Most Searched Games")

    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()

    plt.show()

    # ⭐ Prevent macOS backend from blocking your menu system
    plt.close("all")
    return
