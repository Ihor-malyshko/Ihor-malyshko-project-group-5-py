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
# 🤖 Personal CLI Assistant

A modular command-line assistant written in Python with support for contact and note management, enhanced by a futuristic styled interface.

---

## ✨ CLI Interface & Styling

A futuristic command-line interface with:

- 🌈 Colored text and emoji icons
- 📦 Custom UI components:
  - Contact tables with ASCII-style borders
  - Instruction blocks for command usage
  - Colored highlighting for arguments, examples, and command names
- 🎨 Unified message styling for success, error, and info messages

Integrated using [`colorama`](https://pypi.org/project/colorama/) and [`prompt_toolkit`](https://python-prompt-toolkit.readthedocs.io/).


