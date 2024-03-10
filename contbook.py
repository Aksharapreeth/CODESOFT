contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added successfully.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_contacts():
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts found.")

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '3':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please choose again.")
