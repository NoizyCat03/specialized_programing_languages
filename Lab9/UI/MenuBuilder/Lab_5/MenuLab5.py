"""
Module defining the MenuLab5 class, which represents the menu for Lab 5 operations.
"""

from Classes.Lab_5 import *
from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from UI.MenuBuilder.Lab_5.Commands import *
from Shared.Console.Input import (InputValue, SelectObjectWithDictCommand,
                                  SetInputMessageCommand, InputIntNumberCommand)
from Shared.Constants import BACKGROUND_COLORS, COLORS


class MenuLab5(BuilderMenu):
    """
    Class representing the menu for Lab 5 operations.
    Inherits from BuilderMenu.
    """

    def __init__(self):
        """
        Initialize the MenuLab5 instance with necessary components.
        """
        super().__init__()
        self._config = self._config["lab_5"]
        self.__figure_type = InputValue(message=self._config["figure"]["type"])
        self.__figures_type = InputValue(message=self._config["figure"]["types"])
        self.__figure = Figure()
        self.__size_x = InputValue(message=self._config["size"]["x"])
        self.__size_y = InputValue(message=self._config["size"]["y"])
        self.__size_z = InputValue(message=self._config["size"]["z"])
        self.__color_area_1 = InputValue(message=self._config["colors"]["area_1"])
        self.__color_area_2 = InputValue(message=self._config["colors"]["area_2"])
        self.__color_area_3 = InputValue(message=self._config["colors"]["area_3"])
        self.__border_color = InputValue(message=self._config["colors"]["border"])
        self.__shadow_color = InputValue(message=self._config["colors"]["shadow"])
        self.__scaling = InputValue(message=self._config["scaling"]["value"])

    def _configure_lab_subsystem(self):
        """
        Configure the Lab subsystem of the menu.
        """
        self.__configure_figure_subsystem()
        self.__configure_area_color_subsystem()
        self.__configure_scaling_subsystem()
        self.__configure_build_figure_subsystem()

    def __configure_figure_subsystem(self):
        """
        Configure the figure subsystem of the menu.
        """
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__figure_type, FIGURES))
        self.__configure_size_subsystem()
        if self.__figure_type.value == 'Parallelepiped':
            self.__configure_parallelepiped_subsystem()
        elif self.__figure_type.value == 'Pyramid':
            self.__configure_pyramid_subsystem()

    def __configure_parallelepiped_subsystem(self):
        """
        Configure the parallelepiped subsystem of the menu.
        """
        self.__figure = Parallelepiped()
        self._menu_builder.instant_command(SetSizeXCommand(self.__figure, self.__size_x.value))
        self._menu_builder.instant_command(SetSizeYCommand(self.__figure, self.__size_y.value))
        self._menu_builder.instant_command(SetSizeZCommand(self.__figure, self.__size_z.value))

    def __configure_pyramid_subsystem(self):
        """
        Configure the pyramid subsystem of the menu.
        """
        self.__figure = Pyramid()
        self._menu_builder.instant_command(SetSizeXCommand(self.__figure, self.__size_x.value))
        self._menu_builder.instant_command(SetSizeYCommand(self.__figure, self.__size_y.value))
        self._menu_builder.instant_command(SetSizeZCommand(self.__figure, self.__size_z.value))

    def __configure_size_subsystem(self):
        """
        Configure the size subsystem of the menu.
        """
        self._menu_builder.instant_command(InputIntNumberCommand(self.__size_x))
        self._menu_builder.instant_command(InputIntNumberCommand(self.__size_y))
        self._menu_builder.instant_command(InputIntNumberCommand(self.__size_z))

    def __configure_scaling_subsystem(self):
        """
        Configure the scaling subsystem of the menu.
        """
        self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
                                                                  "Do you want to set scaling (1/0:)"))
        self._configure_check_subsystem()  # scaling
        if self._subsystem_status.value:
            self._menu_builder.instant_command((InputIntNumberCommand(self.__scaling)))
            self._menu_builder.instant_command(SetScalingCommand(self.__figure, self.__scaling.value))

    def _convert_obj_to_result_subsystem(self):
        """
        Convert the figure object to result string.
        """
        self._result = self.__figure.__str__()

    def _configure_package_name(self):
        """
        Configure the package name for Lab 5.
        """
        self._package_name = 'Lab_5'

    def __configure_area_color_subsystem(self):
        """
        Configure the area color subsystem of the menu.
        """
        self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
                                                                  "Do you want to set colors (1/0:)"))
        self._configure_check_subsystem()  # Area, Border, Shadow, color
        if self._subsystem_status.value:
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__color_area_1, BACKGROUND_COLORS))
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__color_area_2, BACKGROUND_COLORS))
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__color_area_3, BACKGROUND_COLORS))
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__border_color, COLORS))
            self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__shadow_color, BACKGROUND_COLORS))

            self._menu_builder.instant_command((SetColorArea1Command(self.__figure, self.__color_area_1.value)))
            self._menu_builder.instant_command((SetColorArea2Command(self.__figure, self.__color_area_2.value)))
            self._menu_builder.instant_command((SetColorArea3Command(self.__figure, self.__color_area_3.value)))
            self._menu_builder.instant_command((SetSymbolColorCommand(self.__figure, self.__border_color.value)))
            self._menu_builder.instant_command((SetShadowColorCommand(self.__figure, self.__shadow_color.value)))

    def __configure_build_figure_subsystem(self):
        """
        Configure the build figure subsystem of the menu.
        """
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__figures_type, FIGURES_TYPE))
        if self.__figures_type.value == '2D':
            self._menu_builder.instant_command(Build2DCommand(self.__figure))
        else:
            self._menu_builder.instant_command(Build3DCommand(self.__figure))
