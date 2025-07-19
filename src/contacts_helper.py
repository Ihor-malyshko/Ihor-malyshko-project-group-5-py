import ui.ui_screens as ui_screens
from ui.ui_helpers import (
    parse_input,
    render_table,
    styled_prompt,
    styled_prompt_with_prefix,
)
from address_book import Record
from ui.style_settings import COLORS


# Define once in your UI module


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
    ui_screens.print_message_block(
        "🎂",
        f"{COLORS.cyan}Check for upcoming birthdays",
        [f"{COLORS.cyan}Enter the number of days ahead to look for birthdays."],
    )

    user_input = styled_prompt(
        "<prompt>Enter number of days to check:</prompt> "
    ).strip()

    if not user_input:
        ui_screens.print_success_message("Canceled.")
        return

    try:
        days = int(user_input)
        upcoming = book.get_upcoming_birthdays(days)

        if upcoming:
            ui_screens.print_success_message(f"🎉 Birthdays in next {days} day(s):")
            for entry in upcoming:
                print(
                    f"{COLORS.green_light}{entry['name']} {COLORS.reset}— {COLORS.cyan}{entry['congratulation_date']}{COLORS.reset}"
                )
        else:
            ui_screens.print_message_block(
                "📭",
                f"{COLORS.cyan}No upcoming birthdays",
                [f"{COLORS.yellow}No contacts have birthdays in the next {days} days."],
            )
            ui_screens.handle_contacts_module()

    except ValueError:
        ui_screens.print_error_message("Please enter a valid number.")


def search_contact(session, book):
    ui_screens.print_message_block(
        "🔎",
        f"{COLORS.cyan}Search contacts (press Enter to cancel)",
        [
            f"{COLORS.cyan}1. By {COLORS.green}name",
            f"{COLORS.cyan}2. By {COLORS.green}phone",
        ],
    )

    choice = styled_prompt("<prompt>Choose option (1/2):</prompt> ")

    results = []

    if choice == "1":
        query = (
            styled_prompt_with_prefix(session, "Enter full or partial name: ")
            .strip()
            .lower()
        )

        results = [
            record
            for record in book.data.values()
            if query in record.name.value.lower()
        ]

    elif choice == "2":
        query_numbers = (
            styled_prompt_with_prefix(
                session, "Enter phone number(s) comma-separated: "
            )
            .strip()
            .split(",")
        )
        for record in book.data.values():
            contact_numbers = [p.value for p in record.phones]
            if any(q.strip() in contact_numbers for q in query_numbers):
                results.append(record)

    elif choice == "":
        ui_screens.print_success_message("Search cancelled.")
        return
    else:
        ui_screens.print_error_message("Invalid choice.")
        return

    if results:
        data = []
        for record in results:
            data.append(
                [
                    record.name.value,
                    record.address.value if record.address else "—",
                    ", ".join(p.value for p in record.phones) if record.phones else "—",
                    record.emails[0].value if record.emails else "—",
                    (
                        record.birthday.value.strftime("%d.%m.%Y")
                        if record.birthday
                        else "—"
                    ),
                    record.note.value if record.note else "—",
                ]
            )

        headers = ["Name", "Address", "Phone", "Email", "Birthday", "Note"]
        ui_screens.print_success_message(f"Found {len(results)} contact(s):")
        render_table(data, headers)

    else:
        ui_screens.print_error_message("Contact not found in address book.")


def delete_contact(book, args):
    if not args:
        ui_screens.print_command_usage("contacts", "delete")
        return

    name = args[0]
    try:
        book.delete(name)
        ui_screens.print_success_message("Contact deleted.")
    except ValueError:
        ui_screens.print_error_message("Contact not found in address book.")


def show_all_contacts(book):
    data = []
    for record in book.data.values():
        data.append(
            [
                record.name.value,
                record.address.value if record.address else "—",
                ", ".join(p.value for p in record.phones) if record.phones else "—",
                record.emails[0].value if record.emails else "—",
                record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "—",
                record.note.value if record.note else "—",
            ]
        )

    headers = ["Name", "Address", "Phone", "Email", "Birthday", "Note"]
    render_table(data, headers)


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
            ui_screens.print_unknown_command(command)
