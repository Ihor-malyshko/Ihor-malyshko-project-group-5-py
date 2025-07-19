import sys
import inspect
from typing import Callable, Dict, Optional, List

from prompt_toolkit import PromptSession

import ui.ui_screens as ui_screens
from ui.ui_helpers import parse_input
import storage.storage as storage
import contacts_helper as contacts
import notes_helper as notes
from cli.enums import Context

from cli.command_processor import CommandProcessor
from cli.context_manager import ContextManager


class Bot:
    def __init__(self):
        self.session = PromptSession()
        self.address_book = storage.load_data()
        self.context_manager = ContextManager()
        self.command_processor = CommandProcessor(self.context_manager)
        self._initialize_commands()

        self.context_manager.register_commands(
            Context.MAIN, list(self.command_handlers.keys())
        )
        self.context_manager.register_commands(
            Context.CONTACTS, list(self.contacts_command_handlers.keys())
        )
        self.context_manager.register_commands(
            Context.NOTES, list(self.notes_command_handlers.keys())
        )

        self.command_processor.register_handlers(Context.MAIN, self.command_handlers)
        self.command_processor.register_handlers(
            Context.CONTACTS, self.contacts_command_handlers
        )
        self.command_processor.register_handlers(
            Context.NOTES, self.notes_command_handlers
        )

    def _initialize_commands(self) -> None:
        """Initialize command handlers dictionary."""
        self.command_handlers: Dict[str, Callable] = {
            "contacts": lambda _: self.context_manager.switch_context(
                Context.CONTACTS, self.handle_contacts_command
            ),
            "notes": lambda _: self.context_manager.switch_context(
                Context.NOTES, self.handle_notes_command
            ),
            "exit": lambda _: self.save_and_exit(),
            "hello": lambda _: ui_screens.print_greeting_response(),
            "help": lambda _: ui_screens.print_help(),
        }

        self.contacts_command_handlers: Dict[str, Callable] = {
            "add": self.wrap_handler(contacts.add_contact, self.address_book),
            "edit": self.wrap_handler(contacts.edit_contact, self.address_book),
            "delete": self.wrap_handler(contacts.delete_contact, self.address_book),
            "birthdays": self.wrap_handler(
                contacts.show_upcoming_birthdays, self.address_book
            ),
            "search": self.wrap_handler(
                contacts.search_contact, self.session, self.address_book
            ),
            "show": self.wrap_handler(contacts.show_all_contacts, self.address_book),
            "back": lambda _: self._back_to_main(),
            "exit": lambda _: self.save_and_exit(),
            "help": lambda _: ui_screens.handle_contacts_module(),
        }

        self.notes_command_handlers: Dict[str, Callable] = {
            # "add": self.wrap_handler(notes.add_note, self.address_book),
            # "edit": self.wrap_handler(notes.edit_note, self.address_book),
            # "delete": self.wrap_handler(notes.delete_note, self.address_book),
            # "search": self.wrap_handler(notes.search_notes, self.address_book),
            # "show": self.wrap_handler(notes.show_notes, self.address_book),
            "exit": lambda _: self.save_and_exit(),
            "back": lambda _: self.context_manager.switch_context(Context.MAIN),
            "help": lambda _: ui_screens.handle_notes_module(),
        }

        self.commands_by_context = {
            Context.MAIN: list(self.command_handlers.keys()),
            Context.CONTACTS: list(self.contacts_command_handlers.keys()),
            Context.NOTES: list(self.notes_command_handlers.keys()),
        }

    def wrap_handler(
        self, handler: Callable, *dependencies
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

    def save_and_exit(self) -> None:
        """Save data and exit the application."""
        storage.save_data(self.address_book)
        ui_screens.print_exit_message()
        sys.exit(0)

    def _back_to_main(self):
        self.context_manager.switch_context(Context.MAIN)
        ui_screens.print_main_menu_options()

    def handle_notes_command(self) -> None:
        ui_screens.handle_notes_module()

    def handle_contacts_command(self) -> None:
        ui_screens.handle_contacts_module()

    def run(self) -> None:
        ui_screens.print_welcome()

        while True:
            try:
                command, args = parse_input(
                    self.session, self.context_manager.command_completer
                )
                if command:
                    self.command_processor.process_command(
                        command, args, self.context_manager.current_context
                    )
            except KeyboardInterrupt:
                self.save_and_exit()
            except Exception as e:
                print(f"An error occurred: {str(e)}")
