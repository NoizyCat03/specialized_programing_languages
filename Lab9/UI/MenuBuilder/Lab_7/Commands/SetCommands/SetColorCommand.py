from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetColorCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, color: str):
        self.__executor = executor
        self.__color = color

    def execute(self) -> None:
        self.__executor.color = self.__color
