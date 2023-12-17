from Shared.Console.Print.ConsolePrint import ConsolePrint
from Shared.Command.Command import Command


class PrintCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: ConsolePrint):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.print()
