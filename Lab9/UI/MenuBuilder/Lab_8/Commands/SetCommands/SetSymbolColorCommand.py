from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetSymbolColorCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, symbol_color: str):
        self.__executor = executor
        self.__symbol_color = symbol_color

    def execute(self) -> None:
        self.__executor.symbol_color = self.__symbol_color
