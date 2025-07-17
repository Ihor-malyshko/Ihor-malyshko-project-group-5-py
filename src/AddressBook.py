from collections import UserDict
from datetime import datetime, timedelta
import re
from Note import Note 

# -------------------- КЛАСИ ПОЛІВ --------------------

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
            parsed = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format")
        self.value = parsed

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

# -------------------- КЛАС ЗАПИСУ --------------------

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.phones = []
        self.emails = []
        self.birthday = None
        self.note = None

    def add_address(self, address):
        self.address = Address(address)

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_email(self, email_address):
        self.emails.append(Email(email_address))

    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)
    
    def add_note(self, note):
        self.note = Note(note)
    def get_note(self):
        if not self.note:
            return None
        return self.note

    def __str__(self):
        name = self.name.value
        address = self.address.value if self.address else "No address"
        phones = ", ".join(phone.value for phone in self.phones) or "No phone"
        emails = ", ".join(email.value for email in self.emails) or "No email"
        birthday = str(self.birthday) if self.birthday else "No birthday"
        note = self.note if self.note else "No note"
        return f"Contact name: {name}, address: {address}, phone: {phones}, email: {emails}, birthday: {birthday}, note: {note}"

# -------------------- АДРЕСНА КНИГА --------------------

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

    def get_upcoming_birthdays(self, days_ahead):
        congratulation_dates = []
        today = datetime.today().date()

        for record in self.data.values():
            if record.birthday:
                bday = record.birthday.value.date()
                bday_this_year = bday.replace(year=today.year)

                if bday_this_year < today:
                    bday_this_year = bday_this_year.replace(year=today.year + 1)

                days_until = (bday_this_year - today).days

                if 0 <= days_until <= days_ahead:
                    congratulation_date = bday_this_year
                    if congratulation_date.weekday() in (5, 6):
                        congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

                    congratulation_dates.append({
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                    })

        return congratulation_dates

    def __str__(self):
        if not self.data:
            return "Address book is empty."
      
        return "\n".join(str(record) for record in self.data.values())