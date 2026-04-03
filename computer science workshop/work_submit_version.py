import pandas as pd
import matplotlib.pyplot as plt

# 讀取 Excel
df = pd.read_excel("dataset will be use.xlsx",
                   sheet_name="vgi_game_stats",
                   header=1)

# 清理欄位
df.columns = df.columns.str.strip()

# -------- 清理數據 --------
df["active_plyrs(24hrs)"] = pd.to_numeric(df["active_plyrs(24hrs)"], errors='coerce')

df["pos_reviews"] = df["pos_reviews"].astype(str).str.replace('%', '', regex=False)
df["pos_reviews"] = pd.to_numeric(df["pos_reviews"], errors='coerce')

# -------- 選擇4隻遊戲 --------
games = [
    "War Thunder",
    "VRChat",
    "Phasmophobia",
    "No Man's Sky"
]

df_selected = df[df["game_name"].isin(games)]

# 排序（按玩家數）
df_selected = df_selected.sort_values(by="active_plyrs(24hrs)")

# -------- 畫圖 --------
fig, ax1 = plt.subplots(figsize=(9, 5))

# 第一條線（玩家數）
ax1.plot(df_selected["game_name"],
         df_selected["active_plyrs(24hrs)"],
         marker='o',
         label="Active Players")

ax1.set_ylabel("Active Players (24hrs)")
ax1.set_xlabel("Game Name")

# 第二條線（評價 %）
ax2 = ax1.twinx()

ax2.plot(df_selected["game_name"],
         df_selected["pos_reviews"],
         marker='s',
         linestyle='--',
         label="Positive Reviews (%)")

ax2.set_ylabel("Positive Reviews (%)")

# 標題
plt.title("Comparison of Popularity vs Player Satisfaction")

# 合併 legend（關鍵🔥）
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
plt.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# 美化
plt.xticks(rotation=20)
ax1.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()