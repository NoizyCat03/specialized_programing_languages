"""
Module defining the Parallelepiped class, which is a subclass of Figure.
"""

from Classes.Lab_5.figure import Figure
from Classes.Lab_5.symbols import SYMBOLS


class Parallelepiped(Figure):
    """
    A class representing a Parallelepiped, a 3D geometric figure.
    Inherits from the Figure class.
    """

    def build_up_2d_line(self, color_1, color_2, symbol_1, symbol_2):
        """
        Build a 2D line with alternating colors and symbols.

        :param color_1: Color for the first symbol.
        :param color_2: Color for the second symbol.
        :param symbol_1: First symbol in the line.
        :param symbol_2: Second symbol in the line.
        :return: A string representing the 2D line.
        """
        line = ''
        for size_x in range(self._size_x + 1):
            if size_x == 0 or size_x == self._size_x:
                line += self.color_line(self, color_1, symbol_1)
            else:
                line += self.color_line(self, color_2, symbol_2)
        return line

    def build_up_2d(self, lines, symbol, space_color):
        """
        Build a 2D representation with alternating symbols and colors.

        :param lines: List of lines to build upon.
        :param symbol: Symbol to use in the representation.
        :param space_color: Color for spaces in the representation.
        :return: A list of lines representing the 2D figure.
        """
        for index in range(len(lines)):
            if index == 0:
                color_1 = self._symbol_color
                color_2 = self._symbol_color
                symbol_1 = SYMBOLS.get('corner')
                symbol_2 = SYMBOLS.get('horizontal')
            else:
                color_1 = self._symbol_color
                color_2 = space_color
                symbol_1 = symbol
                symbol_2 = SYMBOLS.get('space')
            line = self.build_up_2d_line(color_1, color_2, symbol_1, symbol_2)
            lines[index] = lines[index] + line
        return lines

    def build_3d(self, lines):
        """
        Build the 3D representation of the Parallelepiped.

        :param lines: List of lines representing the 2D figure.
        :return: A list of lines representing the 3D figure.
        """
        inclined_count = 1
        for index in range(len(lines)):
            line = ''
            mx = (len(lines[0]))
            shadow_mx = mx + self._size_x
            shadow = ''
            if index != 0 and index != len(lines) - 1:
                count = mx - len(lines[index]) - 1
                if index < self._size_y:
                    symbol = SYMBOLS.get('vertical')
                elif index == self.size_y:
                    symbol = SYMBOLS.get('corner')
                else:
                    count -= inclined_count
                    shadow_count = shadow_mx - len(lines[index]) - 1
                    shadow = self.build_symbol(SYMBOLS.get('space'), shadow_count, self._shadow_color)
                    symbol = SYMBOLS.get('inclined')
                    inclined_count += 1
                line = self.build_symbol(SYMBOLS.get('space'), count, self._color_1)
                line += self.color_line(self, self._symbol_color, symbol)
                line += self.color_line(self, self._symbol_color, shadow)
            lines[index] += line
        return lines

    def create_2d(self):
        """
        Create the 2D representation of the Parallelepiped.

        :return: A list of lines representing the 2D figure.
        """
        shadow_down_lines = self.build_2d_shadow(self, self._size_y, SYMBOLS.get('nothing'), self._size_z)
        down_2d = self.build_up_2d(shadow_down_lines, SYMBOLS.get('vertical'), self._color_2)
        down_2d += [down_2d[0]]
        return down_2d

    def build_2d(self):
        """
        Build the 2D representation of the Parallelepiped.

        Sets the scaling and creates the 2D figure.
        """
        self.set_scaling()
        figure_2d = self.create_2d()
        self._result = self.convert(figure_2d)

    def build(self):
        """
        Build the 3D representation of the Parallelepiped.

        Sets the scaling, creates the 2D figure, and builds the 3D figure.
        """
        self.set_scaling()
        shadow_up_lines = self.build_2d_shadow(self, self._size_z, SYMBOLS.get('space'), self._size_z)
        up_2d = self.build_up_2d(shadow_up_lines, SYMBOLS.get('inclined'), self._color_3)

        down_2d = self.create_2d()

        lines = up_2d + down_2d
        result = self.build_3d(lines)
        self._result = self.convert(result)
