from Shared.StylizeSymbol.Classes.StylizeSymbol import StylizeSymbol
from Shared.Command.Command import Command


class SetColorCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: StylizeSymbol, color: str):
        self.__executor = executor
        self.__color = color

    def execute(self) -> None:
        self.__executor.color = self.__color
