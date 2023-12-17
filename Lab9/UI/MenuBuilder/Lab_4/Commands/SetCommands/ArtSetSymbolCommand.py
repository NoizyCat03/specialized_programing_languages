from Shared.Command.Command import Command
from Classes.Lab_4.customArt import CustomArt


class ArtSetSymbolCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: CustomArt, symbol: str):
        self.__executor = executor
        self.__symbol = symbol

    def execute(self) -> None:
        self.__executor.symbol = self.__symbol
