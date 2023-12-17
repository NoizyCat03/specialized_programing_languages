"""
Module defining the MenuLab1 class, which represents the menu for Lab 1 operations.
"""

from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from Shared.Console.Input import InputValue, InputFloatNumberCommand, InputIntNumberCommand, InputTextCommand
from Classes.Lab_2 import *
from UI.MenuBuilder.Lab_1.Commands import *


class MenuLab1(BuilderMenu):
    """
    Class representing the menu for Lab 1 operations.
    Inherits from BuilderMenu.
    """

    def __init__(self):
        """
        Initialize the MenuLab1 instance with necessary components.
        """
        super().__init__()
        self.__calculator = BaseCalculator()
        self.__num_1 = InputValue(message='Input number 1')
        self.__num_2 = InputValue(message='Input number 2')
        self.__operator = InputValue(message='Input operator')
        self.__custom_round = InputValue(message='Input custom_round')

    def _configure_input_subsystem(self):
        """
        Configure the input subsystem of the menu.
        """
        self._menu_builder.add_command(InputFloatNumberCommand(self.__num_1))
        self._menu_builder.add_command(InputFloatNumberCommand(self.__num_2))
        self._menu_builder.add_command(InputTextCommand(self.__operator))
        self._menu_builder.add_command(InputIntNumberCommand(self.__custom_round))
        self._menu_builder.run()

    def _configure_calculator_subsystem(self):
        """
        Configure the calculator subsystem of the menu.
        """
        self._menu_builder.add_command(SetNum1Command(self.__calculator, self.__num_1.value))
        self._menu_builder.add_command(SetNum2Command(self.__calculator, self.__num_2.value))
        self._menu_builder.add_command(SetOperatorCommand(self.__calculator, self.__operator.value))
        self._menu_builder.add_command(SetCustomRoundCommand(self.__calculator, self.__custom_round.value))
        self._menu_builder.run()

    def _configure_calculation_subsystem(self):
        """
        Configure the calculation subsystem of the menu.
        """
        self._menu_builder.add_command(CalcCommand(self.__calculator))
        self._menu_builder.run()

    def _convert_obj_to_result_subsystem(self):
        """
        Convert the calculator object to result string.
        """
        self._result = self.__calculator.__str__()

    def _configure_lab_subsystem(self):
        """
        Configure the Lab subsystem of the menu.
        """
        self._configure_input_subsystem()
        self._configure_calculator_subsystem()
        self._configure_calculation_subsystem()
