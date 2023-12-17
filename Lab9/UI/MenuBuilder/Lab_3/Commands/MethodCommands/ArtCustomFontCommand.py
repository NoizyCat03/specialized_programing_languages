from Shared.Command.Command import Command
from Classes.Lab_3.art_generator import ArtGenerator


class ArtCustomFontCommand(Command):
    """
    Command can implement custom art .
    """

    def __init__(self, executor: ArtGenerator):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.custom_font()
