# 🤖 Address Book CLI Bot

This project is a **command-line assistant** for managing a personal address book. It allows users to add, edit, search, and delete contacts, store birthdays, and receive birthday reminders for the upcoming week.

## 👥 Team

**Team Name:** Bug Busters

**Members:**
- **Vasylyna Bizniakova** — [vbiznyakova@gmail.com](mailto:vbiznyakova@gmail.com)
- **Yatsenko Serhii** — [serhii2111@yahoo.com](mailto:serhii2111@yahoo.com)
- **Kateryna Kukuruzova** — [kukuruzova.ekaterina@gmail.com](mailto:kukuruzova.ekaterina@gmail.com)
- **Ihor Malyshko** — [malishkoio@gmail.com](mailto:malishkoio@gmail.com)

**Project Board:** [GitHub Project Board](https://github.com/users/Ihor-malyshko/projects/4/views/1)

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

| Context      | Command                                                 | Arguments / Format               | Description                      |
| ------------ | ------------------------------------------------------- | -------------------------------- | -------------------------------- |
| **Main**     | `contacts`                                              | –                                | Enter the Contacts module        |
|              | `notes`                                                 | –                                | Enter the Notes module           |
|              | `hello`                                                 | –                                | Greet the assistant              |
|              | `help`                                                  | –                                | Show main help menu              |
|              | `exit`                                                  | –                                | Save and exit the program        |
| **Contacts** | `add <name> [address] [phones] [email] [birthday]`      | Name (required), others optional | Add a new contact                |
|              | `edit <name> [new_address] [phones] [email] [birthday]` | Name (required), others optional | Edit existing contact            |
|              | `delete <name>`                                         | Name                             | Delete a contact                 |
|              | `search`                                                | –                                | Search contacts by name or phone |
|              | `birthdays`                                             | Number of days (e.g. `7`)        | Show upcoming birthdays          |
|              | `show`                                                  | –                                | Show all saved contacts          |
|              | `back`                                                  | –                                | Return to main menu              |
|              | `help`                                                  | –                                | Show contacts help menu          |
| **Notes**    | `add [note text]`                                       | Optional note text               | Add a new note                   |
|              | `edit [note id]`                                        | ID of the note                   | Edit an existing note            |
|              | `delete [note id]`                                      | ID of the note                   | Delete a note                    |
|              | `search [query]`                                        | Search query                     | Search notes                     |
|              | `list-tags`                                             | –                                | List all tags used in notes      |
|              | `back`                                                  | –                                | Return to main menu              |
|              | `help`                                                  | –                                | Show notes help menu             |



---

## 🧠 Features

- 📚 **Contact Management**  
  Contacts are stored in a custom `AddressBook` class based on `UserDict`.

- 📝 **Contact Notes**  
  Allows users to add personal notes to each contact for additional context or information.

- 🔡 **Command Autocomplete**  
  Supports command autocompletion for faster and easier CLI interaction.

  This feature provides an intelligent autocomplete system for CLI commands using `prompt_toolkit`. It enhances user experience by suggesting valid commands as the user types — minimizing typos and speeding up command entry.

### 🔑 Key Components

- **Context-Aware Autocompletion**  
  Autocompletion adapts to the current context (`MAIN`, `CONTACTS`, `NOTES`) — only valid commands are suggested based on where you are.

- **Tab Completion Support**  
  Just like in traditional CLI environments, pressing `Tab` autocompletes the command you're typing (if there's a match), or shows a list of possible completions.

- **First-Word Command Matching**  
  Only the first word (command name) is completed — arguments are not autocompleted to avoid noise.

- **Live Inline Suggestions**  
  As you type, matching commands appear instantly. Matching is case-insensitive and continuously updates.

- **Command History Navigation**  
  Use `↑` / `↓` to scroll through your command history.

- **Safe Exit Handling**  
  Pressing `Ctrl+C` exits gracefully — data is saved, and an exit message is displayed.

- **Fuzzy Matching for Mistyped Commands**  
  If a command is misspelled, the system uses fuzzy matching to suggest a correction and asks for confirmation before executing it.


### 🧠 Example Interaction

```bash
> shuws
Command 'shuws' not recognized.💡 Did you mean: show? [y/n]: y

┌────────────────┬─────────┬────────────┬───────┬──────────┬──────┐
│ Name           │ Address │ Phone      │ Email │ Birthday │ Note │
├────────────────┼─────────┼────────────┼───────┼──────────┼──────┤
│ John           │ Kyiv    │ 1234567890 │ —     │ —        │ —    │
│ Hogn           │ Kyiv    │ —          │ —     │ —        │ —    │
│ name           │ —       │ —          │ —     │ —        │ —    │
│ John_Greygooze │ Kyiv    │ 1234567890 │ —     │ —        │ —    │
└────────────────┴─────────┴────────────┴───────┴──────────┴──────┘
```

---

## 🧪 Example Usage

TODO

## 🏁 Exiting the Program

To close the bot, type:

```
exit
```