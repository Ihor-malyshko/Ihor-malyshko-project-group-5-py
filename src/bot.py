import ui.ui_screens as ui_screens
from ui.ui_helpers import parse_input
import storage.storage as storage


def main():
    ui_screens.print_welcome()
    # read file
    book = storage.load_data()
    while True:
        command, args = parse_input()

        if command is None:
            continue

        if command in ["close", "exit"]:
            # save
            storage.save_data(book)
            ui_screens.print_exit_message()
            break
        elif command == "hello":
            ui_screens.print_greeting_response()
        elif command == "help":
            ui_screens.print_help()
        elif command == "contacts":
            ui_screens.handle_contacts_module()
        elif command == "notes":
            ui_screens.handle_notes_module()
        else:
            ui_screens.print_unknown_command()


def test_bot():
    pass  # Placeholder for bot tests


def test_file():
    pass  # Placeholder for file save and load tests


if __name__ == "__main__":
    test_bot()
    test_file()
    main()
