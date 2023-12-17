

from Shared.Command.Command import Command
from Classes.Lab_3.art_generator import ArtGenerator


class ArtSetFontCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: ArtGenerator, font: str):
        self.__executor = executor
        self.__font = font

    def execute(self) -> None:
        self.__executor.font = self.__font
