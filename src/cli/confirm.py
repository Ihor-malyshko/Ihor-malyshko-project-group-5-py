from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style


def confirm(question: str) -> bool:
    """
    Prompt the user with a yes/no question, returning True for 'y' and False for 'n'.
    The prompt uses custom styling and key bindings.

    :param question: The question string to display to the user.
    :return: True if the user presses 'y' or 'Y', False if 'n' or 'N'.
    """
    style = Style.from_dict({"question": "ansiblue bold"})

    bindings = KeyBindings()

    result = None

    @bindings.add("y")
    @bindings.add("Y")
    @bindings.add("н")  # Cyrillic equivalent of 'y' key in QWERTY
    @bindings.add("Н")
    def _(event):
        nonlocal result
        result = True
        event.app.exit()

    @bindings.add("n")
    @bindings.add("N")
    @bindings.add("т")  # Cyrillic equivalent of 'n' key in QWERTY
    @bindings.add("Т")
    def _(event):

        nonlocal result
        result = False
        event.app.exit()

    print_formatted_text(HTML(f"<question>{question} [y/n]: </question>"), style=style)

    # Run prompt to wait for y/n keypress, but we ignore the return value,
    # because result is set via key bindings
    prompt("", key_bindings=bindings, style=style)

    return result
