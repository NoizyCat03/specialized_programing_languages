from Shared.Command.Command import Command
from Classes.Lab_4.customArt import CustomArt


class ArtSetJustifyCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: CustomArt, justify: str):
        self.__executor = executor
        self.__justify = justify

    def execute(self) -> None:
        self.__executor.justify = self.__justify
