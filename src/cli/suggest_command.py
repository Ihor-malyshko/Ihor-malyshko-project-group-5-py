from difflib import get_close_matches
from typing import Optional, List

SUGGESTION_MATCHES_COUNT = 2
SUGGESTION_CUTOFF = 0.5


def suggest_command(command: str, available_commands: List[str]) -> Optional[str]:
    """
    Suggest the closest matching command from a list of available commands
    based on the input command string.

    Uses fuzzy matching to find the best candidate command similar to the input.

    :param command: The command string to match.
    :param available_commands: A list of valid command strings to match against.
    :return: The closest matching command if found; otherwise, None.
    """
    matches = get_close_matches(
        command,
        available_commands,
        n=SUGGESTION_MATCHES_COUNT,
        cutoff=SUGGESTION_CUTOFF,
    )
    return matches[0] if matches else None
