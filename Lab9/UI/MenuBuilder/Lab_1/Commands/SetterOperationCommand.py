from Classes.Lab_2.base_calculator import *
from Shared.Command.Command import Command


class SetOperatorCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: BaseCalculator, operator: str):
        self.__executor = executor
        self.__operator = operator

    def execute(self) -> None:
        self.__executor.operator = self.__operator
