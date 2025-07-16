import re
from colorama import init, Fore, Style
from wcwidth import wcswidth
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as PromptStyle

init()


ANSI_ESCAPE_RE = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
BOX_WIDTH = 58  # Width of the inner content inside the frame (without borders)
FULL_WIDTH = BOX_WIDTH + 2  # Total width including border characters

# Style for prompt_toolkit
cli_style = PromptStyle.from_dict(
    {
        "prompt": "#ff00ff bold",
        "bracket": "#00ffff",
        "arrow": "#00ff00 bold",
        "": "#00cc44 bold",
    }
)

# Remove ANSI escape sequences.
def strip_ansi(text: str) -> str:
    return ANSI_ESCAPE_RE.sub("", text)


def visible_width(text: str) -> int:
    return wcswidth(strip_ansi(text))


def separator():
    return f"{Fore.MAGENTA}╠{'═' * (FULL_WIDTH + 2)}╣"


def border(top=True):
    line = f"{'═' * (FULL_WIDTH + 2)}"
    return (
        f"{Fore.MAGENTA}{Style.BRIGHT}╔{line}╗"
        if top
        else f"{Fore.MAGENTA}╚{line}╝{Style.RESET_ALL}"
    )


def center_line(content: str) -> str:
    vis_len = visible_width(content)
    total_pad = FULL_WIDTH - vis_len + 2
    left = total_pad // 2
    right = total_pad - left
    return f"{Fore.CYAN}║{' ' * left}{content}{' ' * right}║"


def line(content: str) -> str:
    padding = FULL_WIDTH - visible_width(content)
    return f"{Fore.CYAN}║ {content}{' ' * max(padding, 0)} ║"


def print_welcome():
    print(border())
    print(
        center_line(
            f"{Fore.CYAN}{Style.BRIGHT}✦ 🤖 PERSONAL ASSISTANT SYSTEM {Fore.GREEN}ONLINE{Fore.CYAN} ✦"
        )
    )
    print(separator())

    static_info = [
        f"{Fore.LIGHTCYAN_EX}Modules: {Fore.GREEN}✔ Contacts  {Fore.YELLOW}✔ Notes",
        f"{Fore.LIGHTCYAN_EX}Status: {Fore.GREEN}All systems operational",
    ]
    for line_content in static_info:
        print(line(line_content))

    print(separator())

    help_lines = [
        f"{Fore.CYAN}🔹 Enter {Fore.LIGHTGREEN_EX}contacts{Fore.CYAN}  - Manage address book",
        f"{Fore.CYAN}🔹 Enter {Fore.LIGHTGREEN_EX}notes{Fore.CYAN}     - Work with notes",
        f"{Fore.CYAN}🔹 Enter {Fore.LIGHTGREEN_EX}help{Fore.CYAN}      - View available commands",
        f"{Fore.CYAN}🔹 Enter {Fore.LIGHTGREEN_EX}exit{Fore.CYAN}      - Save and exit",
    ]
    for line_content in help_lines:
        print(line(line_content))

    print(border(top=False))


def print_exit_message():
    print()
    print(border())
    print(
        line(f"{Fore.CYAN}{Style.BRIGHT}🔒 SESSION SAVED — SHUTTING DOWN ASSISTANT...")
    )
    print(separator())

    messages = [
        f"{Fore.BLUE}👋 Goodbye, human.",
        f"{Fore.BLUE}💡 Remember: information is power.",
    ]
    for msg in messages:
        print(line(msg))

    print(border(top=False))
    print()


def print_unknown_command(command=None):
    print(border())
    print(line(f"{Fore.CYAN}🧭  Command not recognized."))

    if command:
        print(
            line(f"➤  '{Fore.YELLOW}{command}{Fore.CYAN}' is not a valid instruction.")
        )

    print(line(f"➤  Type {Fore.GREEN}help{Fore.CYAN} to view available commands."))
    print(border(top=False))


def print_help():
    print("Here must be help menu")


def print_greeting_response():
    lines = [
        f"{Fore.CYAN}🤖  Hello, human. I'm standing by.",
        f"{Fore.CYAN}➤  Here's what I can help you with:",
    ]
    print(border())
    for line_content in lines:
        print(line(line_content))
    print(separator())
    print_help()


def handle_contacts_module():
    print(border())
    print(line(f"{Fore.CYAN}📁  MODULE: CONTACTS"))
    print(separator())
    print(line(f"{Fore.CYAN}🧭  You have entered the CONTACTS module."))
    print(line(f"{Fore.CYAN}➤  Available commands:"))

    commands = [
        f"• {Fore.LIGHTGREEN_EX}add [name] [phone]{Fore.CYAN}      — Add a new contact",
        f"• {Fore.LIGHTGREEN_EX}edit [name]{Fore.CYAN}             — Edit contact info",
        f"• {Fore.LIGHTGREEN_EX}delete [name]{Fore.CYAN}           — Delete a contact",
        f"• {Fore.LIGHTGREEN_EX}find [query]{Fore.CYAN}            — Search contacts",
        f"• {Fore.LIGHTGREEN_EX}birthdays [days]{Fore.CYAN}        — Upcoming birthdays",
        f"• {Fore.LIGHTGREEN_EX}back{Fore.CYAN}                    — Return to main menu",
    ]

    for cmd in commands:
        print(line(cmd))

    print(border(top=False))


def handle_notes_module():
    print(border())
    print(line(f"{Fore.CYAN}📒  MODULE: NOTES"))
    print(separator())
    print(line(f"{Fore.CYAN}🧭  You have entered the NOTES module."))
    print(line(f"{Fore.CYAN}➤  Available commands:"))

    commands = [
        f"• {Fore.LIGHTGREEN_EX}add [note text]{Fore.CYAN}           — Add new note",
        f"• {Fore.LIGHTGREEN_EX}edit [note id]{Fore.CYAN}            — Edit a note",
        f"• {Fore.LIGHTGREEN_EX}delete [note id]{Fore.CYAN}          — Delete a note",
        f"• {Fore.LIGHTGREEN_EX}search [query]{Fore.CYAN}            — Search notes",
        f"• {Fore.LIGHTGREEN_EX}list-tags{Fore.CYAN}                — List available tags",
        f"• {Fore.LIGHTGREEN_EX}back{Fore.CYAN}                     — Return to main menu",
    ]

    for cmd in commands:
        print(line(cmd))

    print(border(top=False))


def parse_input():
    user_input = prompt(
        [
            ("class:bracket", "╭─["),
            ("class:prompt", "assistant-terminal"),
            ("class:bracket", "]\n"),
            ("class:arrow", "╰─>>> "),
        ],
        style=cli_style,
    )

    if not user_input.strip():
        lines = [
            f"{Fore.CYAN}🧭  No input received.",
            f"{Fore.CYAN}➤  Please enter a valid command.",
        ]
        print(border())
        for msg in lines:
            print(line(msg))
        print(border(top=False))
        return None, []

    cmd, *args = user_input.strip().split()
    return cmd.lower(), args
