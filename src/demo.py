import time
import random
import contacts_helper as contacts
from address_book import Record, AddressBook
from ui.style_settings import COLORS
from ui.ui_helpers import border, line, center_line, separator
import ui.ui_screens as ui_screens


def print_demo():
    """Simulates a user interacting with the personal assistant by typing commands"""

    # Create a temporary address book for the demo
    demo_book = AddressBook()
    
    # Function to simulate user typing with realistic delays
    def simulate_typing(command):
        print(f"{COLORS.green}> {COLORS.reset}", end="", flush=True)
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
        time.sleep(0.8)  # Pause after command
    
    print(border())
    print(line(f"{COLORS.cyan}{COLORS.bright}📽️  INTERACTIVE DEMO MODE{COLORS.reset}"))
    print(line(f"{COLORS.cyan}Watching a simulation of typical user interactions...{COLORS.reset}"))
    print(separator())
    time.sleep(1.5)
    
    # Demo sequence 1: Contacts management
    simulate_typing("contacts")
    ui_screens.handle_contacts_module()
    time.sleep(1.5)
    
    simulate_typing("add John Kyiv 0981234567 john@example.com 15.05.1990")
    contacts.add_contact(demo_book, ["John", "Kyiv", "0981234567", "john@example.com", "15.05.1990"])
    time.sleep(1.5)
    
    simulate_typing("add Alice London 0501112233 alice@example.com 20.07.1988")
    contacts.add_contact(demo_book, ["Alice", "London", "0501112233", "alice@example.com", "20.07.1988"])
    time.sleep(1.5)
    
    simulate_typing("show")
    contacts.show_all_contacts(demo_book)
    time.sleep(2)
    
    simulate_typing("edit John NewYork 0987654321 john.doe@example.com")
    contacts.edit_contact(demo_book, ["John", "NewYork", "0987654321", "john.doe@example.com"])
    time.sleep(1.5)
    
    simulate_typing("show")
    contacts.show_all_contacts(demo_book)
    time.sleep(2)
    
    # Demo sequence 2: Switch to notes
    simulate_typing("notes")
    ui_screens.handle_notes_module()
    time.sleep(1.5)
    
    
    input()  # Wait for user input before continuing