"""
Module defining the MenuLab7 class, which represents the menu for Lab 7 operations.
"""

from Classes.Lab_7 import *
from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from UI.MenuBuilder.Lab_7.Commands import *
from Shared.Console.Input import (InputValue, InputTextCommand, SelectObjectWithDictCommand, SetInputMessageCommand)
from Shared.Constants import COLORS, FONTS


class MenuLab7(BuilderMenu):
    """
    Class representing the menu for Lab 7 operations.
    Inherits from BuilderMenu.
    """

    def __init__(self):
        """
        Initialize the MenuLab7 instance with necessary components.
        """
        super().__init__()
        self._config = self._config["lab_7"]
        self.__request = RequestsAPI()
        self.__data_type = InputValue(message=self._config["data"]["type"])
        self.__custom_data = InputValue(message=self._config["data"]["custom"])
        self.__site = InputValue(message=self._config["site"])
        self.__color = InputValue(message=self._config["color"])
        self.__font = InputValue(message=self._config["font"])

    def _configure_package_name(self):
        """
        Configure the package name for Lab 7.
        """
        self._package_name = 'Lab_7'

    def _configure_lab_subsystem(self):
        """
        Configure the subsystems for Lab 7 menu.
        """
        self.__configure_request_subsystem()
        self.__configure_header_color_subsystem()
        self.__configure_header_font_subsystem()
        self.__configure_build_request_subsystem()

    def __configure_request_subsystem(self):
        """
        Configure the request subsystem for Lab 7 menu.
        """
        self._menu_builder.instant_command(InputTextCommand(self.__site))
        self._menu_builder.instant_command(SetSiteCommand(self.__request, self.__site.value))

    def _convert_obj_to_result_subsystem(self):
        """
        Convert the result subsystem to a string.
        """
        self._result = self.__request.__str__()

    def __configure_header_color_subsystem(self):
        """
        Configure the header color subsystem for Lab 7 menu.
        """
        self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
                                                                  self._config['header_color']))
        self._configure_check_subsystem()  # color
        if self._subsystem_status.value:
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__color, COLORS))
            self._menu_builder.instant_command(SetColorCommand(self.__request, self.__color.value))

    def __configure_header_font_subsystem(self):
        """
        Configure the header font subsystem for Lab 7 menu.
        """
        self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
                                                                  self._config['header_font']))
        self._configure_check_subsystem()  # font
        if self._subsystem_status.value:
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__font, FONTS))
            self._menu_builder.instant_command(SetFontCommand(self.__request, self.__font.value))

    def __configure_build_request_subsystem(self):
        """
        Configure the build request subsystem for Lab 7 menu.
        """
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__data_type, DATA_TYPE))
        if self.__data_type.value == self._config['list']:
            self._menu_builder.instant_command(BuildListCommand(self.__request))
        else:
            self._menu_builder.instant_command(BuildTableCommand(self.__request))
