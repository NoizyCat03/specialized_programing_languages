from Shared.StylizeSymbol.Classes.StylizeSymbol import StylizeSymbol
from Shared.Command.Command import Command


class SetMessageCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: StylizeSymbol, message: str):
        self.__executor = executor
        self.__message = message

    def execute(self) -> None:
        self.__executor.line = self.__message
