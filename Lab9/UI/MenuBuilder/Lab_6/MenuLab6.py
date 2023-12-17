"""
Module defining the MenuLab6 class, which represents the menu for Lab 6 operations.
"""


from Classes.Lab_6 import *
from Shared.BuilderMenu.BuilderMenu import BuilderMenu


class MenuLab6(BuilderMenu):
    """
    Class representing the menu for Lab 6 operations.
    Inherits from BuilderMenu.
    """

    def __init__(self):
        """
        Initialize the MenuLab6 instance with necessary components.
        """
        super().__init__()
        self.__text_calculator = TestCalculator()

    def _configure_package_name(self):
        """
        Configure the package name for Lab 6.
        """
        self._package_name = 'Lab_6'

    def run_menu(self):
        """
        Run the Lab 6 menu by executing the TestCalculator.
        """
        self.__text_calculator.run()
