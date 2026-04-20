import pandas as pd
import matplotlib.pyplot as plt

 
# This Reads the CSV file and makes it into a table so the data can be used
df = pd.read_csv("interest_over_time.csv")


# This finds the most popular title per year by number of searches
top_per_year = df.loc[df.groupby('year')['num_searches'].idxmax()].sort_values('year')
 

# This sets the size of the chart width=14 height=8 inch
plt.figure(figsize=(14, 8))


#This creates bar chart and lables it adding years to x-axis and and the search count on the y-axis and the converts the numbers to text
plt.bar(top_per_year['year'].astype(str), top_per_year['num_searches'], width=0.5)

# This loops through the csv and finds the years,names and search count using the zip and that then pairs them up so they can go in the graph
for year, name, count in zip(top_per_year['year'].astype(str), top_per_year['name'], top_per_year['num_searches']):
    plt.text(year,   # x position 
             count,  # y position 
             f"{name}\n({int(count)})",  # This inserts name and then adds the search count without decimals
             ha='center', fontsize=8)    # This centres the text and makes in font size 8
 

plt.xlabel("Year")
 
plt.ylabel("Number of Searches")

plt.title("Most Popular VR Title per Year")

plt.savefig("vr_most_popular_per_year.png",)
 
plt.show()