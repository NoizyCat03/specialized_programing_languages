"""
Module docstring describing the purpose of the module.
"""

import pyfiglet
from Classes.Lab_3.scalable_art import ScalableArt

class ArtGenerator:
    """
    Class docstring describing the purpose of the class.
    """

    def __init__(self, **kwargs):
        """
        Constructor with optional keyword arguments for initialization.
        """
        self._ascii_art = ''
        self._message = kwargs.get('message', '')
        self._height = kwargs.get('height', 1)
        self._width = kwargs.get('width', 1)
        self._justify = kwargs.get('direction', 'auto')
        self._font = kwargs.get('font', 'standard')
        self._symbol = kwargs.get('symbol', '*')

    def custom_font(self):
        """
        Replace specific characters in the art with user-defined symbols.
        """
        if self._font != 'banner3':
            self.create_art(font='banner3')
        for original_char, user_char in zip("#/", self._symbol):
            self._ascii_art = self._ascii_art.replace(original_char, user_char)

    def create_art(self, **kwargs):
        """
        Create ASCII art using pyfiglet library.
        """
        font = kwargs.get('font', self._font)
        art = pyfiglet.Figlet(font=font, justify=self._justify)
        self._ascii_art = art.renderText(self._message)

    def scaling(self):
        """
        Scale the ASCII art using the ScaLableArt class.
        """
        self.create_art()
        self._ascii_art = ScalableArt(self._ascii_art,
                                      self._height, self._width).generate_zoom_art()

    def __str__(self):
        """
        String representation of the ArtGenerator instance.
        """
        return self._ascii_art

    # Properties and setters for various attributes

    @property
    def message(self):
        """
        Property method for accessing the message attribute.
        """
        return self._message

    @message.setter
    def message(self, value):
        """
        Setter method for the message attribute.
        """
        self._message = value

    @property
    def justify(self):
        """
        Property method for accessing the justify attribute.
        """
        return self._justify

    @justify.setter
    def justify(self, value):
        """
        Setter method for the justify attribute.
        """
        self._justify = value

    @property
    def font(self):
        """
        Property method for accessing the font attribute.
        """
        return self._font

    @font.setter
    def font(self, value):
        """
        Setter method for the font attribute.
        """
        self._font = value

    @property
    def width(self):
        """
        Property method for accessing the width attribute.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        """
        self._width = value

    @property
    def height(self):
        """
        Property method for accessing the height attribute.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        """
        self._height = value

    @property
    def symbol(self):
        """
        Property method for accessing the symbol attribute.
        """
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        """
        Setter method for the symbol attribute.
        """
        self._symbol = value

    @property
    def ascii_art(self):
        """
        Property method for accessing the ascii_art attribute.
        """
        return self._ascii_art
