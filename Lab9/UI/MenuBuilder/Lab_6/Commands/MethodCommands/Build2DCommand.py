from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class Build2DCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.build_2d()
