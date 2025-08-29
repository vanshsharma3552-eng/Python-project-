import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact '{name}' added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n=== Contact List ===")
        for idx, c in enumerate(contacts, 1):
            print(f"{idx}. {c['name']} | {c['phone']}")

# Search contact by name or phone
def search_contact(contacts):
    keyword = input("Search by name or phone: ").lower()
    found = [c for c in contacts if keyword in c['name'].lower() or keyword in c['phone']]
    if found:
        for c in found:
            print("\n--- Contact Found ---")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
    else:
        print("No contact found.")

# Update contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c['name'].lower() == name:
            print("Leave field blank to keep current value.")
            new_name = input(f"New name [{c['name']}]: ") or c['name']
            new_phone = input(f"New phone [{c['phone']}]: ") or c['phone']
            new_email = input(f"New email [{c['email']}]: ") or c['email']
            new_address = input(f"New address [{c['address']}]: ") or c['address']

            c.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated.")
            return
    print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name:
            confirm = input(f"Are you sure you want to delete '{c['name']}'? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(i)
                print("Contact deleted.")
                return
    print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
