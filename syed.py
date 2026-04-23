import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel(r"C:\Users\syed\Downloads\dataset will be use.xlsx")


data.columns = ["release_date", "game_name", "req_age", "recommendations"]

data = data.iloc[1:]


data["release_date"] = pd.to_numeric(data["release_date"], errors="coerce")
data["recommendations"] = pd.to_numeric(data["recommendations"], errors="coerce")


data = data.dropna(subset=["release_date", "game_name", "recommendations"])


data["release_date"] = data["release_date"].astype(int)
data["recommendations"] = data["recommendations"].astype(int)


games = data["game_name"].unique()[:2]
filtered = data[data["game_name"].isin(games)]

plt.figure(figsize=(10, 6))

for game in games:
    game_data = filtered[filtered["game_name"] == game]
    plt.plot(
        game_data["release_date"],
        game_data["recommendations"],
        marker="o",
        linestyle="-",
        label=game
    )

plt.grid(True)
plt.xlabel("Release Date")
plt.ylabel("Recommendations")
plt.title("Release Date and Recommendations for Two Games")
plt.legend()
plt.tight_layout()
plt.show()

