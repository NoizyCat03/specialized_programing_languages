from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetColorArea3Command(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, color_area_3: str):
        self.__executor = executor
        self.__color_area_3 = color_area_3

    def execute(self) -> None:
        self.__executor.color_3 = self.__color_area_3
