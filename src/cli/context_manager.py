from cli.command_completer import CommandCompleter
from typing import Callable, Dict, Optional, List
from cli.enums import Context
from cli.messages import Messages


class ContextManager:
    """Manages application contexts and their associated commands."""

    def __init__(self):
        self.current_context = Context.MAIN
        self.commands_by_context: Dict[Context, List[str]] = {}
        self.command_completer: Optional[CommandCompleter] = None

    def register_commands(self, context: Context, commands: List[str]) -> None:
        """
        Register available commands for a context.

        :param context: Context to register commands for
        :param commands: List of available commands
        """
        self.commands_by_context[context] = commands
        self._update_completer()

    @property
    def available_commands(self) -> List[str]:
        return self.commands_by_context.get(self.current_context, [])

    def switch_context(
        self, context: Context, on_switch: Optional[Callable] = None
    ) -> None:
        """
        Switch to a different context.

        :param context: Context to switch to
        """
        if context not in Context:
            raise ValueError(Messages.INVALID_CONTEXT.format(context))

        self.current_context = context
        self._update_completer()
        if on_switch:
            on_switch()

    def _update_completer(self) -> None:
        """Update command completer for current context."""
        commands = self.commands_by_context.get(self.current_context, [])
        self.command_completer = CommandCompleter(commands)
