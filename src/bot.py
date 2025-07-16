# import ui_helpers
import storage  

from collections import UserDict
import re
from datetime import datetime

# -------------------- КЛАСИ --------------------

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name is required")
        super().__init__(value)

class Address(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Address is required")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone must be 10 digits")
        super().__init__(value)

class Email(Field):
    def __init__(self, value):
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.phones = []
        self.emails = []
        self.birthday = None

    def add_address(self, address):
        self.address = Address(address)

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_email(self, email_address):
        self.emails.append(Email(email_address))

    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)

    def __str__(self):
        name = self.name.value
        address = self.address.value if self.address else "No address"
        phones = ", ".join(phone.value for phone in self.phones) or "No phone"
        emails = ", ".join(email.value for email in self.emails) or "No email"
        birthday = self.birthday.value if self.birthday else "No birthday"
        return f"Contact name: {name}, address: {address}, phone: {phones}, email: {emails}, birthday: {birthday}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# -------------------- ПАРСЕР КОМАНД --------------------

def parse_input(user_input):
    parts = user_input.strip().split()
    return parts[0].lower(), parts[1:]

# -------------------- ДОДАВАННЯ КОНТАКТУ --------------------

def add_contact(book, args):
    print("Adding new contact (or press Enter to cancel)")

    name = input("Enter name: ").strip()
    if not name:
        print("Canceled.")
        return

    try:
        record = Record(name)

        address = input("Enter address or press Enter to skip: ").strip()
        if address:
            record.add_address(address)

        phone_input = input("Enter phone numbers (10 digits, comma-separated) or press Enter to skip: ").strip()
        if phone_input:
            phones = [p.strip() for p in phone_input.split(",")]
            for phone in phones:
                record.add_phone(phone)

        email = input("Enter email or press Enter to skip: ").strip()
        if email:
            record.add_email(email)

        birthday = input("Enter birthday (DD.MM.YYYY) or press Enter to skip: ").strip()
        if birthday:
            record.add_birthday(birthday)

        book.add_record(record)
        print("Contact added successfully")

    except ValueError as e:
        print(f"Error: {e}")

# -------------------- ОСНОВНИЙ ЦИКЛ --------------------

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            add_contact(book, args)

        elif command == "show":
            print("All contacts:")
            print(book)

        else:
            print("Invalid command.")

# -------------------- ЗАПУСК --------------------

# if __name__ == "__main__":
#     main()


# def main():
#     ui_helpers.print_welcome()
#     # read file
#     book = storage.load_data()
#     while True:
#         command, args = ui_helpers.parse_input()

#         if command is None:
#             continue

#         if command in ["close", "exit"]:
#             # save
#             storage.save_data(book)
#             ui_helpers.print_exit_message()
#             break
#         elif command == "hello":
#             ui_helpers.print_greeting_response()
#         elif command == "help":
#             ui_helpers.print_help()
#         elif command == "contacts":
#             ui_helpers.handle_contacts_module()
#         elif command == "notes":
#             ui_helpers.handle_notes_module()
#         else:
#             ui_helpers.print_unknown_command()


def test_bot():
    pass  # Placeholder for bot tests


def test_file():
    pass  # Placeholder for file save and load tests


if __name__ == "__main__":
    test_bot()
    test_file()
    main()
