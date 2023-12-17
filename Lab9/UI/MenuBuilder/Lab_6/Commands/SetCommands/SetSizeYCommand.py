from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetSizeYCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, size_y: int):
        self.__executor = executor
        self.__size_y = size_y

    def execute(self) -> None:
        self.__executor.size_y = self.__size_y
