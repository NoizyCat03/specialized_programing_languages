from Shared.Console.Input import InputValue
from Shared.Command.Command import Command


class InputFloatNumberCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: InputValue):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.input_float_number()
