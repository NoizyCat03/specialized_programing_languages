"""
Module defining the StylizeSymbol class for generating stylized symbols.
"""

from Shared.Constants.colors import COLORS


class StylizeSymbol:
    """
    Class for generating stylized symbols with color and font attributes.
    """

    def __init__(self, **kwargs):
        """
        Constructor for the StylizeSymbol class.

        Args:
            line (str): The symbol or line to be stylized.
            color (str): The color of the stylized symbol.
            font (str): The font of the stylized symbol.
        """
        self.__line = kwargs['line'] if 'line' in kwargs else ''
        self.__color = kwargs['color'] if 'color' in kwargs else COLORS.get('RESET')
        self.__font = kwargs['font'] if 'font' in kwargs else ''
        self.__result = ''

    def generate_custom_line(self):
        """
        Generate a custom stylized line based on the provided attributes.
        """
        self.__result = self.__color + self.__font + self.__line + COLORS.get('RESET')

    def __str__(self):
        """
        Get the string representation of the stylized symbol.

        Returns:
            str: The string representation of the stylized symbol.
        """
        return self.__result

    # GET result
    @property
    def result(self):
        """
        Get the result attribute.

        Returns:
            str: The result attribute.
        """
        return self.__result

    # GETTER/SETTER line
    @property
    def line(self):
        """
        Get the line attribute.

        Returns:
            str: The line attribute.
        """
        return self.__line

    @line.setter
    def line(self, line):
        """
        Set the line attribute.

        Args:
            line (str): The new value for the line attribute.
        """
        self.__line = line

    # GETTER/SETTER color
    @property
    def color(self):
        """
        Get the color attribute.

        Returns:
            str: The color attribute.
        """
        return self.__color

    @color.setter
    def color(self, color):
        """
        Set the color attribute.

        Args:
            color (str): The new value for the color attribute.
        """
        self.__color = color

    # GETTER/SETTER line
    @property
    def font(self):
        """
        Get the font attribute.

        Returns:
            str: The font attribute.
        """
        return self.__font

    @font.setter
    def font(self, font):
        """
        Set the font attribute.

        Args:
            font (str): The new value for the font attribute.
        """
        self.__font = font
