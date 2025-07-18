import ui.ui_screens as ui_screens
from ui.ui_helpers import parse_input
from ui.ui_screens import print_unknown_command
from address_book import Record


def add_contact(book, args):
    if not args:
        ui_screens.print_command_usage("contacts", "add")
        return

    try:
        name = args[0]
        record = Record(name)

        if len(args) > 1:
            record.add_address(args[1])
        if len(args) > 2:
            phones = args[2].split(",")
            for phone in phones:
                record.add_phone(phone.strip())
        if len(args) > 3:
            record.add_email(args[3])
        if len(args) > 4:
            record.add_birthday(args[4])

        book.add_record(record)
        ui_screens.print_success_message("Contact added successfully")

    except ValueError as e:
        ui_screens.print_error_message(f"Error: {e}")


def edit_contact(book, args):
    if not args:
        ui_screens.print_edit_contact_usage("contacts", "edit")
        return

    name = args[0]
    record = book.find(name)

    if not record:
        ui_screens.print_error_message("Contact not found in address book")
        return

    try:
        if len(args) > 1:
            record.add_address(args[1])
        if len(args) > 2:
            record.phones = []
            for phone in args[2].split(","):
                record.add_phone(phone.strip())
        if len(args) > 3:
            record.emails = []
            record.add_email(args[3])
        if len(args) > 4:
            record.add_birthday(args[4])

        ui_screens.print_success_message("Contact updated successfully!")

    except ValueError as e:
        ui_screens.print_error_message(f"Error while editing contact: {e}")


def show_upcoming_birthdays(book):
    user_input = input("Enter number of days to check: ").strip()
    if not user_input:
        print("Canceled.")
        return

    try:
        days = int(user_input)
        upcoming = book.get_upcoming_birthdays(days)
        if upcoming:
            print(f"🎉 Birthdays in next {days} days:")
            for entry in upcoming:
                print(f"{entry['name']} — {entry['congratulation_date']}")
        else:
            ui_screens.print_no_upcoming_birthdays()

    except ValueError:
        ui_screens.print_error_message("Please enter a valid number.")


def search_contact(session, book):
    print("Search contacts (or press Enter to cancel)")
    print("Available search criteria:\n 1. By name\n 2. By phone")
    choice = session.prompt("Choose search criteria (1/2): ").strip()

    if choice == "1":
        query = session.prompt("Enter full or partial name: ").strip().lower()
        results = [
            record
            for record in book.data.values()
            if query in record.name.value.lower()
        ]

    elif choice == "2":
        query_numbers = (
            session.prompt("Enter phone number(s) comma-separated: ").strip().split(",")
        )
        results = []
        for record in book.data.values():
            contact_numbers = [p.value for p in record.phones]
            if any(q.strip() in contact_numbers for q in query_numbers):
                results.append(record)
    else:
        ui_screens.print_error_message("Invalid choice.")
        return

    if results:
        print(f"🔍 Found {len(results)} contact(s):")
        for r in results:
            print(r)
    else:
        ui_screens.print_error_message("Contact not found in address book")


def delete_contact(book, args):
    if not args:
        print("Usage: delete <name>")
        return

    name = args[0]
    try:
        book.delete(name)
        print("🗑️ Contact deleted.")
    except ValueError:
        ui_screens.print_error_message("Contact not found in address book.")


def show_all_contacts(book):
    print("📇 All contacts:")
    print(book)


def contacts_handler(book, args):
    while True:
        command, args = parse_input()

        if command in ["back", "exit"]:
            break

        elif command == "add":
            add_contact(book, args)

        elif command == "edit":
            edit_contact(book, args)

        elif command == "delete":
            delete_contact(book, args)

        elif command == "birthdays":
            show_upcoming_birthdays(book)

        elif command == "search":
            search_contact(book)

        elif command == "show":
            print("📇 All contacts:")
            print(book)

        else:
            print_unknown_command(command)
