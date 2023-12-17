from Shared.Command.Command import Command
from Classes.Lab_4.customArt import CustomArt


class ArtSetMessageCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: CustomArt, message: str):
        self.__executor = executor
        self.__message = message

    def execute(self) -> None:
        self.__executor.message = self.__message
