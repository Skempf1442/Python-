# crud_app.py

def main_menu():
    """Display the main menu to the user and get their selection."""
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

def check():
    """Check if the customer list file exists and read its content."""
    try:
        with open("customer_list.txt", 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

def create():
    """Create a new entry and save it to the customer list."""
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

def read():
    """Display an entry by the last name."""
    customer = check()
    if not customer:
        print("No entries available.")
        return
    lname = input("Enter the last name of the customer you are looking for: ")
    found = False
    for entry in customer:
        if lname in entry:
            print("Entry found:", entry.strip())
            found = True
    if not found:
        print("No entry found for the given last name.")

def update():
    """Update an existing entry."""
    customer = check()
    if not customer:
        print("No entries available.")
        return
    lname = input("Enter the last name of the customer you want to update: ")
    found = False
    for i, entry in enumerate(customer):
        if lname in entry:
            print("Entry found:", entry.strip())
            fname = input("Enter new first name: ")
            lname_new = input("Enter new last name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            customer[i] = f"{fname}, {lname_new}, {phone}, {email}\n"
            found = True
            break
    if found:
        save(customer)
        print("Entry updated.")
    else:
        print("No entry found for the given last name.")

def delete():
    """Delete an existing entry."""
    customer = check()
    if not customer:
        print("No entries available.")
        return
    lname = input("Enter the last name of the customer you want to delete: ")
    found = False
    for i, entry in enumerate(customer):
        if lname in entry:
            print("Entry found and deleted:", entry.strip())
            del customer[i]
            found = True
            break
    if found:
        save(customer)
    else:
        print("No entry found for the given last name.")

def save(output):
    """Save the customer list back to the file."""
    with open("customer_list.txt", 'w') as file:
        file.writelines(output)
    print("File updated.")

def main():
    """Main function to run the CRUD application."""
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
