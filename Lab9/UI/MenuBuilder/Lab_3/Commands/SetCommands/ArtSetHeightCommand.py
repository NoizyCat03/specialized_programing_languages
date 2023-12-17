

from Shared.Command.Command import Command
from Classes.Lab_3.art_generator import ArtGenerator


class ArtSetHeightCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: ArtGenerator, height: str):
        self.__executor = executor
        self.__height = height

    def execute(self) -> None:
        self.__executor.height = self.__height
