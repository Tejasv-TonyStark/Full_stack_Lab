'''•	Description: Create a program that manages a simple contact book. Users can add a contact (name and phone number), view all contacts, and search for a contact by name.
•	Requirements: 
o	Store contacts in a list of dictionaries (e.g., {"name": "Alice", "phone": "1234567890"}).
o	Write functions for: 
	Adding a contact (prompt for name and phone).
	Displaying all contacts.
	Searching for a contact by name (case-insensitive).
o	Validate phone numbers (e.g., must be numeric, 10 digits).
o	Use a while loop for a menu-driven interface (options: add, view, search, exit).
•	Tested Skills: Lists, dictionaries, functions, user input, string manipulation, loops.
'''

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    if phone.isdigit() and len(phone) == 10:
        contacts.append({"name": name, "phone": phone})
        print("Contact added")
    else:
        print("Invalid phone number. It must be 10 digits.")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts available")
    else:
        for c in contacts:
            print(c["name"], "-", c["phone"])

def search_contact():
    n = input("Enter name to search: ").lower()
    found = False
    for c in contacts:
        if c["name"].lower() == n:
            print("Found:", c["name"], c["phone"])
            found = True
            break

    if not found:
        print("Contact not found")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        view_contacts()
    elif ch == "3":
        search_contact()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option")