from Shared.Command.Command import Command
from Classes.Lab_3.art_generator import ArtGenerator


class ArtSetJustifyCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: ArtGenerator, justify: str):
        self.__executor = executor
        self.__justify = justify

    def execute(self) -> None:
        self.__executor.justify = self.__justify
