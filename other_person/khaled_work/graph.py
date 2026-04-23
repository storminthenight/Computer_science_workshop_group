import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Khaled Graph")
    # if you want to run this as a script, you can call main() here

    # Load dataset
    df = pd.read_excel("/Users/liwalun/Computer_science_workshop_group-main/other_person/data_set/dataset will be use.xlsx",
                    sheet_name="vgi_game_stats",
                    header=1)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert to numeric
    df["units_sold"] = pd.to_numeric(df["units_sold"], errors='coerce')
    df["active_plyrs(24hrs)"] = pd.to_numeric(df["active_plyrs(24hrs)"], errors='coerce')

    # Drop missing values
    df = df.dropna(subset=["units_sold", "active_plyrs(24hrs)", "game_name"])

    # Top 5 games
    top_games = df.sort_values(by="units_sold", ascending=False).head(5)

    # Plot
    fig, ax1 = plt.subplots(figsize=(10,5))

    # Bars
    bars = ax1.bar(top_games["game_name"], top_games["units_sold"])
    ax1.set_ylabel("Units Sold")

    # Line (make it stronger)
    ax2 = ax1.twinx()
    ax2.plot(top_games["game_name"],
            top_games["active_plyrs(24hrs)"],
            marker='o',
            linestyle='--',
            linewidth=3)

    ax2.set_ylabel("Active Players (24hrs)")

    # Title
    plt.title("Game Sales vs Current Popularity")

    # Legend
    ax1.legend(["Units Sold"], loc="upper left")
    ax2.legend(["Active Players"], loc="upper right")

    # Style
    plt.xticks(rotation=30)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("graph.png")
    plt.show()
