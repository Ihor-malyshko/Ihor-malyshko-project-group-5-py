from ui.style_settings import COLORS
from ui.ui_helpers import border, line, center_line, separator


def print_welcome():
    print(border())
    print(
        center_line(
            f"{COLORS.cyan}{COLORS.bright}✦ 🤖 PERSONAL ASSISTANT SYSTEM {COLORS.green}ONLINE{COLORS.cyan} ✦"
        )
    )
    print(separator())

    static_info = [
        f"{COLORS.cyan_light}Modules: {COLORS.green}✔ Contacts  {COLORS.yellow}✔ Notes",
        f"{COLORS.cyan_light}Status: {COLORS.green}All systems operational",
    ]
    for item in static_info:
        print(line(item))

    print(separator())

    help_lines = [
        f"{COLORS.cyan}🔹 Enter {COLORS.green_light}contacts{COLORS.cyan}  - Manage address book",
        f"{COLORS.cyan}🔹 Enter {COLORS.green_light}notes{COLORS.cyan}     - Work with notes",
        f"{COLORS.cyan}🔹 Enter {COLORS.green_light}help{COLORS.cyan}      - View available commands",
        f"{COLORS.cyan}🔹 Enter {COLORS.green_light}exit{COLORS.cyan}      - Save and exit",
    ]
    for item in help_lines:
        print(line(item))

    print(border(top=False))


def print_exit_message():
    print()
    print(border())
    print(
        line(f"{COLORS.cyan}{COLORS.bright}🔒 SESSION SAVED — SHUTTING DOWN ASSISTANT...")
    )
    print(separator())

    messages = [
        f"{COLORS.blue}👋 Goodbye, human.",
        f"{COLORS.blue}💡 Remember: information is power.",
    ]
    for msg in messages:
        print(line(msg))

    print(border(top=False))
    print()


def print_unknown_command(command=None):
    print(border())
    print(line(f"{COLORS.cyan}🧭  Command not recognized."))
    if command:
        print(
            line(f"➤  '{COLORS.yellow}{command}{COLORS.cyan}' is not a valid instruction.")
        )
    print(line(f"➤  Type {COLORS.green}help{COLORS.cyan} to view available commands."))
    print(border(top=False))


def print_greeting_response():
    print(border())
    lines = [
        f"{COLORS.cyan}🤖  Hello, human. I'm standing by.",
        f"{COLORS.cyan}➤  Here's what I can help you with:",
    ]
    for l in lines:
        print(line(l))
    print(separator())
    print("Here must be help menu")  # Replace with call to real help menu


def handle_contacts_module():
    print(border())
    print(line(f"{COLORS.cyan}📁  MODULE: CONTACTS"))
    print(separator())
    print(line(f"{COLORS.cyan}🧭  You have entered the CONTACTS module."))
    print(line(f"{COLORS.cyan}➤  Available commands:"))

    commands = [
        f"• {COLORS.green_light}add [name] [phone]{COLORS.cyan}      — Add a new contact",
        f"• {COLORS.green_light}edit [name]{COLORS.cyan}             — Edit contact info",
        f"• {COLORS.green_light}delete [name]{COLORS.cyan}           — Delete a contact",
        f"• {COLORS.green_light}find [query]{COLORS.cyan}            — Search contacts",
        f"• {COLORS.green_light}birthdays [days]{COLORS.cyan}        — Upcoming birthdays",
        f"• {COLORS.green_light}back{COLORS.cyan}                    — Return to main menu",
    ]
    for cmd in commands:
        print(line(cmd))

    print(border(top=False))


def handle_notes_module():
    print(border())
    print(line(f"{COLORS.cyan}📒  MODULE: NOTES"))
    print(separator())
    print(line(f"{COLORS.cyan}🧭  You have entered the NOTES module."))
    print(line(f"{COLORS.cyan}➤  Available commands:"))

    commands = [
        f"• {COLORS.green_light}add [note text]{COLORS.cyan}           — Add new note",
        f"• {COLORS.green_light}edit [note id]{COLORS.cyan}            — Edit a note",
        f"• {COLORS.green_light}delete [note id]{COLORS.cyan}          — Delete a note",
        f"• {COLORS.green_light}search [query]{COLORS.cyan}            — Search notes",
        f"• {COLORS.green_light}list-tags{COLORS.cyan}                — List available tags",
        f"• {COLORS.green_light}back{COLORS.cyan}                     — Return to main menu",
    ]
    for cmd in commands:
        print(line(cmd))

    print(border(top=False))

def print_help():
    print("Here must be help menu")

