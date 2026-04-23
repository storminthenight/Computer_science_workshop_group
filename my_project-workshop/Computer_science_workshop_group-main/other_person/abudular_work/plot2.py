import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Abdular Graph 2")
    # if you want to run this as a script, you can call main() here

    data = pd.read_excel("/Users/liwalun/Computer_science_workshop_group-main/other_person/data_set/dataset will be use.xlsx")

    data.columns = ["year", "game_name", "id", "searches"]
    data = data.iloc[1:]
    data["searches"] = data["searches"].astype(int)

    total_searches = data.groupby("game_name")["searches"].sum()
    top_6 = total_searches.sort_values(ascending=False).head(6)

    plt.figure(figsize=(10,5))
    top_6.plot(kind="bar")

    plt.xlabel("Game Name")
    plt.ylabel("Total Searches")
    plt.title("Top 6 Most Searched Games")

    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()

    plt.show()

