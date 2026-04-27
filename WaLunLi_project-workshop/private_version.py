import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_graph():
    # load the excel file (my dataset for the games)
    file_path = "/Users/liwalun/Computer_science_workshop_group-main/WaLunLi_project-workshop/data_set/dataset will be use.xlsx"

    # read the sheet (first row is header)
    df = pd.read_excel(file_path, sheet_name="vgi_game_stats", header=1)

    # clean column names
    df.columns = df.columns.str.strip()

    # convert active players to numeric
    df["active_plyrs(24hrs)"] = pd.to_numeric(df["active_plyrs(24hrs)"], errors='coerce')

    # clean positive reviews (remove % and convert to number)
    df["pos_reviews"] = df["pos_reviews"].astype(str).replace('%', '', regex=False)
    df["pos_reviews"] = pd.to_numeric(df["pos_reviews"], errors='coerce')

    # strip game names
    df["game_name"] = df["game_name"].str.strip()

    # only keep the 4 games I want to compare
    games = ["War Thunder", "VRChat", "Phasmophobia", "No Man's Sky"]
    df_selected = df[df["game_name"].isin(games)]

    # sort from low to high (active players)
    df_selected = df_selected.sort_values(by="active_plyrs(24hrs)")

    # convert positive reviews to 0–100 scale
    df_selected["pos_reviews"] = df_selected["pos_reviews"] * 100

    # start plotting
    fig, ax1 = plt.subplots(figsize=(10, 6))

    x = np.arange(len(df_selected))
    width = 0.4

    # bar for active players
    bars1 = ax1.bar(
        x - width/2,
        df_selected["active_plyrs(24hrs)"],
        width,
        label="Active Players (24hrs)",
        color="#4C72B0"
    )

    ax1.set_ylabel("Active Players (24hrs)")
    ax1.set_xlabel("Game Name")
    ax1.set_xticks(x)
    ax1.set_xticklabels(df_selected["game_name"], rotation=20)

    # second axis for positive reviews
    ax2 = ax1.twinx()
    bars2 = ax2.bar(
        x + width/2,
        df_selected["pos_reviews"],
        width,
        label="Positive Reviews (%)",
        color="#DD8452"
    )

    ax2.set_ylabel("Positive Reviews (%)")

    # add value labels on top of bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 1000,
                 f"{int(height)}", ha='center', fontsize=8)

    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 1,
                 f"{height:.1f}%", ha='center', fontsize=8)

    # title
    plt.title("Comparison of Game Popularity and Player Satisfaction (Low → High)")

    # merge legends
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1 + h2, l1 + l2, loc='upper left')

    plt.tight_layout()
    plt.show()
    plt.close('all')

if __name__ == "__main__":
    generate_graph()
