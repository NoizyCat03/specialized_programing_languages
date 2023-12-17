"""
Module defining the Validator class for validating and converting values.
"""


class Validator:
    """
    Singleton class for validating and converting values.
    """
    _instance = None

    def __new__(cls):
        """
        Override the __new__ method to implement the Singleton pattern.

        Returns:
            Validator: The instance of the Validator class.
        """
        if cls._instance is None:
            cls._instance = super(Validator, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def int_validate(value):
        """
        Validate and convert a value to an integer.

        Args:
            value: The value to be validated and converted.

        Returns:
            int: The converted integer value.

        Raises:
            TypeError: If the value cannot be converted to an integer.
        """
        try:
            return int(value)
        except TypeError:
            raise TypeError('Value is not convertible to int')

    @staticmethod
    def float_validate(value):
        """
        Validate and convert a value to a float.

        Args:
            value: The value to be validated and converted.

        Returns:
            float: The converted float value.

        Raises:
            TypeError: If the value cannot be converted to a float.
        """
        try:
            return float(value)
        except TypeError:
            raise TypeError('Value is not convertible to float')

    @staticmethod
    def bool_validate(value):
        """
        Validate and convert a value to a boolean.

        Args:
            value: The value to be validated and converted.

        Returns:
            bool: The converted boolean value.

        Raises:
            TypeError: If the value cannot be converted to a boolean.
        """
        try:
            return bool(value)
        except TypeError:
            raise TypeError('Value is not convertible to bool')
