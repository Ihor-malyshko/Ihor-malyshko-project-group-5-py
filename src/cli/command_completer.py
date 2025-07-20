from typing import Iterable, List
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.completion import CompleteEvent
from cli.keyboard_layout import KEYBOARD_LAYOUT


class CommandCompleter(Completer):
    """
    A custom completer for CLI commands.

    It only provides completions when the cursor is positioned in the first word
    (i.e., the command name), and ignores further arguments.

    Completions are case-insensitive.
    """

    def __init__(self, commands: List[str]) -> None:
        """
        Initialize the completer with a list of available commands.

        :param commands: A list of command strings to complete from.
        """
        self.commands = commands

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        """
        Yield command completions for the current input.

        :param document: The Document instance representing the current input.
        :param complete_event: The completion trigger event (unused).
        :yield: Completion suggestions for matching commands.
        """
        text = document.text_before_cursor
        words = text.strip().split()

        # Only suggest completions for the first word
        cursor_pos = document.cursor_position
        first_space = text.find(" ")
        if first_space != -1 and cursor_pos > first_space:
            return  # Cursor is past the first word → don't show completions

        fragment = words[0].lower() if words else ""
        fragment_lower = fragment.lower()
        translit_fragment = self._translate_layout(fragment_lower)
        current_word = document.get_word_before_cursor()

        for command in self.commands:
            cmd_lower = command.lower()
            if cmd_lower.startswith(fragment_lower) or cmd_lower.startswith(
                translit_fragment
            ):
                # Show completion starting from the beginning of the current word being typed
                yield Completion(
                    command,
                    start_position=-len(current_word),
                )

    def _translate_layout(self, input_str: str) -> str:
        """Translates a string typed in Cyrillic as if on a QWERTY keyboard to Latin."""
        return input_str.translate(KEYBOARD_LAYOUT)
