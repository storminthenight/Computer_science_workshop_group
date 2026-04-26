import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Two-Game Search Interest Graph")

    # Excel file path
    excel_file = "/Users/liwalun/Computer_science_workshop_group-main/other_person/data_set/dataset will be use.xlsx"

    # Read interest_over_time sheet (skip metadata rows)
    interest_df = pd.read_excel(excel_file, sheet_name="interest_over_time", header=2)

    # Clean column names
    interest_df.columns = ["year", "name", "id", "num_searches"]

    # Convert types
    interest_df["year"] = pd.to_numeric(interest_df["year"], errors="coerce")
    interest_df["num_searches"] = pd.to_numeric(interest_df["num_searches"], errors="coerce")

    # Remove invalid rows
    interest_df = interest_df.dropna(subset=["year", "name", "num_searches"])

    # Pick first two games
    games = interest_df["name"].unique()[:2]
    filtered = interest_df[interest_df["name"].isin(games)]

    # Plot
    plt.figure(figsize=(10, 6))

    for game in games:
        game_data = filtered[filtered["name"] == game].sort_values("year")
        plt.plot(
            game_data["year"],
            game_data["num_searches"],
            marker="o",
            linestyle="-",
            label=game
        )

    plt.grid(True)
    plt.xlabel("Year")
    plt.ylabel("Searches")
    plt.title("Search Interest Over Time for Two VR Games")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Prevent macOS backend from blocking your menu
    plt.close("all")
    return
