from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetFontCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, font: str):
        self.__executor = executor
        self.__font = font

    def execute(self) -> None:
        self.__executor.font = self.__font
