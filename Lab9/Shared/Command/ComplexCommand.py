"""
Module defining the ComplexCommand class.
"""

import logging
from Shared.Command.Command import Command


class ComplexCommand:
    """
    ComplexCommand class that allows instant execution of a given command.
    """

    def __init__(self):
        logging.basicConfig(filename='Data/Log/example.log', encoding='utf-8', level=logging.DEBUG)
        """
        Constructor for the ComplexCommand class.
        Initializes the logger instance.
        """

    def instant_command(self, command: Command) -> None:
        """
        Executes a given command and logs information about the executed command.

        Args:
            command (Command): The command to be executed.
        """
        logging.info(command)
        command.execute()


# Example usage
# complex_command = ComplexCommand()
# command_to_execute = SomeConcreteCommand()
# complex_command.instant_command(command_to_execute)
