'''Task: File-Based To-Do List 
•	Description: Write a program that lets users add and view to-do items, saving them to a file so they persist between runs.
•	Requirements: 
o	Store to-do items as a list of strings.
o	Write functions for: 
	Adding a to-do item.
	Reading and displaying all to-do items from a file (todos.txt).
	Saving the to-do list to the file after each addition.
o	Handle file errors (e.g., file not found) using try-except.
o	Use a simple command-line interface (options: add, view, exit).
•	Tested Skills: File I/O, lists, functions, error handling, user input.
'''

filename = "todos.txt"

def add_todo():
    todo = input("Enter a to-do item: ")
    try:
        with open(filename, "a") as f:
            f.write(todo + "\n")
        print("Added")
    except:
        print("Error writing to file")

def view_todos():
    try:
        with open(filename, "r") as f:
            data = f.readlines()
            if len(data) == 0:
                print("No to-do items")
            else:
                for t in data:
                    print("-", t.strip())
    except FileNotFoundError:
        print("File not found, no items yet")

while True:
    print("\n1. Add To-Do")
    print("2. View To-Do List")
    print("3. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_todo()
    elif ch == "2":
        view_todos()
    elif ch == "3":
        print("Bye")
        break
    else:
        print("Invalid option")