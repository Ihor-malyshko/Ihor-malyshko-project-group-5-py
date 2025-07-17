# import ui_helpers
import storage  

from AddressBook import AddressBook, Record

# -------------------- ФУНКЦІЇ ДЛЯ КОМАНД --------------------

def add_contact(book, args):
    print("Adding new contact (or press Enter to cancel)")

    name = input("Enter name: ").strip()
    if not name:
        print("Canceled.")
        return

    try:
        record = Record(name)

        address = input("Enter address or press Enter to skip: ").strip()
        if address:
            record.add_address(address)

        phone_input = input("Enter phone numbers (10 digits, comma-separated) or press Enter to skip: ").strip()
        if phone_input:
            phones = [p.strip() for p in phone_input.split(",")]
            for phone in phones:
                record.add_phone(phone)

        email = input("Enter email or press Enter to skip: ").strip()
        if email:
            record.add_email(email)

        birthday = input("Enter birthday (DD.MM.YYYY) or press Enter to skip: ").strip()
        if birthday:
            record.add_birthday(birthday)

        book.add_record(record)
        print("Contact added successfully")

    except ValueError as e:
        print(f"Error: {e}")


def show_upcoming_birthdays(book):
    print("Birthdays reminder")
    user_input = input("Enter number of days to check (or press Enter to cancel): ").strip()

    if not user_input:
        print("Canceled.")
        return

    try:
        days = int(user_input)
        upcoming = book.get_upcoming_birthdays(days)

        if upcoming:
            print(f"Birthdays in the next {days} days:")
            for entry in upcoming:
                print(f"{entry['name']} — {entry['congratulation_date']}")
        else:
            print(f"No birthdays in the next {days} days.")

    except ValueError:
        print("Please enter a valid number.")


def search_contact(book):
    print("Search contacts (or press Enter to cancel)")
    print("Available search criteria:\n 1. By name\n 2. By phone")
    choice = input("Choose search criteria (1/2): ").strip()

    if not choice:
        print("Canceled.")
        return

    if choice == "1":
        query = input("Enter full or partial name: ").strip().lower()
        if not query:
            print("Canceled.")
            return

        results = [
            record for record in book.data.values()
            if query in record.name.value.lower()
        ]

    elif choice == "2":
        phone_query = input("Enter phone number (10 digits, comma-separated): ").strip()
        if not phone_query:
            print("Canceled.")
            return

        query_numbers = [num.strip() for num in phone_query.split(",")]
        results = []

        for record in book.data.values():
            contact_numbers = [p.value for p in record.phones]
            if any(q in contact_numbers for q in query_numbers):
                results.append(record)

    else:
        print("Invalid choice.")
        return

    print(f"Found {len(results)} contact(s):")
    for record in results:
        print(record)


def edit_contact(book):
    print("Editing contact (or press Enter to cancel)")
    name = input("Enter name: ").strip()

    if not name:
        print("Canceled.")
        return

    record = book.find(name)
    if not record:
        print("Contact not found.")
        return

    print("Enter new values (or press Enter to keep current value)")

    new_address = input("Enter address or press Enter to skip: ").strip()
    if new_address:
        record.add_address(new_address)

    new_phones = input("Enter phone numbers (10 digits, comma-separated) or press Enter to skip: ").strip()
    if new_phones:
        record.phones = []
        for phone in new_phones.split(","):
            record.add_phone(phone.strip())

    new_email = input("Enter email or press Enter to skip: ").strip()
    if new_email:
        record.emails = []
        record.add_email(new_email)

    new_birthday = input("Enter birthday (DD.MM.YYYY) or press Enter to skip: ").strip()
    if new_birthday:
        record.add_birthday(new_birthday)

    print("Contact updated successfully!")


def delete_contact(book):
    print("Delete contacts (or press Enter to cancel)")
    name = input("Enter name: ").strip()

    if not name:
        print("Canceled.")
        return

    try:
        book.delete(name)
        print("Contact deleted")
    except ValueError:
        print("Contact not found.")


# -------------------- ПАРСЕР --------------------

def parse_input(user_input):
    parts = user_input.strip().split()
    return parts[0].lower(), parts[1:]


# -------------------- MAIN --------------------

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            add_contact(book, args)

        elif command == "show":
            print("All contacts:")
            print(book)

        elif command == "birthdays":
            show_upcoming_birthdays(book)

        elif command == "search":
            search_contact(book)

        elif command == "edit":
            edit_contact(book)

        elif command == "delete":
            delete_contact(book)

        else:
            print("Invalid command.")


# -------------------- ЗАПУСК --------------------

if __name__ == "__main__":
    main()
# -------------------- ЗАПУСК --------------------

# if __name__ == "__main__":
#     main()


# def main():
#     ui_helpers.print_welcome()
#     # read file
#     book = storage.load_data()
#     while True:
#         command, args = ui_helpers.parse_input()

#         if command is None:
#             continue

#         if command in ["close", "exit"]:
#             # save
#             storage.save_data(book)
#             ui_helpers.print_exit_message()
#             break
#         elif command == "hello":
#             ui_helpers.print_greeting_response()
#         elif command == "help":
#             ui_helpers.print_help()
#         elif command == "contacts":
#             ui_helpers.handle_contacts_module()
#         elif command == "notes":
#             ui_helpers.handle_notes_module()
#         else:
#             ui_helpers.print_unknown_command()


# def test_bot():
#     pass  # Placeholder for bot tests


# def test_file():
#     pass  # Placeholder for file save and load tests


# if __name__ == "__main__":
#     test_bot()
#     test_file()
#     main()
