import ui.ui_screens as ui_screens
from ui.ui_helpers import parse_input
import storage.storage as storage
import contacts_helper as contacts
import notes_helper as notes


def main():
    ui_screens.print_welcome()
    # read file
    book = storage.load_data()

    while True:
        command, args = parse_input()

        if command in ["close", "exit"]:
            storage.save_data(book)
            ui_screens.print_exit_message()
            break

        elif command == "hello":
            ui_screens.print_greeting_response()
        elif command == "n":
            if not args:
                # If no arguments, show help for notes module
                ui_screens.handle_notes_module()
            else:
                # Handle specific commands in notes module
                notes.note_handler(book, args)
        elif command == "help":
            ui_screens.print_help()
        elif command == "contacts":
            ui_screens.handle_contacts_module()
            contacts.contacts_handler(book, args)
        else:
            ui_screens.print_unknown_command(command)


if __name__ == "__main__":
    main()