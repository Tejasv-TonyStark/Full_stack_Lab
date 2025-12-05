'''•  Task: Expense Tracker 
•	Description: Build a program to track daily expenses. Users can add expenses (description and amount) and view the total spent.
•	Requirements: 
o	Store expenses in a list of tuples (e.g., ("Coffee", 5.50)).
o	Write functions for: 
	Adding an expense (prompt for description and amount).
	Calculating and displaying the total of all expenses.
	Displaying all expenses.
o	Validate that the amount is a positive number using try-except.
o	Use a menu-driven interface (options: add, view, total, exit).
•	Tested Skills: Lists, tuples, functions, error handling, user input, basic calculations
'''


expenses = []   

def add_expense():
    desc = input("Enter expense description: ")
    amt = input("Enter amount: ")

    try:
        amt = float(amt)
        if amt > 0:
            expenses.append((desc, amt))
            print("Expense added")
        else:
            print("Amount must be positive")
    except:
        print("Invalid amount")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet")
    else:
        for e in expenses:
            print(e[0], "-", e[1])

def total_expenses():
    total = 0
    for e in expenses:
        total += e[1]
    print("Total spent =", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Amount")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_expense()
    elif ch == "2":
        view_expenses()
    elif ch == "3":
        total_expenses()
    elif ch == "4":
        print("Bye")
        break
    else:
        print("Wrong option")