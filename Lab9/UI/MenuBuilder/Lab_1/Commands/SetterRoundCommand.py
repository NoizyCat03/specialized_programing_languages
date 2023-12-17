from Classes.Lab_2.base_calculator import *
from Shared.Command.Command import Command


class SetCustomRoundCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: BaseCalculator, custom_round: int):
        self.__executor = executor
        self.__custom_round = custom_round

    def execute(self) -> None:
        self.__executor.custom_round = self.__custom_round
