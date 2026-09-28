# Expense Tracker

##Project Title
Expense Tracker

##Overview of the Project
The Expense Tracker is a Python-based project designed to help users track their daily expenses, organize them into categories, and monitor their monthly budget. The application allows users to enter expense details, save them to a file, and view their total spending, remaining budget, and category-wise summary.

This project was created to improve Python programming skills while building a practical application for personal finance management.

## Features
- Add new expenses
- Choose an expense category
- Save expense records in a CSV file
- Calculate total spending
- Track remaining monthly budget
- View budget left per day
- Show category-wise expense summary
- Simple and beginner-friendly project structure

## Technologies / Tools Used
- Python
- VS Code
- CSV file handling
- Object-oriented programming
- Basic Python functions and loops
- Command-line interface

## Project Structure
- `Expense_Tracker.py` - main application file
- `Expense.py` - contains the expense class
- `Budget_Services.py` - handles budget and summary calculations
- `expenses_record.csv` - stores all expense records
- `README.md` - project documentation

## Installation
1. Make sure Python is installed on your system.
2. Download or clone the project folder.
3. Open the project folder in VS Code or any Python editor.

## Steps to Run the Project
Open the terminal in the project folder and run:

```bash
python Expense_Tracker.py

"""If you are using Python 3 specifically, you can also run:
python3 Expense_Tracker.py"""
#Instructions for Testing
Run the application using the command above.
Enter an expense name.
Enter the amount of the expense.
Select a category.
Choose whether to add another expense.
Enter your monthly budget.
Check the summary displayed in the terminal.
Verify that:
total expense value is correct
remaining budget is calculated correctly
category-wise summary is shown correctly"""
#Example Test Case:

#Example input:
Expense Name: Groceries
Amount: 250
Category: Groceries
Add another expense: Yes
Expense Name: Movie
Amount: 120
Category: Entertainment
Monthly Budget: 2000

#Example output:
Total Expense Value: $370.00
Remaining Budget: $1630.00
Remaining Budget per Day: $54.33
Category-wise summary:
Groceries: $250.00
Entertainment: $120.00

#Conclusion
This project is a beginner-friendly Python application that helps users manage daily expenses and budget planning. It is useful for learning Python basics, file storage, and practical project development.

#Future Improvements
Add date and time for each expense
Improve category reporting
Add graphs and charts
Add a graphical user interface
Add better validation and error handling