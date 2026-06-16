# Tell the program to look for a file named contacts.json.
# If the file exists: Open it, read the data, and load it into your main contacts variable.
# If the file does not exist (like the first time you run it): Create a brand-new,
# empty dictionary for your contacts.
import json
import os


def load_contacts(file):
    if os.path.exists(file):
        # File exists → load it
        with open(file, "r") as f:
            contacts = json.load(f)
    else:
        # File does NOT exist → create empty dictionary
        contacts = {}

    return contacts


def add_contact(contacts):
    name = input("Enter name: ").strip()

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {"phone": phone, "email": email}

    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("----------------------")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("\nContact Found:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def save_contacts(file, contacts):
    with open(file, "w") as f:
        json.dump(contacts, f, indent=4)


def main():
    file = "contacts.json"
    contacts = load_contacts(file)
    print(contacts)

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            save_contacts(file, contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
