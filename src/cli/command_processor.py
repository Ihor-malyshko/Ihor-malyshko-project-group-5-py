from typing import Callable, Dict, Optional, List
import ui.ui_screens as ui_screens
from cli.confirm import confirm
from cli.suggest_command import suggest_command
from cli.enums import Context
from cli.messages import Messages


class CommandProcessor:
    """Processes and executes commands with their handlers."""

    def __init__(self, context_manager):
        self.handlers_by_context: Dict[Context, Dict[str, Callable]] = {}
        self.context_manager = context_manager

    def register_handlers(self, context: str, handlers: Dict[str, Callable]) -> None:
        """
        Register command handlers for a context.

        :param context: Context to register handlers for
        :param handlers: Command handlers mapping
        """
        self.handlers_by_context[context] = handlers

    def process_command(
        self,
        command: str,
        args: List[str],
        context: Context,
    ) -> Optional[str]:
        """
        Process a command in the current context.

        :return: Command execution result if any
        """
        handlers = self.handlers_by_context.get(context, {})
        handler = handlers.get(command)

        if not handler:
            return self._handle_invalid_command(command, args, context)

        return handler(args)

    def _handle_invalid_command(
        self,
        command: str,
        args: List[str],
        context: Context,
    ) -> Optional[str]:
        """Handle invalid command by suggesting alternatives."""

        available_commands = self.context_manager.available_commands
        suggestion = suggest_command(command, available_commands)
        if not suggestion:
            ui_screens.print_unknown_command(command)
            return None

        message = Messages.UNKNOWN_COMMAND.format(command, suggestion)
        if confirm(message):
            return self.process_command(suggestion, args, context)
        return None
