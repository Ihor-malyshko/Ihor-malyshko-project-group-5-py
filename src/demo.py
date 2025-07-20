import time
import random
import contacts_helper as contacts
import notes_helper as notes_helper
from address_book import Record, AddressBook
from ui.style_settings import COLORS
from ui.ui_helpers import border, line, center_line, separator
import ui.ui_screens as ui_screens

def simulate_typing(command):
        # Print terminal header with proper colors
        print(f"╭─[{COLORS.magenta}assistant-terminal{COLORS.reset}]")
        print(f"╰─{COLORS.green}>>> {COLORS.reset}", end="", flush=True)
        
        for char in command:
            print(char, end="", flush=True)
            # Add random typing speed variations to look more realistic
            if random.random() < 0.05:
                time.sleep(random.uniform(0.2, 0.5))  # Pause like thinking
            elif random.random() < 0.2:
                time.sleep(random.uniform(0.08, 0.15))  # Slight pause
            else:
                time.sleep(random.uniform(0.03, 0.07))  # Normal typing speed
        print()


def print_demo():
    """Simulates a user interacting with the personal assistant by typing commands"""

    # Create a temporary address book for the demo
    demo_book = AddressBook()
    
    # Function to simulate user typing with realistic delays
    
    
    print(border())
    print(line(f"📽️{COLORS.cyan}{COLORS.bright}  INTERACTIVE DEMO MODE{COLORS.reset}      "))
    print(line(f"{COLORS.cyan}Watching a simulation of typical user interactions...{COLORS.reset}"))
    print(separator())
    
    # Demo sequence 1: Contacts management
    simulate_typing("contacts")
    ui_screens.handle_contacts_module()
    input()  # Wait for user input before continuing
    
    
    simulate_typing("add Maks  0987654321")
    contacts.add_contact(demo_book, ["Maks", "", "0987654321"])
    time.sleep(1.5)
    
    simulate_typing("add Maks Lviv 0987654321")
    contacts.add_contact(demo_book, ["Maks", "Lviv", "0987654321"])
    time.sleep(1.5)
    
    simulate_typing("add John Kyiv 0981234567 john@example.com 15.05.1990")
    contacts.add_contact(demo_book, ["John", "Kyiv", "0981234567", "john@example.com", "15.05.1990"])
    time.sleep(1.5)
    
    simulate_typing("add Alice London 0501112233 alice@example.com 20.07.1988")
    contacts.add_contact(demo_book, ["Alice", "London", "0501112233", "alice@example.com", "20.07.1988"])
    time.sleep(1.5)
    
    simulate_typing("show")
    contacts.show_all_contacts(demo_book)
    time.sleep(1.5)
    
    simulate_typing("edit John NewYork 0987654321 john.doe@example.com")
    contacts.edit_contact(demo_book, ["John", "NewYork", "0987654321", "john.doe@example.com"])
    time.sleep(1.5)
    
    simulate_typing("show")
    contacts.show_all_contacts(demo_book)    
    input()  # Wait for user input before continuing
    
    # Demo sequence 2: Switch to notes
    simulate_typing("notes")
    ui_screens.handle_notes_module()
    input()  # Wait for user input before continuing
    
    
    simulate_typing("add John, important work, Meeting notes for John")
    notes_helper.add_note(demo_book, ["John,", "important work,", "work Meeting notes for John"])
    time.sleep(1.5)
    
    
    simulate_typing("show")
    notes_helper.show_contacts_with_notes(demo_book)
    time.sleep(1.5)
    
    simulate_typing("add Alice, work London,")
    notes_helper.add_note(demo_book, ["Alice,", "work London,"])
    time.sleep(1.5)

    simulate_typing("contacts")
    ui_screens.handle_contacts_module()
    simulate_typing("add Andrii address 1234567890")
    contacts.add_contact(demo_book, ["Andrii", "address", "1234567890"])
    time.sleep(0.5)
    simulate_typing("notes")
    ui_screens.handle_notes_module()
    time.sleep(0.5)
    simulate_typing("add Andrii, family, Something interesting about this person")
    notes_helper.add_note(demo_book, ["Andrii,", "family,", "Something interesting about this person"])
    time.sleep(0.5)
    
    input()  # Wait for user input before continuing
    
    
    simulate_typing("search work")
    notes_helper.search_contacts_by_tag(demo_book, "work")
    time.sleep(1.5)
    
    simulate_typing("search family")
    notes_helper.search_contacts_by_tag(demo_book, "family")
    time.sleep(1.5)
    
    input()  # Wait for user input before continuing
    
    simulate_typing("contacts")
    ui_screens.handle_contacts_module()
    simulate_typing("show")
    contacts.show_all_contacts(demo_book)
    time.sleep(1.5)
    input()  # Wait for user input before continuing