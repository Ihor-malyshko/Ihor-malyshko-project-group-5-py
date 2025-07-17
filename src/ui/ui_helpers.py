from prompt_toolkit import prompt
from wcwidth import wcswidth
from ui.style_settings import FULL_WIDTH, ANSI_ESCAPE_RE, COLORS, cli_style


def strip_ansi(text: str) -> str:
    return ANSI_ESCAPE_RE.sub("", text)


def visible_width(text: str) -> int:
    return wcswidth(strip_ansi(text))


def border(top=True) -> str:
    line = "═" * (FULL_WIDTH + 2)
    return (
        f"{COLORS.magenta}{COLORS.bright}╔{line}╗"
        if top
        else f"{COLORS.magenta}╚{line}╝{COLORS.reset}"
    )


def separator() -> str:
    return f"{COLORS.magenta}╠{'═' * (FULL_WIDTH + 2)}╣"


def line(content: str) -> str:
    padding = FULL_WIDTH - visible_width(content)
    return f"{COLORS.cyan}║ {content}{' ' * max(padding, 0)} ║"


def center_line(content: str) -> str:
    vis_len = visible_width(content)
    total_pad = FULL_WIDTH - vis_len + 2
    left = total_pad // 2
    right = total_pad - left
    return f"{COLORS.cyan}║{' ' * left}{content}{' ' * right}║"

def parse_input():
    """
    Prompt user for input using custom CLI style.
    Returns:
        tuple[str | None, list[str]]: (command, arguments)
    """
    user_input = prompt(
        [
            ("class:bracket", "╭─["),
            ("class:prompt", "assistant-terminal"),
            ("class:bracket", "]\n"),
            ("class:arrow", "╰─>>> "),
        ],
        style=cli_style,
    )

    if not user_input.strip():
        lines = [
            "🧭  No input received.",
            "➤  Please enter a valid command.",
        ]
        print(border())
        for msg in lines:
            print(line(msg))
        print(border(top=False))
        return None, []

    cmd, *args = user_input.strip().split()
    return cmd.lower(), args
