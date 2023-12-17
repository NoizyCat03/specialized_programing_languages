"""
Module defining the BuilderMenu class for configuring and executing a menu with subsystems.
"""

import json

from Shared.Command.ComplexCommand import ComplexCommand
from Shared.Console.Input import InputValue, InputBoolCommand, SetInputMessageCommand, InputTextCommand
from Shared.Save.Classes.DataSaver import DataSaver
from Shared.StylizeSymbol import StylizeSymbol, SetMessageCommand, GenerateCustomLineCommand
from Shared.Console.Print import ConsolePrint, SetOutputCommand, PrintCommand
from Shared.Save.Commands.MethodCommands.SaveTxtCommand import SaveTxtCommand


class BuilderMenu:
    """
    BuilderMenu class for configuring and executing a menu with subsystems.
    """

    def __init__(self):
        """
        Constructor for the BuilderMenu class.
        """
        with open('config.json', 'r') as config_file:
            self._config = json.load(config_file)
            self._config = self._config["variables"]
        self._result = ''
        self._stylize_symbols = StylizeSymbol()
        self._package_name = ''
        self._save = DataSaver()
        self._filename = InputValue(message="Input the filename: ")
        self._output = ConsolePrint()
        self._menu_builder = ComplexCommand()
        self._subsystem_status = InputValue()
        self._save_status = InputValue()

    def _configure_lab_subsystem(self):
        """
        Configure the lab subsystem. (Needs implementation)
        """
        pass

    def _configure_package_name(self):
        """
        Configure the package name. (Needs implementation)
        """
        pass

    def _configure_save_subsystem(self):
        """
        Configure the save subsystem based on user input.
        """
        self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
                                                                  "Do you want to save (1/0:)"))
        self._configure_check_subsystem()
        if self._subsystem_status.value:
            self._configure_package_name()
            self._menu_builder.instant_command(InputTextCommand(self._filename))
            self._save.file_name = self._filename.value
            self._save._Lab = self._package_name
            self._menu_builder.instant_command(SaveTxtCommand(self._save, self._result))

    def _convert_obj_to_result_subsystem(self):
        """
        Convert an object to the result subsystem. (Needs implementation)
        """
        pass

    def _configure_output_subsystem(self):
        """
        Configure the output subsystem with messages and symbols.
        """
        self._menu_builder.instant_command(SetMessageCommand(self._stylize_symbols, self._result))
        self._menu_builder.instant_command((GenerateCustomLineCommand(self._stylize_symbols)))
        self._menu_builder.instant_command(SetOutputCommand(self._output, self._stylize_symbols))
        self._menu_builder.instant_command(PrintCommand(self._output))

    def _configure_check_subsystem(self):
        """
        Configure the check subsystem to get a boolean value from user input.
        """
        self._menu_builder.instant_command(InputBoolCommand(self._subsystem_status))

    def run_menu(self):
        """
        Run the configured menu.
        """
        try:
            self._configure_lab_subsystem()
            self._convert_obj_to_result_subsystem()
        except ValueError as e:
            self._result = "Error: " + e.__str__()

        self._configure_output_subsystem()
        try:
            self._configure_save_subsystem()
        except BaseException as e:
            self._result = e.__str__()

# Example usage
# menu = BuilderMenu()
# menu.run_menu()
