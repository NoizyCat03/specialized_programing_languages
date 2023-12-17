"""
Module defining the MainMenu class, which represents the main menu of the application.
"""

from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from Shared.Command.ComplexCommand import ComplexCommand
from Shared.Console.Input import InputValue, SelectObjectWithDictCommand

from UI.Menu.user_out_menu import MENU
from UI.Menu.Commands import RunLabMenuCommand


class MainMenu:
    """
    Class representing the main menu of the application.
    """
    _instance = None

    def __new__(cls):
        """
        Ensure that only one instance of MainMenu is created.
        """
        if cls._instance is None:
            cls._instance = super(MainMenu, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initialize the MainMenu instance with necessary components.
        """
        self._menu = BuilderMenu()
        self._user_input = InputValue(message="Choose menu")
        self._menu_builder = ComplexCommand()
        self._proces = None

    def run_menu(self):
        """
        Run the main menu loop, allowing the user to make selections.
        """
        while True:
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self._user_input,
                                                                           MENU))
            self._menu_builder.instant_command(RunLabMenuCommand(self._menu,
                                                                 self._user_input.value))
