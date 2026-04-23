import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Charlie Graph")

    # Read CSV
    df = pd.read_csv("/Users/liwalun/Computer_science_workshop_group-main/other_person/charlie_work/interest_over_time.csv")

    # Find most popular title per year
    top_per_year = df.loc[df.groupby('year')['num_searches'].idxmax()].sort_values('year')

    # Plot
    plt.figure(figsize=(14, 8))
    plt.bar(top_per_year['year'].astype(str), top_per_year['num_searches'], width=0.5)

    # Add labels
    for year, name, count in zip(top_per_year['year'].astype(str), top_per_year['name'], top_per_year['num_searches']):
        plt.text(year, count, f"{name}\n({int(count)})", ha='center', fontsize=8)

    plt.xlabel("Year")
    plt.ylabel("Number of Searches")
    plt.title("Most Popular VR Title per Year")
    plt.tight_layout()
    plt.show()
