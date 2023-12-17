"""
Module defining the MenuLab2 class, which represents the menu for Lab 2 operations.
"""

from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from Shared.Console.Input import InputValue, InputFloatNumberCommand, InputIntNumberCommand, InputTextCommand
from Classes.Lab_2 import *
from UI.MenuBuilder.Lab_2.Commands import *


class MenuLab2(BuilderMenu):
    """
    Class representing the menu for Lab 2 operations.
    Inherits from BuilderMenu.
    """

    def __init__(self):
        """
        Initialize the MenuLab2 instance with necessary components.
        """
        super().__init__()
        self._config = self._config["lab_2"]
        self.__calculator = BaseCalculator()
        self.__num_1 = InputValue(message=self._config["num_1"])
        self.__num_2 = InputValue(message=self._config["num_2"])
        self.__operator = InputValue(message=self._config["operator"])
        self.__custom_round = InputValue(message=self._config["custom_round"])

    def configure_input_subsystem(self):
        """
        Configure the input subsystem of the menu.
        """
        self._menu_builder.instant_command(InputFloatNumberCommand(self.__num_1))
        self._menu_builder.instant_command(InputFloatNumberCommand(self.__num_2))
        self._menu_builder.instant_command(InputTextCommand(self.__operator))
        self._menu_builder.instant_command(InputIntNumberCommand(self.__custom_round))

    def _configure_package_name(self):
        """
        Configure the package name for Lab 2.
        """
        self._package_name = 'Lab_2'

    def configure_calculator_subsystem(self):
        """
        Configure the calculator subsystem of the menu.
        """
        self._menu_builder.instant_command(SetNum1Command(self.__calculator, self.__num_1.value))
        self._menu_builder.instant_command(SetNum2Command(self.__calculator, self.__num_2.value))
        self._menu_builder.instant_command(SetOperatorCommand(self.__calculator, self.__operator.value))
        self._menu_builder.instant_command(SetCustomRoundCommand(self.__calculator, self.__custom_round.value))

    def configure_calculation_subsystem(self):
        """
        Configure the calculation subsystem of the menu.

        Handle exceptions for division by zero or arithmetic errors.
        """
        try:
            self._menu_builder.instant_command(CalcCommand(self.__calculator))
        except (ZeroDivisionError, ArithmeticError) as e:
            self._result = self._config["variables"]["Error"] + e.__str__()

    def _convert_obj_to_result_subsystem(self):
        """
        Convert the calculator object to result string.
        """
        self._result = self.__calculator.__str__()

    def _configure_lab_subsystem(self):
        """
        Configure the Lab subsystem of the menu.
        """
        self.configure_input_subsystem()
        self.configure_calculator_subsystem()
        self.configure_calculation_subsystem()
