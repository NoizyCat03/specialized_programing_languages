"""
Module defining the Pyramid class, which is a subclass of Figure.
"""

from Classes.Lab_5.figure import Figure
from Classes.Lab_5.symbols import SYMBOLS


class Pyramid(Figure):
    """
    A class representing a Pyramid, a 3D geometric figure.
    Inherits from the Figure class.
    """

    def set_length_x(self):
        """
        Set the length of the base of the pyramid along the x-axis.
        """
        self._length_x = self._size_x + self._size_y

    def set_length_y(self):
        """
        Set the length of the base of the pyramid along the y-axis.
        """
        self._length_y = self._size_z

    @staticmethod
    def build_up_2d_line(self, color_1, color_2, symbol_1, symbol_2, count):
        """
        Build a 2D line with alternating colors and symbols.

        :param self:
        :param color_1: Color for the first symbol.
        :param color_2: Color for the second symbol.
        :param symbol_1: First symbol in the line.
        :param symbol_2: Second symbol in the line.
        :param count: Number of symbols to build in the line.
        :return: A string representing the 2D line.
        """
        line = ''
        for size_x in range(count):
            if size_x == 0:
                line += self.color_line(self, color_1, symbol_1)
            else:
                line += self.color_line(self, color_2, symbol_2)
        return line

    @staticmethod
    def build_up_2d(self, lines, symbol, space_color):
        """
        Build a 2D representation with alternating symbols and colors.

        :param self:
        :param lines: List of lines to build upon.
        :param symbol: Symbol to use in the representation.
        :param space_color: Color for spaces in the representation.
        :return: A list of lines representing the 2D figure.
        """
        mx = len(lines[0])
        for index in range(len(lines)):
            if index == 0:
                color_1 = self._symbol_color
                color_2 = ''
                symbol_1 = self.SYMBOLS.get('corner')
                symbol_2 = ''
                count = 1
            else:
                color_1 = self._symbol_color
                color_2 = space_color
                symbol_1 = symbol
                symbol_2 = self.SYMBOLS.get('space')
                count = mx - len(lines[index])

            line = self.build_up_2d_line(self, color_1, color_2, symbol_1, symbol_2, count)

            lines[index] = lines[index] + line
        return lines

    @staticmethod
    def build_3d(self, lines):
        """
        Build the 3D representation of the Pyramid.

        :param self:
        :param lines: List of lines representing the 2D figure.
        :return: A list of lines representing the 3D figure.
        """
        inclined_count = 0
        mx = 0
        count = 0
        for index in range(len(lines)):
            line = ''
            shadow_mx = mx + self._size_x
            shadow = ''
            if index != 0 and index != len(lines) - 1:
                if index < self._size_y:
                    count = index - 1
                    symbol = '\\'
                elif index == self._size_y:
                    mx = count
                    count = 0
                    symbol = self.SYMBOLS.get('nothing')
                else:
                    count = mx - inclined_count
                    shadow_count = shadow_mx - len(lines[index]) - 1
                    shadow = self.build_symbol(self.SYMBOLS.get('space'), shadow_count, self._shadow_color)
                    symbol = self.SYMBOLS.get('inclined')
                    inclined_count += 1
                line = self.build_symbol(self.SYMBOLS.get('space'), count, self._color_2)
                line += self.color_line(self, self._symbol_color, symbol)
                line += self.color_line(self, self._symbol_color, shadow)
            lines[index] += line
        return lines

    def build_footer(self):
        """
        Build the footer line for the Pyramid.

        :return: A string representing the footer line.
        """
        line = ''
        for index in range(self._size_y * 2 + 1):
            if index == 0 or index == (self._size_y * 2):
                symbol = '+'
            elif index == self._size_y:
                symbol = '|'
            else:
                symbol = ' '
            line += self.color_line(self, self._symbol_color, symbol)
        return line

    def build(self):
        """
        Build the 3D representation of the Pyramid.

        Sets the scaling, creates the 2D figure, and builds the 3D figure.
        """
        self.set_scaling()
        shadow_up_lines = self.build_2d_shadow(self, self._size_y, SYMBOLS.get('space'), self._size_y)
        first_list = self.build_up_2d(self, shadow_up_lines, SYMBOLS.get('inclined'), self._color_1)
        for index in range(len(first_list)):
            if index != 0:
                line = self.color_line(self, self._default_color, SYMBOLS.get('vertical'))
            else:
                line = ''
            first_list[index] += line

        second_list = [s.replace('/', '\\') for s in first_list]
        second_list += [self.build_footer()]

        second_list = list(reversed(second_list))
        lst = first_list + second_list
        result = self.build_3d(self, lst)
        self._result = self.convert(result)
