import pickle
import os
import sys
from address_book import AddressBook

# Absolute path to the data file stored in the same directory as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "addressbook.pkl")

# Cтворює псевдонім для модуля, щоб pickle міг знайти потрібний клас
sys.modules['AddressBook'] = sys.modules.get('address_book', sys.modules[__name__])


def save_data(book, filename=FILE_PATH):
    """
    Serialize and save the AddressBook object to a file using pickle.
    The file will be saved in the same folder as this script by default.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=FILE_PATH):
    """
    Load and return the AddressBook object from a file.
    If the file does not exist, return a new empty AddressBook instance.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, ModuleNotFoundError, AttributeError):
        return AddressBook()
