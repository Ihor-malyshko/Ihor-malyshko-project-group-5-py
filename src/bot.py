import pickle
from colorama import init, Fore
from AddressBook import AddressBook

init()

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # init AddressBook if file not found
        return AddressBook()  

def parse_input():
    user_input = input("Enter a command: ")
    # Handle empty input
    if not user_input.strip():
        print(f"{Fore.RED}Error{Fore.RESET}: Empty input. Please enter a command.")
        return None, []
    
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except Exception:
        print(f"{Fore.RED}Error{Fore.RESET}: Invalid command format.")
        return None, []



def main():
    print("Welcome to the assistant bot!")
    # read file
    book = load_data()
    while True:
        command, args = parse_input()
        
        if command is None:
            continue
            
        if command in ["close", "exit"]:
            # save 
            save_data(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")


def test_bot():
  pass  # Placeholder for bot tests

def test_file():
  pass  # Placeholder for file save and load tests

if __name__ == "__main__":
    test_bot()
    test_file()
    main()