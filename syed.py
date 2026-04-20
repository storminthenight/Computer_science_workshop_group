import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel(r"C:\Users\syed\Downloads\dataset will be use.xlsx")


data.columns = ["year", "game_name", "id", "followers"]

data = data.iloc[1:]


data["year"] = pd.to_numeric(data["year"], errors="coerce")
data["followers"] = pd.to_numeric(data["followers"], errors="coerce")


data = data.dropna(subset=["year", "game_name", "followers"])


data["year"] = data["year"].astype(int)
data["followers"] = data["followers"].astype(int)


games = data["game_name"].unique()[:2]
filtered = data[data["game_name"].isin(games)]

plt.figure(figsize=(10, 6))

for game in games:
    game_data = filtered[filtered["game_name"] == game]
    plt.plot(
        game_data["year"],
        game_data["followers"],
        marker="o",
        linestyle="-",
        label=game
    )

plt.grid(True)
plt.xlabel("Year")
plt.ylabel("Followers")
plt.title("Followers over time for two games")
plt.legend()
plt.tight_layout()
plt.show()

