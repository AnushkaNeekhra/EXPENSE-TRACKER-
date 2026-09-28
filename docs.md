# Expense Tracker

## Project Title
📈Expense Tracker

## Overview of the Project
The Expense Tracker is a Python-based application designed to help users record their day-to-day expenses, organize spending by category, and monitor their monthly budget. The system is simple, lightweight, and beginner-friendly, making it suitable for students and individuals who want to manage personal finances more effectively.

This project was developed to improve programming skills while solving a practical real-world problem related to personal budgeting.

## Problem Statement
Many students and individuals struggle to keep track of their spending because they do not maintain a proper record of expenses. This usually leads to overspending, poor financial planning, and difficulty in understanding where the money is going. A simple tracking system is needed so that users can monitor their spending habits, control their finances, and stay within their monthly budget.

## Objectives
The main objectives of this project are:
- To allow users to add expenses easily
- To classify expenses into different categories
- To save expense records for future reference
- To calculate total monthly expenditure
- To identify the amount of money left in the budget
- To display category-wise expense summaries
- To help users manage their budget more efficiently

## Scope of the Project
The scope of this project includes:
- adding expense records
- selecting categories
- storing data in a file
- calculating total spending
- checking remaining budget
- determining budget left per day
- showing spending summary by category

The project is limited to personal expense tracking and does not include advanced financial analysis, cloud integration, or online database support.

## Target Users
The main target users of this project are:
- college students
- beginners learning Python
- people who want to manage personal expenses
- users who want a simple budget tracker

## Features
- Add new expense records
- Select an expense category
- Save expenses in a CSV file
- Calculate total spending
- Check remaining monthly budget
- Show daily remaining budget
- View expenses by category
- Simple command-line interface

## Functional Requirements
The system must:
- allow the user to enter an expense name
- allow the user to enter an expense amount
- allow the user to select an expense category
- save each expense entry into a file
- calculate the total of all recorded expenses
- calculate the remaining budget after subtracting the total expenses
- display category-wise total spending
- allow the user to add multiple expenses in a session
- handle invalid input gracefully

## Non-Functional Requirements
The non-functional requirements are:
- The system should be easy to use
- The system should respond quickly to user input
- The program should be simple and clear for beginners
- The code should be maintainable and readable
- Data should be stored safely in a local file
- The system should handle invalid inputs without crashing

## Technologies / Tools Used
- Python
- VS Code
- CSV file handling
- Object-oriented programming
- Command-line interface
- Basic file storage and calculation logic

## System Architecture Diagram
The project follows a simple client-side command-line architecture.

```text
+----------------------+
|     User Interface   |
|   (Expense_Tracker)  |
+----------+-----------+
           |
           v
+----------+-----------+
|  Input Validation    |
|  Expense Entry       |
+----------+-----------+
           |
           v
+----------+-----------+
|  Business Logic      |
|  Budget Services     |
|  Expense Calculation |
+----------+-----------+
           |
           v
+----------+-----------+
|  Storage Layer       |
|  expenses_record.csv |
+----------------------+
# Process flow / Workflow Diagram 
Start
  |
  v
Enter expense name
  |
  v
Enter expense amount
  |
  v
Select category
  |
  v
Save expense to file
  |
  v
Ask: Add another expense?
  |-- Yes --> repeat expense entry
  |
  v
No
  |
  v
Enter monthly budget
  |
  v
Calculate total expenses
  |
  v
Calculate remaining budget
  |
  v
Display summary
  |
  v
End

# UML Diagram (Use Case Diagram)
+-------------------+
|      User         |
+-------------------+
         |
         v
+---------------------------------+
|        Expense Tracker          |
|---------------------------------|
| 1. Add Expense                  |
| 2. Select Category              |
| 3. Save Expense                 |
| 4. View Total Spending          |
| 5. View Remaining Budget        |
| 6. View Category Summary        |
+---------------------------------+

# UML Diagram (Use Class Diagram)
+---------------------+
|       Expense        |
+---------------------+
| - name: str          |
| - amount: float      |
| - category: str      |
+---------------------+
| + __init__()         |
+---------------------+

        ^
        |
        |
+---------------------+
|   BudgetService      |
+---------------------+
| + categorize_expenses() |
| + get_remaining_days_in_month() |
| + display_summary() |
+---------------------+

UML Diagram (Sequence Diagram )
User     ExpenseTracker     Expense      BudgetService
 |             |               |             |
 |-- Add Expense -->|               |             |
 |             |-- create ->    |             |
 |             |               |-- save -->  |
 |             |<-- success --- |             |
 |             |               |             |
 |-- Enter Budget -->|               |             |
 |             |-- load data -->|             |
 |             |               |             |
 |             |-- calculate -->|             |
 |             |<-- summary ----|             |

 #Database / Storage Design
This project uses a simple local CSV file for storage rather than a relational database. The system is lightweight and beginner-friendly.

#Storage File
C:\Users\ANUSHKA NEEKHRA\PYTHON_PROJECT1\expenses_record.csv

#Sample Record Format
Groceries,250.00,Groceries
Movie,120.00,Entertainment
Transport,80.00,Transport

# ER Diagram 
+------------------+       stores       +------------------+
|      User        | -----------------> |     Expense      |
+------------------+                    +------------------+
| user_id          |                    | id               |
| name             |                    | name             |
| budget           |                    | amount           |
+------------------+                    | category         |
                                        +------------------+

# Schema Design 
The data model is simple:

Expense Name
Expense Amount
Expense Category

Sample schema:
Expense (
    name: string,
    amount: float,
    category: string
)
# Testing Instructions 
1.Open the project folder in VS Code.
2. Run the program using:
python Expense_Tracker.py
3.Enter an expense name.
4.Enter the amount.
5.Select the category.
6.Add another expense if needed.
7.Enter the monthly budget.
8.Check whether the total, remaining budget, and category summary are correct.
# Dataset Description
Not applicable for this project because it is a simple personal expense management application and does not use an external dataset.

#Model Selection Rationale
Not applicable for this project because no machine learning model is used.

#Evaluation Methodology
Not applicable for this project because this is not an ML-based system. The project is validated by checking:
user input handling
correct calculations
file storage behavior
summary output accuracy
#Conclusion
The Expense Tracker is a simple and practical project that helps users manage their personal finances more effectively. It demonstrates core Python concepts such as input handling, file operations, calculations, and object-oriented programming. The project is ideal for beginner-level learning and can be extended in the future with additional features such as monthly reports, charts, and a graphical interface.

```md
# Statement of the Project

## Problem Statement
Managing daily expenses is a common problem for students, especially when they are living on a limited budget. Many people find it difficult to keep track of where their money is being spent, which can lead to overspending and poor financial planning. Students often have to manage expenses like groceries, travel, food, entertainment, and study-related costs, and without a proper tracking system, it becomes hard to know how much money is left.

This project aims to solve that problem by creating a simple expense tracking system that helps users record expenses, classify them into categories, and monitor their monthly budget. The system is designed to make budgeting easier and more organized for students and other users who want to control their spending.

## Scope of the Project
The scope of this project is limited to a simple and user-friendly expense tracking application. It includes:
- adding expenses
- selecting an expense category
- saving records in a file
- calculating total monthly spending
- checking remaining budget
- displaying category-wise summaries
- showing budget left per day

This project does not aim to provide advanced financial analysis or a full business accounting system. It is a beginner-level project focused on basic Python programming and practical budget management.

## Target Users
The primary target users of this project are:
- college students
- beginners learning Python
- people who want to manage personal expenses
- users who want a simple monthly budget tracker

This project is especially useful for students who want to track spending on food, transport, books, entertainment, and other daily needs.

## High-Level Features
The high-level features of the project are:
- Expense entry: users can enter the name and amount of an expense
- Category selection: users can assign each expense to a category
- Data storage: expenses are saved in a file for later use
- Budget calculation: total spending is calculated automatically
- Remaining budget check: users can see how much money is left
- Daily budget tracking: users can know how much they can spend per day
- Summary display: the system shows total cost and category-wise spending

## Conclusion
This project is a simple but useful application designed to help students and beginners understand how to build a practical tool using Python. It focuses on solving a real-world problem related to money management while also helping learners practice important programming concepts such as input handling, file operations, classes, functions, and calculation logic.

