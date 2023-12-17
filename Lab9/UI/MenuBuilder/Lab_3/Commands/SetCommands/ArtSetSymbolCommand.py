from Shared.Command.Command import Command
from Classes.Lab_3.art_generator import ArtGenerator


class ArtSetSymbolCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: ArtGenerator, symbol: str):
        self.__executor = executor
        self.__symbol = symbol

    def execute(self) -> None:
        self.__executor.symbol = self.__symbol
