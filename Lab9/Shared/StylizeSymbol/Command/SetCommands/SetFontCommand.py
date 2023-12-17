from Shared.StylizeSymbol.Classes.StylizeSymbol import StylizeSymbol
from Shared.Command.Command import Command


class SetFontCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: StylizeSymbol, font: str):
        self.__executor = executor
        self.__font = font

    def execute(self) -> None:
        self.__executor.color = self.__font
