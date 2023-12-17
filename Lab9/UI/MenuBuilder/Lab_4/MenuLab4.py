"""
Module defining the MenuLab4 class, which represents the menu for Lab 4 operations.
"""

from Classes.Lab_4 import *
from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from UI.MenuBuilder.Lab_4.Commands import *
from Shared.Console.Input import InputValue, InputTextCommand, SelectObjectWithDictCommand, SetInputMessageCommand, \
    InputIntNumberCommand, InputBoolCommand
from Shared.Constants import COLORS, FONTS_TYPE, JUSTIFIES
from Shared.StylizeSymbol import SetColorCommand


class MenuLab4(BuilderMenu):
    """
    Class representing the menu for Lab 4 operations.
    Inherits from BuilderMenu.
    """

    def __init__(self):
        """
        Initialize the MenuLab4 instance with necessary components.
        """
        super().__init__()
        self._config = self._config["lab_4"]
        self._ascii_art = CustomArt()
        self._message = InputValue(message=self._config["message"])
        self._height = InputValue(message=self._config["height"])
        self._width = InputValue(message=self._config["width"])
        self._justify = InputValue(message=self._config["direction"])
        self._font = InputValue(message=self._config["font"])
        self._color = InputValue(message=self._config["color"])
        self._symbol = InputValue(message=self._config["symbol"])
        self._subsystem_status = InputValue(message=self._config["scaling_status"])
        self._font_type = InputValue(message=self._config["font_type"])

    def _configure_package_name(self):
        """
        Configure the package name for Lab 4.
        """
        self._package_name = 'Lab_4'

    def _configure_lab_subsystem(self):
        """
        Configure the Lab subsystem of the menu.
        """
        self._configure_message_subsystem()
        self._configure_justify_subsystem()
        self._configure_font_subsystem()
        self._configure_scaling_subsystem()
        self._configure_color_subsystem()

    def _convert_obj_to_result_subsystem(self):
        """
        Convert the ASCII art object to result string.
        """
        self._result = self._ascii_art.__str__()

    def _configure_message_subsystem(self):
        """
        Configure the message subsystem of the menu.
        """
        self._menu_builder.instant_command(InputTextCommand(self._message))
        self._menu_builder.instant_command(ArtSetMessageCommand(self._ascii_art, self._message.value))

    def _configure_justify_subsystem(self):
        """
        Configure the justify subsystem of the menu.
        """
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self._justify, JUSTIFIES))
        self._menu_builder.instant_command(ArtSetJustifyCommand(self._ascii_art, self._justify.value))

    def _configure_font_subsystem(self):
        """
        Configure the font subsystem of the menu.
        """
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self._font_type, FONTS_TYPE))
        if self._font_type.value == 'Base Fonts':
            self._configure_base_font_subsystem()
        elif self._font_type.value == 'Custom font':
            self._configure_custom_font_subsystem()
        else:
            self._menu_builder.instant_command((ArtCreateCommand(self._ascii_art)))

    def _configure_base_font_subsystem(self):
        """
        Configure the base font subsystem of the menu.
        """
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self._font, FONTS))
        self._menu_builder.instant_command(ArtSetFontCommand(self._ascii_art, self._font.value))
        self._menu_builder.instant_command((ArtCreateCommand(self._ascii_art)))

    def _configure_custom_font_subsystem(self):
        """
        Configure the custom font subsystem of the menu.
        """
        self._menu_builder.instant_command(InputTextCommand(self._symbol))
        self._menu_builder.instant_command(ArtSetSymbolCommand(self._ascii_art, self._symbol.value))
        self._menu_builder.instant_command(ArtCustomFontCommand(self._ascii_art))

    def _configure_color_subsystem(self):
        """
        Configure the color subsystem of the menu.
        """
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self._color, COLORS))
        self._menu_builder.instant_command(SetColorCommand(self._stylize_symbols, self._color.value))

    def _configure_check_subsystem(self):
        """
        Configure the check subsystem of the menu.
        """
        self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
                                                                  "Do you want to set scaling(1/0:)"))
        self._menu_builder.instant_command(InputBoolCommand(self._subsystem_status))

    def _configure_scaling_subsystem(self):
        """
        Configure the scaling subsystem of the menu.
        """
        self._configure_check_subsystem()
        if self._subsystem_status.value:
            self._menu_builder.instant_command(InputIntNumberCommand(self._width))
            self._menu_builder.instant_command(InputIntNumberCommand(self._height))
            self._menu_builder.instant_command((ArtSetWidthCommand(self._ascii_art, self._width.value)))
            self._menu_builder.instant_command((ArtSetHeightCommand(self._ascii_art, self._height.value)))
            self._menu_builder.instant_command(ArtScalingCommand(self._ascii_art))
