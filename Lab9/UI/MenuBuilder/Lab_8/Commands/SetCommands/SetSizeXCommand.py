from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetSizeXCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, size_x: str):
        self.__executor = executor
        self.__size_x = size_x

    def execute(self) -> None:
        self.__executor.size_x = self.__size_x
