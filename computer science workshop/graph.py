import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_excel("dataset will be use.xlsx")

# Fix columns
data.columns = ["year", "game_name", "id", "searches"]

# Remove bad row
data = data.iloc[1:]

# Convert to numbers
data["searches"] = pd.to_numeric(data["searches"], errors='coerce')

# Group by game (average searches)
avg_searches = data.groupby("game_name")["searches"].mean()

# Take top 10 games
top10 = avg_searches.sort_values(ascending=False).head(10)

# Plot
plt.figure()
plt.bar(top10.index, top10.values)

plt.xticks(rotation=60)
plt.xlabel("Game Name")
plt.ylabel("Average Searches")
plt.title("Top 10 Games by Average Search Interest")

plt.grid(axis='y')
plt.tight_layout()   # <-- THIS fixes the cut labels

# Save
plt.savefig("graph.png")

plt.show()