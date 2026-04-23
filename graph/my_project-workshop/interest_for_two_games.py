import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
excel_file = 'dataset will be used.xlsx'

# Read the interest_over_time sheet (skip first 2 rows as they contain metadata)
interest_df = pd.read_excel(excel_file, sheet_name='interest_over_time', header=2)

# Read the vgi_game_stats sheet (skip first 2 rows as they contain metadata)
stats_df = pd.read_excel(excel_file, sheet_name='vgi_game_stats', header=2)

# Clean up column names
interest_df.columns = ['year', 'name', 'id', 'num_searches']
stats_df.columns = ['game_name', 'active_plyrs_min', 'active_plyrs_24hrs', 'pos_reviews', 
                    'gross_rev', 'units_sold', 'avg_time_total', 'avg_time_2weeks']

# Filter for top grossing games (excluding NaN and non-numeric)
stats_df['gross_rev_numeric'] = pd.to_numeric(stats_df['gross_rev'].str.replace('$', '').str.replace('m', ''), errors='coerce')
top_games = stats_df.nlargest(10, 'gross_rev_numeric')[['game_name', 'gross_rev_numeric']]
print("Top 10 games by gross revenue:")
print(top_games)

# Get the top 5 games
top5_game_names = top_games['game_name'].head(5).tolist()
print(f"\nTop 5 games: {top5_game_names}")

# Extract interest data for these games
fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#ff7f00', '#984ea3']

for i, game_name in enumerate(top5_game_names):
    # Filter data for this game
    game_data = interest_df[interest_df['name'] == game_name].copy()
    
    if not game_data.empty:
        # Sort by year
        game_data = game_data.sort_values('year')
        
        # Get the revenue for annotation
        revenue = top_games[top_games['game_name'] == game_name]['gross_rev_numeric'].values[0]
        
        ax.plot(game_data['year'], game_data['num_searches'], 
                marker='o', linewidth=2.5, markersize=8,
                label=f"{game_name} (${revenue:.1f}M)", 
                color=colors[i % len(colors)])

ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Searches', fontsize=14, fontweight='bold')
ax.set_title('Search Interest Over Time for Top Grossing VR Games', 
             fontsize=16, fontweight='bold', pad=20)

ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xticks(range(2010, 2025))
ax.set_xticklabels(range(2010, 2025), rotation=45)

plt.tight_layout()
plt.show()