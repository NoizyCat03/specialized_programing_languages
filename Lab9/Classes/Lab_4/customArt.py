from Classes.Lab_3.art_generator import ArtGenerator
from Classes.Lab_4.fonts import fonts


class CustomArt(ArtGenerator):
    """CustomArt class extends ArtGenerator to create customized ASCII art."""

    def __init__(self, **kwargs):
        """
        Initialize the CustomArt instance.

        :param kwargs: Additional keyword arguments.
        """
        # Initialize the CustomArt with default font 'standard'
        super().__init__(**kwargs)
        self._font = 'standard'

    def _custom_justify(self):
        """
        Apply custom justification based on the specified 'justify' parameter.

        :return: Justified message.
        :rtype: str
        """
        message = self.message
        if self.justify == 'center':
            message = message.rjust(20, ' ')
        elif self.justify == 'right':
            message = message.rjust(40)
        elif self.justify == 'left':
            message = message.ljust(0, ' ')
        return message

    def _create(self, **kwargs):
        """
        Create custom ASCII art using the specified font and justification.

        :param kwargs: Additional keyword arguments.
        :return: Generated ASCII art.
        :rtype: str
        """
        if 'font' in kwargs:
            font = kwargs['font']
        else:
            font = self._font
        # Get the font definition from the 'fonts' module
        font = fonts.get(font)
        self._direction_message = self._custom_justify()
        art = []
        max_lines = max(len(font.get(letter, '').split('\n')) for letter in self._direction_message)

        output = self.generate_art(max_lines, font, art)
        return output

    def generate_art(self, max_lines, font, art):
        """
        Generate ASCII art based on font, justification, and message.

        :param max_lines: Maximum lines in the ASCII art.
        :type max_lines: int
        :param font: Font definition.
        :type font: dict
        :param art: List to store ASCII art lines.
        :type art: list
        :return: Generated ASCII art.
        :rtype: str
        """
        for line_num in range(max_lines):
            line = ""
            # Iterate through each letter in the message
            for letter in self._direction_message:
                letter_lines = font.get(letter, '').split('\n')
                # Check if the current line number is within the range of the letter lines
                if line_num < len(letter_lines):
                    # Apply justification based on the specified 'justify' parameter
                    if self.justify == 'left':
                        line += letter_lines[line_num].ljust(len(letter_lines[0]) + 1)
                    elif self.justify == 'center':
                        line += letter_lines[line_num].center(len(letter_lines[0]) + 1)
                    elif self.justify == 'right':
                        line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
                    else:
                        line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
                else:
                    # If the line number is outside the range, add spaces
                    line += ' ' * (len(letter_lines[0]) + 1)
            # Add the line to the art
            art.append(line)
        # Join the lines to form the final output
        output = '\n'.join(art)
        return output
