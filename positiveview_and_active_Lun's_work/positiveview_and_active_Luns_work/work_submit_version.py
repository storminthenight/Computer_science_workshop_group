import pandas as pd
import matplotlib.pyplot as plt

# read Excel
file_path = "/Users/liwalun/Computer_science_workshop_group-main/positiveview_and_active_Luns_work/dataset will be use.xlsx"

df = pd.read_excel(file_path,
                   sheet_name="vgi_game_stats",
                   header=1)

# clean column names
df.columns = df.columns.str.strip()

# -------- clean data --------
df["active_plyrs(24hrs)"] = pd.to_numeric(df["active_plyrs(24hrs)"], errors='coerce')

df["pos_reviews"] = df["pos_reviews"].astype(str).str.replace('%', '', regex=False)
df["pos_reviews"] = pd.to_numeric(df["pos_reviews"], errors='coerce')

# -------- select 4 games --------
games = [
    "War Thunder",
    "VRChat",
    "Phasmophobia",
    "No Man's Sky"
]

df_selected = df[df["game_name"].isin(games)]

# sort by player count
df_selected = df_selected.sort_values(by="active_plyrs(24hrs)")

# -------- plot --------
fig, ax1 = plt.subplots(figsize=(9, 5))

# first line (player count)
ax1.plot(df_selected["game_name"],
         df_selected["active_plyrs(24hrs)"],
         marker='o',
         label="Active Players")

ax1.set_ylabel("Active Players (24hrs)")
ax1.set_xlabel("Game Name")

# second line (review %)
ax2 = ax1.twinx()

ax2.plot(df_selected["game_name"],
         df_selected["pos_reviews"],
         marker='s',
         linestyle='--',
         label="Positive Reviews (%)")

ax2.set_ylabel("Positive Reviews (%)")

# title
plt.title("Comparison of Popularity vs Player Satisfaction")

# merge legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
plt.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# tidy up
plt.xticks(rotation=20)
ax1.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()