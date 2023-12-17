from Shared.Command.Command import Command
from Classes.Lab_4.customArt import CustomArt


class ArtSetWidthCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: CustomArt, width: str):
        self.__executor = executor
        self.__width = width

    def execute(self) -> None:
        self.__executor.width = self.__width


