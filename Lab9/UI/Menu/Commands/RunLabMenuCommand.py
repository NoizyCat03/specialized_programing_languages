from Shared.Command.Command import Command
from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from UI.Menu.program_menu import PROGRAM_MENU
from UI.MenuBuilder import Exit


class RunLabMenuCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: BuilderMenu, Lab: str):
        self.__executor = executor
        self.__Lab = Lab

    def execute(self) -> None:
        self.__executor = PROGRAM_MENU.get(self.__Lab, Exit())
        self.__executor.run_menu()
