from Classes.Lab_2.base_calculator import *
from Shared.Command.Command import Command


class SetNum1Command(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: BaseCalculator, number: float):
        self.__executor = executor
        self.__number = number

    def execute(self) -> None:
        self.__executor.num_1 = self.__number
