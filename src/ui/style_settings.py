import re
from colorama import Fore, Style
from prompt_toolkit.styles import Style as PromptStyle
from typing import NamedTuple

# Layout settings
BOX_WIDTH = 58
FULL_WIDTH = BOX_WIDTH + 2

# ANSI regex for width calculation
ANSI_ESCAPE_RE = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")

# Prompt style
cli_style = PromptStyle.from_dict(
    {
        "prompt": "#ff00ff bold",
        "bracket": "#00ffff",
        "arrow": "#00ff00 bold",
        "": "#00cc44 bold",
    }
)



class Colors(NamedTuple):
    green: str
    green_light: str
    cyan: str
    cyan_light: str
    yellow: str
    magenta: str
    blue: str
    bright: str
    reset: str


COLORS = Colors(
    green=Fore.GREEN,
    green_light=Fore.LIGHTGREEN_EX,
    cyan=Fore.CYAN,
    cyan_light=Fore.LIGHTCYAN_EX,
    yellow=Fore.YELLOW,
    magenta=Fore.MAGENTA,
    blue=Fore.BLUE,
    bright=Style.BRIGHT,
    reset=Style.RESET_ALL,
)
