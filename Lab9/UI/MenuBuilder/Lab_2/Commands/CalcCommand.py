from Classes.Lab_2.base_calculator import *
from Shared.Command.Command import Command


class CalcCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: BaseCalculator):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.calc()
