# 🤖 Address Book CLI Bot

This project is a **command-line assistant** for managing a personal address book. It allows users to add, edit, search, and delete contacts, store birthdays, and receive birthday reminders for the upcoming week.

# project-group-5-py
Ihor-malyshko/project-group-5-py

Team name {довге тире} Bug Busters

Команда:
Vasylyna Bizniakova- vbiznyakova@gmail.com
Yatsenko_Serhii - serhii2111@yahoo.com
Kateryna - kukuruzova.ekaterina@gmail.com
Ihor Malyshko - malishkoio@gmail.com

board - https://github.com/users/Ihor-malyshko/projects/4/views/1

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Ihor-malyshko/project-group-5-py
cd project-group-5-py
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

* **PowerShell (Windows):**

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

* **Command Prompt (Windows):**

  ```cmd
  venv\Scripts\activate.bat
  ```

* **macOS / Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the assistant bot

#### Manually:

```bash
cd src
python bot.py
```

#### Or via script (Windows only):

* For Command Prompt:

  ```cmd
  .\run.bat
  ```

* For PowerShell:

  ```powershell
  .\run.ps1
  ```

---

## 💬 Supported Commands

| Command                        | Arguments                         | Description                                                  |
|-------------------------------|-----------------------------------|--------------------------------------------------------------|
| `hello`                       | –                                 | Greets the user.                                             |
| `add [name] [phone]`          | Name, phone number                | Adds a new contact or a phone number to an existing one.     |
| `edit [name] [old] [new]`   | Name, old phone, new phone        | Replaces an old phone number with a new one.                 |
| `phone [name]`                | Name                              | Displays the phone number(s) for a contact.                  |
| `show`                         | –                                 | Lists all saved contacts.                                    |
| `birthdays`                   | –                                 | Lists birthdays for the upcoming week.                       |
| `help`, `-h`                  | –                                 | Displays all available commands.                             |
| `exit`, `close`               | –                                 | Exits the program.                                           |

---

## 🧠 Features

- 📚 **Contact Management**  
  Contacts are stored in a custom `AddressBook` class based on `UserDict`.

- 📝 **Contact Notes**  
  Allows users to add personal notes to each contact for additional context or information.

- 🔡 **Command Autocomplete**  
  Supports command autocompletion for faster and easier CLI interaction.


## 🧪 Example Usage

TODO

## 🏁 Exiting the Program

To close the bot, type:

```
exit
```