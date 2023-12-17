from Shared.Console.Input import InputValue
from Shared.Command.Command import Command


class ConvertStringObjectCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: InputValue, message: str):
        self.__executor = executor
        self.__message = message

    def execute(self) -> None:
        self.__executor.convert__string_object(self.__message)
