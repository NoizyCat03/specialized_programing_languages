from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetSizeZCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, size_z: int):
        self.__executor = executor
        self.__size_z = size_z

    def execute(self) -> None:
        self.__executor.size_z = self.__size_z
