import sys
import inspect
from typing import Callable, Dict, Optional, List

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

import storage
import ui_helpers
import cli
from AddressBook import AddressBook, Record
from Note import note_handler

IGNORE_CASE = True


def wrap_handler(
    handler: Callable, *dependencies
) -> Callable[[List[str]], Optional[str]]:
    """
    Wraps a command handler to provide a consistent interface.

    If the original handler accepts 'args', it will be passed.
    Otherwise, only dependencies are passed.
    """
    sig = inspect.signature(handler)
    accepts_args = "args" in sig.parameters

    def wrapper(args):
        if accepts_args:
            return handler(*dependencies, args)
        return handler(*dependencies)

    return wrapper


def add_contact(book: AddressBook, args: List[str]) -> None:
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


def edit_contact(book: AddressBook, args: List[str]) -> None:
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


def show_upcoming_birthdays(session: PromptSession, book: AddressBook) -> None:
    user_input = session.prompt("Enter number of days to check: ").strip()
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


def search_contact(session: PromptSession, book: AddressBook):
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
        print("❌ Invalid choice.")
        return

    if results:
        print(f"🔍 Found {len(results)} contact(s):")
        for r in results:
            print(r)
    else:
        print("❌ No contacts found.")


def delete_contact(book: AddressBook, args: List[str]) -> None:
    if not args:
        print("Usage: delete <name>")
        return

    name = args[0]
    try:
        book.delete(name)
        print("🗑️ Contact deleted.")
    except ValueError:
        print("❌ Contact not found.")


def show_all_contacts(book: AddressBook) -> None:
    print("📇 All contacts:")
    print(book)


def notes_command_handler(book: AddressBook, args: List[str]) -> None:
    if not args:
        ui_helpers.handle_notes_module()
    else:
        note_handler(book, args)


def save_and_exit(book) -> None:
    """Save data and exit the application."""
    storage.save_data(book)
    ui_helpers.print_exit_message()
    sys.exit(0)


def process_command(
    command: str,
    args: List[str],
    command_handlers: Dict[str, Callable],
    available_commands: List[str],
) -> Optional[str]:
    handler = command_handlers.get(command)

    if not handler:
        return handle_invalid_command(
            command, args, command_handlers, available_commands
        )

    return handler(args)


def handle_invalid_command(
    command: str,
    args: List[str],
    command_handlers: Dict[str, Callable],
    available_commands: List[str],
) -> Optional[str]:
    suggestion = cli.suggest_command(command, available_commands)

    if suggestion:
        message = f"Command '{command}' not recognized.💡 Did you mean: {suggestion}?"
        if cli.confirm(message):
            return process_command(
                suggestion, args, command_handlers, available_commands
            )
        else:
            return None
    else:
        ui_helpers.print_unknown_command(command)
        return None


def main():
    session = PromptSession()
    # read file
    book = storage.load_data()

    command_handlers: Dict[str, Callable] = {
        "add": wrap_handler(add_contact, book),
        "change": wrap_handler(edit_contact, book),
        "show": wrap_handler(show_all_contacts, book),
        "delete": wrap_handler(delete_contact, book),
        "edit": wrap_handler(edit_contact, book),
        "birthdays": wrap_handler(show_upcoming_birthdays, session, book),
        "search": wrap_handler(search_contact, session, book),
        "notes": wrap_handler(notes_command_handler, book),
        "close": wrap_handler(save_and_exit, book),
        "exit": wrap_handler(save_and_exit, book),
        "hello": lambda _: ui_helpers.print_greeting_response(),
        "help": lambda _: ui_helpers.print_help(),
    }

    available_commands = list(command_handlers.keys())
    command_completer = WordCompleter(available_commands, ignore_case=IGNORE_CASE)

    ui_helpers.print_welcome()

    while True:
        try:
            command, args = ui_helpers.parse_input(session, command_completer)
            if command:
                process_command(command, args, command_handlers, available_commands)
        except KeyboardInterrupt:
            save_and_exit(book)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
