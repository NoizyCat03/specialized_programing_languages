from Shared.Command.Command import Command
from Classes.Lab_4.customArt import CustomArt


class ArtCustomFontCommand(Command):
    """
    Command can implement custom art .
    """

    def __init__(self, executor: CustomArt):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.custom_font()
