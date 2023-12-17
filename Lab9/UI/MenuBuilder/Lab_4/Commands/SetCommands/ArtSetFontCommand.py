from Shared.Command.Command import Command
from Classes.Lab_4.customArt import CustomArt


class ArtSetFontCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: CustomArt, font: str):
        self.__executor = executor
        self.__font = font

    def execute(self) -> None:
        self.__executor.font = self.__font
