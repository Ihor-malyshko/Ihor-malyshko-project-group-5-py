from ui.style_settings import COLORS
from ui.ui_helpers import border, line, center_line, separator


def print_main_menu_options():
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

    print_main_menu_options()


def print_exit_message():
    print()
    print(border())
    print(
        line(
            f"{COLORS.cyan}{COLORS.bright}🔒 SESSION SAVED — SHUTTING DOWN ASSISTANT..."
        )
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
            line(
                f"➤  '{COLORS.yellow}{command}{COLORS.cyan}' is not a valid instruction."
            )
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
    print(line(f"{COLORS.cyan}➤  Available commands (Required: <>, Optional: []):"))
    print(line(f"{COLORS.cyan}"))
 

    commands = [
        f"• {COLORS.green_light}add <name> [address] [phones] [email] [birthday]{COLORS.cyan} — Add a new contact",
        f"• {COLORS.green_light}edit <name> [new_address] [phones] [email] [birthday]{COLORS.cyan} — Edit existing contact",
        f"• {COLORS.green_light}delete <name>{COLORS.cyan} — Delete a contact",
        f"• {COLORS.green_light}search{COLORS.cyan} — Search contacts by name or phone",
        f"• {COLORS.green_light}birthdays{COLORS.cyan} — Show upcoming birthdays",
        f"• {COLORS.green_light}show{COLORS.cyan} — Show all saved contacts",
        f"• {COLORS.green_light}back{COLORS.cyan} — Return to main menu",
        f"• {COLORS.green_light}help{COLORS.cyan} — Show contacts help menu",
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
        f"• {COLORS.green_light}help{COLORS.cyan}                     — Show notes help menu",
    ]
    for cmd in commands:
        print(line(cmd))

    print(border(top=False))


def print_help():
    print(border())
    print(line(f"{COLORS.cyan}🧭  MAIN MENU HELP"))
    print(separator())
    print(line(f"{COLORS.cyan}Available commands in main context:"))

    commands = [
        f"• {COLORS.green_light}contacts{COLORS.cyan} — Enter the Contacts module",
        f"• {COLORS.green_light}notes{COLORS.cyan}    — Enter the Notes module",
        f"• {COLORS.green_light}hello{COLORS.cyan}    — Get a greeting from the assistant",
        f"• {COLORS.green_light}help{COLORS.cyan}     — Show this help menu",
        f"• {COLORS.green_light}exit{COLORS.cyan}     — Save and exit the program",
    ]
    for cmd in commands:
        print(line(cmd))

    print(separator())
    print(
        line(
            f"{COLORS.cyan}🧩  Inside each module, type {COLORS.green_light}help{COLORS.cyan} to see available commands."
        )
    )
    print(border(top=False))


# ======================= CONTACTS MODULE USAGE MESSAGES  =======================
# Dispatches a help message based on module and command.
# If the module or command is unknown, shows a fallback error message.


def print_command_usage(module, command):
    usage_messages = {
        "contacts": {
            "add": print_add_contact_usage,
            "edit": print_edit_contact_usage,
            "delete": print_delete_contact_usage,
            "search": print_search_contact_usage,
            "birthdays": print_birthdays_usage,
            "show": print_show_contacts_usage,
        },
        # Future modules like "notes" can be added here
        # "notes": {
        #     "add": print_add_note_usage,
        #     ...
        # },
    }

    try:
        usage_messages[module][command]()
    except KeyError:
        print_unknown_command(command)


# Shows usage message for 'add' command in contacts module
def print_add_contact_usage():
    print_message_block(
        "🚀",
        f"Command {COLORS.yellow}add{COLORS.cyan} requires at least a <name> argument.",
        [
            f"{COLORS.cyan}📌  Usage: {COLORS.green_light}add <name> [address] [phones] [email] [birthday]",
            f"{COLORS.cyan}📎  Example: {COLORS.green_light}add John Kyiv 1234567890 john@email.com 01.01.1990",
        ],
    )


# Shows usage message for 'edit' command
def print_edit_contact_usage():
    print_message_block(
        "🛠️",
        f"Command {COLORS.yellow}edit{COLORS.cyan} requires at least a <name> to locate the contact.",
        [
            f"{COLORS.cyan}📌  Usage: {COLORS.green_light}edit <name> [new_address] [phones] [email] [birthday]",
            f"{COLORS.cyan}📎  Example: {COLORS.green_light}edit John NewYork 0987654321 new@email.com 02.02.1992",
        ],
    )


# Shows usage message for 'delete' command
def print_delete_contact_usage():
    print_message_block(
        "🗑️",
        f"Command {COLORS.yellow}delete{COLORS.cyan} requires a <name> of the contact to remove.",
        [
            f"{COLORS.cyan}📌  Usage: {COLORS.green_light}delete <name>",
            f"{COLORS.cyan}📎  Example: {COLORS.green_light}delete John",
        ],
    )


# Generic success message renderer (used for things like 'updated')
def print_success_message(message: str):
    print(border())
    print(line(f"{COLORS.success}✅ {message}"))
    print(border(top=False))


# Generic error message renderer
def print_error_message(message: str):
    print(border())
    print(line(f"{COLORS.error}⛔  {message}"))
    print(border(top=False))


# Shows usage message for 'search' command
def print_search_contact_usage():
    print(border())
    print(line(f"{COLORS.cyan}ℹ️  You can search contacts by name or phone number"))
    print(separator())
    print(line(f"{COLORS.cyan}Follow prompts to complete search."))
    print(border(top=False))


# Shows usage message for 'birthdays' command
def print_birthdays_usage():
    print(border())
    print(line(f"{COLORS.cyan}ℹ️  View upcoming birthdays"))
    print(separator())
    print(line(f"{COLORS.cyan}Enter number of days to look ahead."))
    print(
        line(f"{COLORS.cyan}Example: {COLORS.green_light}7  {COLORS.cyan}(next 7 days)")
    )
    print(border(top=False))


# Shows usage message for 'show' command
def print_show_contacts_usage():
    print(border())
    print(line(f"{COLORS.cyan}ℹ️  Displaying all saved contacts"))
    print(separator())
    print(line(f"{COLORS.cyan}No additional arguments required."))
    print(border(top=False))


# ---------------------------- SHARED HELPERS ----------------------------


# Renders a full info block with border and emoji, including body lines
def print_message_block(title_emoji, title, body_lines):
    print(border())
    print(line(f"{COLORS.cyan}{title_emoji}  {title}"))
    print(separator())
    for l in body_lines:
        print(line(l))
    print(border(top=False))


# ======================= END =======================
