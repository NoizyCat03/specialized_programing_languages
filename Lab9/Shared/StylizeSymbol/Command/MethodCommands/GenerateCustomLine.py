from Shared.StylizeSymbol.Classes.StylizeSymbol import StylizeSymbol
from Shared.Command.Command import Command


class GenerateCustomLineCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: StylizeSymbol):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.generate_custom_line()
