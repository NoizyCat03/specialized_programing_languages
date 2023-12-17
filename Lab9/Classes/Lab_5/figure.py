from Shared.Constants.colors import COLORS
from Classes.Lab_5.symbols import SYMBOLS


class Figure:

    def __init__(self, **kwargs):
        self._length_x = 0
        self._length_y = 0

        if 'size_x' in kwargs:
            self._size_x = kwargs['size_x']

            if 'size_y' in kwargs and 'size_z' in kwargs:
                self._size_y = kwargs['size_y']
                self._size_z = kwargs['size_z']
                self._size_z = kwargs['size_z']
            else:
                self._size_y = self._size_z = self._size_x

        else:
            self._size_y = self._size_z = self._size_x = 1

        self._result = ''
        self._color_1 = COLORS.get('RED')
        self._color_2 = COLORS.get('GREEN')
        self._color_3 = COLORS.get('YELLOW')

        self._default_color = COLORS.get('RESET')
        self._shadow_color = COLORS.get('WHITE')
        self._symbol_color = COLORS.get('BLACK')

        self._space = 0
        self._scaling = 1

    @classmethod
    def _number_validate(cls, num):
        if num > 0:
            return num
        else:
            raise ValueError(f"Parameter '{num}' must be greater than zero")

    @property
    def result(self):
        return self._result

    @property
    def size_z(self):
        return self._size_z

    @size_z.setter
    def size_z(self, value):
        self._size_z = self._number_validate(value)

    @property
    def scaling(self):
        return self._scaling

    @scaling.setter
    def scaling(self, value):
        self._scaling = self._number_validate(value)

    @property
    def size_y(self):
        return self._size_y

    @size_y.setter
    def size_y(self, value):
        self._size_y = self._number_validate(value)

    @property
    def size_x(self):
        return self._size_x

    @size_x.setter
    def size_x(self, value):
        self._size_x = self._number_validate(value)

    @property
    def color_3(self):
        return self._color_3

    @color_3.setter
    def color_3(self, value):
        self._color_3 = value

    @property
    def shadow_color(self):
        return self._shadow_color

    @shadow_color.setter
    def shadow_color(self, value):
        self._shadow_color = value

    @property
    def symbol_color(self):
        return self._symbol_color

    @symbol_color.setter
    def symbol_color(self, value):
        self._symbol_color = value

    @property
    def color_1(self):
        return self._color_1

    @color_1.setter
    def color_1(self, value):
        self._color_1 = value

    @property
    def color_2(self):
        return self._color_2

    @color_2.setter
    def color_2(self, value):
        self._color_2 = value

    def set_length_x(self):
        self._length_x = self._length_x

    def set_length_y(self):
        self._length_y = self._length_y

    def set_scaling(self):
        self.size_x *= self._scaling
        self.size_y *= self._scaling
        self.size_z *= self._scaling

    @staticmethod
    def color_line(self, color, line):
        return color + line + self._default_color

    @staticmethod
    def build_2d_shadow(self, count, symbol, size):
        lines = []
        for index in range(count):
            line = self.build_symbol(SYMBOLS.get('space'), self._space, self._default_color)
            line += self.color_line(self, self._default_color, symbol * (size - index))
            lines += [line]
        return lines

    def build_symbol(self, symbol, count, color):
        line = ''
        for i in range(count):
            line += self.color_line(self, color, symbol)
        return line

    def build_2d(self):
        pass

    def build(self):
        pass

    @staticmethod
    def remove_color_codes(text):
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text

    @staticmethod
    def convert(lines):
        result = ''
        for line in lines:
            result += line + '\n'
        return result

    def __str__(self):
        return self._result
