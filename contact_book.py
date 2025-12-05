def validate_phone(phone: str) -> bool:
    """Return True if phone is numeric and 10 digits."""
    return phone.isdigit() and len(phone) == 10


def add_contact(contacts: list, name: str | None = None, phone: str | None = None) -> None:
    """Add a contact to the contacts list. If name or phone are None, prompt the user.

    The function validates the phone (numeric, 10 digits). It appends a dict to `contacts`.
    """
    if name is None:
        name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty. Contact not added.")
        return

    if phone is None:
        phone = input("Enter phone number (10 digits): ").strip()

    while not validate_phone(phone):
        print("Invalid phone. Must be numeric and 10 digits.")
        phone = input("Enter phone number (10 digits): ").strip()

    contacts.append({"name": name, "phone": phone})
    print(f"Contact added: {name} - {phone}")


def display_contacts(contacts: list) -> None:
    """Print all contacts in a readable format."""
    if not contacts:
        print("No contacts available.")
        return

    print("Contacts:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")


def search_contact(contacts: list, query: str) -> list:
    """Search for contacts by name (case-insensitive). Returns list of matches."""
    q = query.strip().lower()
    matches = [c for c in contacts if q in c["name"].lower()]
    if matches:
        print(f"Found {len(matches)} match(es):")
        for c in matches:
            print(f"- {c['name']} - {c['phone']}")
    else:
        print("No contacts found matching that name.")

    return matches


def main() -> None:
    contacts: list[dict] = []

    menu = (
        "\nContact Book - choose an option:\n"
        "1. Add contact\n"
        "2. View all contacts\n"
        "3. Search contact by name\n"
        "4. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Enter option (1-4): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            name = input("Enter name to search: ").strip()
            if name:
                search_contact(contacts, name)
            else:
                print("Search query cannot be empty.")
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
