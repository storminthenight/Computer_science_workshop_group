import sys
import os


## This is the main function that allows users to select and display different graphs created by various team members.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import Abdulrahman_work.plot
import Abdulrahman_work.plot2
import charlie_work.vrmostpopularbyyear
import khaled_work.graph
import syed_work.syed
import Kens_work.ken_graph #it will effect the loop if we use this graph, so I comment it out for now
import positiveview_and_active_Luns_work.work_submit_version

graphs = {
    1: Abdulrahman_work.plot.main,
    2: Abdulrahman_work.plot2.main,
    3: charlie_work.vrmostpopularbyyear.main,
    4: khaled_work.graph.main,
    5: syed_work.syed.main,
    #6: Kens_work.ken_graph.main,
    6: positiveview_and_active_Luns_work.work_submit_version.main
}

def menu():
    print("==============================")
    print("   VIDEO GAME GRAPH SYSTEM")
    print("==============================")
    print("1. Abdulrahman – interest for the two games changes over time")
    print("2. Abdulrahman – Top 6 Most Searched Games")
    print("3. Charlie – Most Popular VR Title per Year")
    print("4. Khaled – Game Sales vs Current Popularity")
    print("5. Syed – Followers Over Time")
 #  print("6. Ken – Custom Graph")
    print("6. Lun – Popularity vs Satisfaction")
    print("0. Exit")
    print("------------------------------")

def main():
    while True:
        menu()
        choice_str = input("Enter a number (0-7): ").strip()

        if not choice_str.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice_str)

        if choice == 0:
            print("Bye.")
            break

        if choice in graphs:
            print(f"Graph {choice} is displaying...")
            graphs[choice]()   # call the corresponding graph function

            # to prevent the graph from closing immediately, we can ask the user to press Enter after viewing the graph
            input("Press Enter to return to menu…")

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

