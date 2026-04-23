import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = "/Users/liwalun/Computer_science_workshop_group-main/other_person/data_set/dataset will be use.xlsx"

    df_raw = pd.read_excel(file_path, sheet_name="vgi_game_stats", header=None)
    df = pd.read_excel(file_path, sheet_name="vgi_game_stats", header=1)

    df.columns = df.columns.str.strip()
    df["active_plyrs(24hrs)"] = pd.to_numeric(df["active_plyrs(24hrs)"], errors='coerce')

    df["pos_reviews"] = df["pos_reviews"].astype(str).str.replace('%', '', regex=False)
    df["pos_reviews"] = pd.to_numeric(df["pos_reviews"], errors='coerce')

    df["game_name"] = df["game_name"].str.strip()

    games = ["War Thunder", "VRChat", "Phasmophobia", "No Man's Sky"]
    df_selected = df[df["game_name"].isin(games)]
    df_selected = df_selected.sort_values(by="active_plyrs(24hrs)")

    fig, ax1 = plt.subplots(figsize=(9, 5))

    ax1.plot(df_selected["game_name"],
             df_selected["active_plyrs(24hrs)"],
             marker='o',
             label="Active Players")

    ax1.set_ylabel("Active Players (24hrs)")
    ax1.set_xlabel("Game Name")

    ax2 = ax1.twinx()
    ax2.plot(df_selected["game_name"],
             df_selected["pos_reviews"],
             marker='s',
             linestyle='--',
             label="Positive Reviews (%)")

    ax2.set_ylabel("Positive Reviews (%)")

    plt.title("Comparison of Popularity vs Player Satisfaction")

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    plt.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    plt.xticks(rotation=20)
    ax1.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

   # Close the plot to free up memory
    plt.close('all')
    return
