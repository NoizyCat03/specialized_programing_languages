"""
Module defining the ConsolePrint class.
"""


class ConsolePrint:
    """
    Class representing a console printer.
    """

    def __init__(self, **kwargs):
        """
        Constructor for the ConsolePrint class.

        Args:
            **kwargs: Keyword arguments for customization.
                      - 'output': The output message to be printed.
        """
        self.__output = kwargs['output'] if 'output' in kwargs else ''

    def print(self):
        """
        Method to print the output message to the console.
        """
        print(self.__output)

    @property
    def output(self) -> str:
        """
        Getter for the output property.

        Returns:
            str: The current output message.
        """
        return self.__output

    @output.setter
    def output(self, output) -> None:
        """
        Setter for the output property.

        Args:
            output: The new output message to set.
        """
        self.__output = output
