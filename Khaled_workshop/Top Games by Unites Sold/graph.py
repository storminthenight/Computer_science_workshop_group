import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("dataset will be use.xlsx",
                   sheet_name="vgi_game_stats",
                   header=1)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert to numeric
df["units_sold"] = pd.to_numeric(df["units_sold"], errors='coerce')

# Drop missing values
df = df.dropna(subset=["units_sold", "game_name"])

# Top 5 games by units sold
top_games = df.sort_values(by="units_sold", ascending=False).head(5)

# Plot
plt.figure(figsize=(10,5))
plt.bar(top_games["game_name"], top_games["units_sold"])

# Labels
plt.title("Top Games by Units Sold")
plt.xlabel("Game Name")
plt.ylabel("Units Sold")

# Style
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("graph.png")
plt.show()