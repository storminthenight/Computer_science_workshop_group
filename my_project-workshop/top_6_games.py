import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("dataset will be used.xlsx")
data.columns = ["year", "game_name", "id", "searches"]
data = data.iloc[1:]
data["searches"] = data["searches"].astype(int)

# groups the data by game name and adds together all search values for each game
total_searches = data.groupby("game_name")["searches"].sum()

# sorts the games from highest to lowest searches and selects the top six.
top_6 = total_searches.sort_values(ascending=False).head(6)

# chart size
plt.figure(figsize=(10,5))

# bar chart
top_6.plot(kind="bar")

plt.xlabel("Game Name")
plt.ylabel("Total Searches")
plt.title("Top 6 Most Searched Games")

#rotaion for the lines
plt.xticks(rotation=45)
# horizental lines
plt.grid(axis='y')
plt.tight_layout()
plt.show()