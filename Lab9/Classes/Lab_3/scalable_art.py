"""
Module docstring describing the purpose of the module.
"""


class ScalableArt:
    """
    Class docstring describing the purpose of the class.
    """

    def __init__(self, art: str, height: int, width: int):
        """
        Initialize the ScaLableArt with the provided art, height, and width.
        """
        self._art = art
        self._update_height = height
        self._update_width = width

    def generate_zoom_art(self) -> str:
        """
        Generate scaled ASCII art based on the provided height and width.
        """
        lines = self.__generate_art_list(self._art)
        len_base_art = len(lines)
        len_base_art_line = len(max(lines, key=len))
        scale = self.__get_scale(self._update_height, self._update_width,
                                 len_base_art, len_base_art_line)
        new_art_list = self.__get_new_art_list(lines, scale)
        art = self.__convert_list_to_art(new_art_list)
        return art

    @staticmethod
    def __generate_art_list(art: str) -> list:
        """
        Convert the ASCII art string into a list of lines.
        """
        line = ''
        lines = []
        for char in art:
            if char != '\n':
                line += char
            else:
                lines.append(line)
                line = ''
        return lines

    @staticmethod
    def __get_scale(base_height: int, base_width: int,
                    update_height: int, update_width: int) -> int:
        """
        Calculate the scaling factor based on the provided dimensions.
        """
        square_base = base_height * base_width
        square_update = update_height * update_width
        scale = round(max(square_base, square_update) / min(square_base, square_update))
        return scale

    @staticmethod
    def __convert_list_to_art(line_list: list) -> str:
        """
        Convert a list of lines back into a single string with line breaks.
        """
        result = ''
        for line in line_list:
            result += line + '\n'
        return result

    @staticmethod
    def __get_new_art_list(lines: list, scale: int) -> list:
        """
        Scale each line in the ASCII art list.
        """
        result = []
        for line in lines:
            new_line = ''
            for char in line:
                new_line += char * scale
            result.extend([new_line] * scale)
        return result

    def __str__(self):
        return self._art
