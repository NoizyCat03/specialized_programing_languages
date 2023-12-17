from Shared.Console.Print.ConsolePrint import ConsolePrint
from Shared.Command.Command import Command


class SetOutputCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: ConsolePrint, output: str):
        self.__executor = executor
        self.__output = output

    def execute(self) -> None:
        self.__executor.output = self.__output
