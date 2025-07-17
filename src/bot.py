import storage
import ui_helpers
from address_book import Record
from note import note_handler


def add_contact(book, args):
    if not args:
        print("Usage: add <name> [address] [phones] [email] [birthday]")
        print("Example: add John Kyiv 1234567890 john@email.com 01.01.1990")
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
        print("✅ Contact added successfully")

    except ValueError as e:
        print(f"❌ Error: {e}")


def edit_contact(book, args):
    if not args:
        print("Usage: edit <name> [new_address] [phones] [email] [birthday]")
        print("Example: edit John NewAddress 0987654321 new@email.com 02.02.1992")
        return

    name = args[0]
    record = book.find(name)

    if not record:
        print("❌ Contact not found.")
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

        print("✅ Contact updated successfully!")

    except ValueError as e:
        print(f"❌ Error while editing contact: {e}")


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
            print("📭 No upcoming birthdays.")

    except ValueError:
        print("❌ Please enter a valid number.")


def search_contact(book):
    print("Search contacts (or press Enter to cancel)")
    print("Available search criteria:\n 1. By name\n 2. By phone")
    choice = input("Choose search criteria (1/2): ").strip()

    if choice == "1":
        query = input("Enter full or partial name: ").strip().lower()
        results = [
            record for record in book.data.values()
            if query in record.name.value.lower()
        ]

    elif choice == "2":
        query_numbers = input("Enter phone number(s) comma-separated: ").strip().split(",")
        results = []
        for record in book.data.values():
            contact_numbers = [p.value for p in record.phones]
            if any(q.strip() in contact_numbers for q in query_numbers):
                results.append(record)
    else:
        print("❌ Invalid choice.")
        return

    if results:
        print(f"🔍 Found {len(results)} contact(s):")
        for r in results:
            print(r)
    else:
        print("❌ No contacts found.")


def delete_contact(book, args):
    if not args:
        print("Usage: delete <name>")
        return

    name = args[0]
    try:
        book.delete(name)
        print("🗑️ Contact deleted.")
    except ValueError:
        print("❌ Contact not found.")


def main():
    
    ui_helpers.print_welcome()
    # read file
    book = storage.load_data()

    while True:
        command, args = ui_helpers.parse_input()

        if command in ["close", "exit"]:
            storage.save_data(book)
            ui_helpers.print_exit_message()
            break

        elif command == "hello":
            ui_helpers.print_greeting_response()
        # elif command == "notes":
        elif command == "n":
            if not args:
              # If no arguments, show help for notes module
                ui_helpers.handle_notes_module()
            else:
              # Handle specific commands in notes module
              note_handler(book, args)

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

        elif command == "help":
            ui_helpers.print_help()

        else:
            ui_helpers.print_unknown_command(command)


if __name__ == "__main__":
    main()