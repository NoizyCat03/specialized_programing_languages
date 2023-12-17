from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetColorArea1Command(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, color_area_1: str):
        self.__executor = executor
        self.__color_area_1 = color_area_1

    def execute(self) -> None:
        self.__executor.color_1 = self.__color_area_1
