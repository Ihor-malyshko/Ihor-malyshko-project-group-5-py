from colorama import init, Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as PromptStyle


init()

cli_style = PromptStyle.from_dict(
    {
        "prompt": "#ff00ff bold",
        "bracket": "#00ffff",
        "arrow": "#00ff00 bold",
        "": "#00cc44 bold",
    }
)


def print_welcome():
    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
    )
    print(
        f"{Fore.CYAN}{Style.BRIGHT}║  ✦  🤖 PERSONAL ASSISTANT SYSTEM {Fore.GREEN}ONLINE{Fore.CYAN}  ✦              ║"
    )
    print(f"{Fore.MAGENTA}╠══════════════════════════════════════════════════════╣")

    print(
        f"{Fore.BLUE}║  {Fore.LIGHTCYAN_EX}Modules: "
        f"{Fore.GREEN}✔ Contacts  "
        f"{Fore.YELLOW}✔ Notes                         {Fore.BLUE}║"
    )

    print(
        f"{Fore.BLUE}║  {Fore.LIGHTCYAN_EX}Status: {Fore.GREEN}All systems operational                {Fore.BLUE}║"
    )

    print(f"{Fore.MAGENTA}╠══════════════════════════════════════════════════════╣")

    print(
        f"{Fore.CYAN}║  🔹 Enter {Fore.LIGHTGREEN_EX}contact{Fore.CYAN}  - Manage address book             ║"
    )
    print(
        f"{Fore.CYAN}║  🔹 Enter {Fore.LIGHTGREEN_EX}note{Fore.CYAN}     - Work with notes                  ║"
    )
    print(
        f"{Fore.CYAN}║  🔹 Enter {Fore.LIGHTGREEN_EX}help{Fore.CYAN}     - View available commands          ║"
    )
    print(
        f"{Fore.CYAN}║  🔹 Enter {Fore.LIGHTGREEN_EX}exit{Fore.CYAN}     - Save and exit                    ║"
    )

    print(
        f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}"
    )


def print_exit_message():
    print()
    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
    )
    print(
        f"{Fore.CYAN}{Style.BRIGHT}║  🔒 SESSION SAVED — SHUTTING DOWN ASSISTANT...       ║"
    )
    print(f"{Fore.MAGENTA}╠══════════════════════════════════════════════════════╣")
    print(f"{Fore.BLUE}║  👋 Goodbye, human.                                   ")
    print(f"{Fore.BLUE}║  💡 Remember: information is power.                   ")
    print(
        f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}"
    )
    print()


def print_unknown_command(command=None):
    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
    )
    print(f"{Fore.CYAN}║  🧭  Command not recognized.                          ")
    if command:
        print(
            f"{Fore.CYAN}║  ➤ '{Fore.YELLOW}{command}{Fore.CYAN}' is not a valid instruction."
        )
    print(
        f"{Fore.CYAN}║  ➤  Type {Fore.GREEN}help{Fore.CYAN} to view available commands."
    )

    print(
        f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}"
    )


def print_help():
    print("Here must be help menu")


def print_greeting_response():
    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
    )
    print(f"{Fore.CYAN}║  🤖  Hello, human. I'm standing by.                  ")
    print(f"{Fore.CYAN}║  ➤  Here's what I can help you with:                 ")
    print(
        f"{Fore.MAGENTA}╠══════════════════════════════════════════════════════╣{Style.RESET_ALL}"
    )
    print_help()


from colorama import Fore, Style


def handle_contact_module():
    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
    )
    print(f"{Fore.CYAN}║  📁  MODULE: CONTACTS                                ║")
    print(f"{Fore.MAGENTA}╠══════════════════════════════════════════════════════╣")
    print(f"{Fore.CYAN}║  🧭  You have entered the CONTACT module.            ║")
    print(f"{Fore.CYAN}║  ➤  Available commands:                              ║")
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}add [name] [phone]{Fore.CYAN}      — Add a new contact     ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}edit [name]{Fore.CYAN}             — Edit contact info     ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}delete [name]{Fore.CYAN}           — Delete a contact      ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}find [query]{Fore.CYAN}            — Search contacts       ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}birthdays [days]{Fore.CYAN}        — Upcoming birthdays    ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}back{Fore.CYAN}                    — Return to main menu   ║"
    )
    print(
        f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}"
    )

    # Здесь можно запустить внутренний цикл для приёма команд внутри модуля
    while True:
        cmd, args = parse_input()
        if not cmd:
            continue

        if cmd == "back":
            break
        elif cmd == "add":
            print("🛠  Add contact logic not implemented yet.")
        elif cmd == "edit":
            print("🛠  Edit contact logic not implemented yet.")
        elif cmd == "delete":
            print("🛠  Delete contact logic not implemented yet.")
        elif cmd == "find":
            print("🛠  Find contact logic not implemented yet.")
        elif cmd == "birthdays":
            print("🛠  Birthdays logic not implemented yet.")
        else:
            print_unknown_command(cmd)


def handle_contacts_module():
    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
    )
    print(f"{Fore.CYAN}║  📁  MODULE: CONTACTS                                ║")
    print(f"{Fore.MAGENTA}╠══════════════════════════════════════════════════════╣")
    print(f"{Fore.CYAN}║  🧭  You have entered the CONTACTS module.            ║")
    print(f"{Fore.CYAN}║  ➤  Available commands:                              ║")
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}add [name] [phone]{Fore.CYAN}      — Add a new contact     ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}edit [name]{Fore.CYAN}             — Edit contact info     ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}delete [name]{Fore.CYAN}           — Delete a contact      ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}find [query]{Fore.CYAN}            — Search contacts       ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}birthdays [days]{Fore.CYAN}        — Upcoming birthdays    ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}back{Fore.CYAN}                    — Return to main menu   ║"
    )
    print(
        f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}"
    )


def handle_notes_module():
    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
    )
    print(f"{Fore.CYAN}║  📒  MODULE: NOTES                                   ║")
    print(f"{Fore.MAGENTA}╠══════════════════════════════════════════════════════╣")
    print(f"{Fore.CYAN}║  🧭  You have entered the NOTES module.              ║")
    print(f"{Fore.CYAN}║  ➤  Available commands:                              ║")
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}add [note text]{Fore.CYAN}           — Add new note         ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}edit [note id]{Fore.CYAN}            — Edit a note           ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}delete [note id]{Fore.CYAN}          — Delete a note         ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}search [query]{Fore.CYAN}            — Search notes          ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}list-tags{Fore.CYAN}                — List available tags   ║"
    )
    print(
        f"{Fore.CYAN}║     • {Fore.LIGHTGREEN_EX}back{Fore.CYAN}                     — Return to main menu    ║"
    )
    print(
        f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}"
    )


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
        print(
            f"{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════════════════════╗"
        )
        print(f"{Fore.CYAN}║  🧭  No input received.                               ")
        print(f"{Fore.CYAN}║  ➤  Please enter a valid command.                    ")
        print(
            f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}"
        )
        return None, []

    cmd, *args = user_input.strip().split()
    return cmd.lower(), args
