from Shared.Console.Input import InputValue
from Shared.Command.Command import Command


class SetInputMessageCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: InputValue, message: str):
        self.__executor = executor
        self.__message = message

    def execute(self) -> None:
        self.__executor.message = self.__message
