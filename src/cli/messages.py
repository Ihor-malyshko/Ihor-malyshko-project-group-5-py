from dataclasses import dataclass


@dataclass(frozen=True)
class Messages:
    UNKNOWN_COMMAND = "Command '{}' not recognized.💡 Did you mean: {}?"
    ERROR_OCCURRED = "An error occurred: {}"
    INVALID_CONTEXT = "Invalid context: {}"


@dataclass(frozen=True)
class ErrorMessages:
    INVALID_COMMAND = "Invalid command: {}"
    INVALID_ARGUMENTS = "Invalid arguments for command: {}"
    CONTEXT_ERROR = "Cannot switch to context: {}"
