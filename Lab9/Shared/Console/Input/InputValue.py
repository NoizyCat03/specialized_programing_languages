"""
Module defining the InputValue class.
"""

from Shared.Console.Print.ConsolePrint import ConsolePrint
from colorama import Style

from Shared.Validate.Validator import Validator


class InputValue:
    """
    Class representing an input value with various validation methods.
    """

    def __init__(self, **kwargs) -> None:
        """
        Constructor for the InputValue class.

        Args:
            **kwargs: Keyword arguments for customization.
                      - 'message': The message to display when prompting for input.
        """
        self._message = kwargs['message'] if 'message' in kwargs else ''
        self._value = ''
        self.__validator = Validator()
        self.__print = ConsolePrint()

    def input_text(self) -> None:
        """
        Method to input and validate a text value.
        """
        self._value = self.user_input(f"{self._message}: ")

    def input_int_number(self) -> None:
        """
        Method to input and validate an integer number.
        """
        self._value = self.__validator.int_validate(self.user_input(f"{self._message}: "))

    def input_float_number(self) -> None:
        """
        Method to input and validate a floating-point number.
        """
        self._value = self.__validator.float_validate(self.user_input(f"{self._message}: "))

    def input_bool(self) -> None:
        """
        Method to input and validate a boolean value.
        """
        self._value = self.__validator.bool_validate(self.user_input(f"{self._message}: "))

    def convert__string_object(self, message: str) -> None:
        """
        Method to convert a string to an object.

        Args:
            message (str): The message to be converted to an object.
        """
        self._value = message

    def select_object_with_dict(self, dictionary: dict):
        """
        Method to select an object from a dictionary.

        Args:
            dictionary (dict): The dictionary containing key-value pairs.
        """
        self.__print.output = f"{self._message}:"
        self.__print.print()
        for key, value in dictionary.items():
            self.__print.output = f"{key}: {value}" + Style.RESET_ALL
            self.__print.print()
        param = self.user_input('Input key of dictionary: ')
        self._value = dictionary.get(param, '')

    @staticmethod
    def user_input(message):
        """
        Static method to get user input.

        Args:
            message (str): The message to display when prompting for input.

        Returns:
            str: User input as a string.
        """
        return input(f"{message}")

    def __str__(self) -> str:
        """
        String representation of the input value.

        Returns:
            str: The string representation of the input value.
        """
        return self._value

    @property
    def message(self) -> str:
        """
        Getter for the message property.

        Returns:
            str: The message associated with the input value.
        """
        return self._message

    @message.setter
    def message(self, message) -> None:
        """
        Setter for the message property.

        Args:
            message: The new message to set.
        """
        self._message = message

    @property
    def value(self):
        """
        Getter for the value property.

        Returns:
            str: The current value of the input.
        """
        return self._value
