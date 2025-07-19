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


def parse_input(session, command_completer):
    """
    Prompt user for input using custom CLI style.
    Returns:
        tuple[str | None, list[str]]: (command, arguments)
    """
    user_input = session.prompt(
        [
            ("class:bracket", "╭─["),
            ("class:prompt", "assistant-terminal"),
            ("class:bracket", "]\n"),
            ("class:arrow", "╰─>>> "),
        ],
        style=cli_style,
        completer=command_completer,
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


def render_table(data, headers=None, row_color=None):
    """
    data: list of lists (rows)
    headers: list of column names
    row_color: optional color for rows
    """
    from ui.style_settings import COLORS

    if not data:
        print(f"{COLORS.yellow}⚠️  No data to display.{COLORS.reset}")
        return

    # If headers not provided — use keys from first row if it's a dict
    if headers is None:
        if isinstance(data[0], dict):
            headers = list(data[0].keys())
            data = [[str(row.get(col, "—")) for col in headers] for row in data]
        else:
            headers = [f"Column {i+1}" for i in range(len(data[0]))]

    # Determine max column widths
    col_widths = [len(h) for h in headers]
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    def horizontal_line(left, middle, right, fill="─"):
        return left + middle.join(fill * (w + 2) for w in col_widths) + right

    def format_row(row, sep="│", color=None):
        styled = []
        for i, cell in enumerate(row):
            c = str(cell)
            styled.append(f" {color or ''}{c:<{col_widths[i]}}{COLORS.reset} ")
        return sep + sep.join(styled) + sep

    # Print table
    print(horizontal_line("┌", "┬", "┐"))
    print(format_row(headers, color=COLORS.cyan + COLORS.bright))
    print(horizontal_line("├", "┼", "┤"))

    for row in data:
        print(format_row(row, color=row_color or COLORS.green_light))

    print(horizontal_line("└", "┴", "┘"))
