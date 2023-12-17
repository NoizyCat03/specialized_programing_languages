from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetSiteCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, site: str):
        self.__executor = executor
        self.__site = site

    def execute(self) -> None:
        self.__executor.site = self.__site
