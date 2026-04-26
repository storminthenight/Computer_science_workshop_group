README – Main Function Folder

This folder contains the main program used to run all group visualisations.  
The main function provides a menu system that allows the user to select and display different graphs created by each group member.

Requirements  
Before running the program, make sure the following are installed:

- Python 3.x  
- pandas  
- matplotlib  
- numpy  
- openpyxl  

You can install the required packages using:

pip install pandas matplotlib numpy openpyxl

How to Run the Program

1. Download or clone the repository:
Computer_science_workshop_group-main.zip

2. Extract the zip file.

3. Navigate to the main function folder.

4. Open terminal / command prompt in this folder.

5. Run the main program:

python main.py

Program Behaviour

- The program will display a menu in the terminal  
- Each option represents a visualisation created by a group member  
- Enter the number to select a graph  
- The selected graph will open in a new window  
- Close the graph window to return to the main menu  
- You can continue selecting different visualisations  

Structure

main.py  
menu system for selecting visualisations  

init.py  
allows modules to be imported  

visualisation files  
individual graphs from group members  

Notes

- All visualisations are implemented as functions using def main()  
- The main menu imports each visualisation module  
- Closing a graph returns control to the menu  
- Invalid input is handled to prevent crashes  

This folder is used to integrate all individual visualisations into a single interactive program.
