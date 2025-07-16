import ui_helpers
import storage


def main():
    ui_helpers.print_welcome()
    # read file
    book = storage.load_data()
    while True:
        command, args = ui_helpers.parse_input()

        if command is None:
            continue

        if command in ["close", "exit"]:
            # save
            storage.save_data(book)
            ui_helpers.print_exit_message()
            break
        elif command == "hello":
            ui_helpers.print_greeting_response()
        elif command == "help":
            ui_helpers.print_help()
        elif command == "contacts":
            ui_helpers.handle_contacts_module()
        elif command == "notes":
            ui_helpers.handle_notes_module()
        else:
            ui_helpers.print_unknown_command()


def test_bot():
    pass  # Placeholder for bot tests


def test_file():
    pass  # Placeholder for file save and load tests


if __name__ == "__main__":
    test_bot()
    test_file()
    main()
