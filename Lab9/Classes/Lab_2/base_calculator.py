"""
Module docstring describing the purpose of the module.
"""

import math
from Classes.Lab_2.operators import OPERATORS


class BaseCalculator:
    """
    Class docstring describing the purpose of the class.
    """

    def __init__(self, **kwargs):
        """
        Constructor with optional keyword arguments for initialization.
        """
        self._num_1 = kwargs.get('num_1', 0)
        self._num_2 = kwargs.get('num_2', 0)
        self._operator = kwargs.get('operator', '+')
        self._custom_round = kwargs.get('custom_round', 0)
        self._result = 0

    @classmethod
    def _number_validate(cls, num):
        """
        Number validation method.
        """
        try:
            num = float(num)
            return num
        except ValueError as exc:
            raise ValueError(f"Parameter '{num}' is not a number") from exc

    @classmethod
    def _operator_validate(cls, symbol):
        """
        Operator validation method.
        """
        if symbol not in OPERATORS:
            raise ValueError(f"Operator is not in {OPERATORS}!")
        return symbol

    def _add(self):
        """
        Method for addition operation.
        """
        return self._num_1 + self._num_2

    def _sub(self):
        """
        Method for subtraction operation.
        """
        return self._num_1 - self._num_2

    def _mul(self):
        """
        Method for multiplication operation.
        """
        return self._num_1 * self._num_2

    def _div(self):
        """
        Method for division operation.
        """
        if self._num_2 != 0:
            return self._num_1 / self._num_2
        raise ZeroDivisionError("Division by zero")

    def _deg(self):
        """
        Method for exponentiation operation.
        """
        return self._num_1 ** self._num_2

    def _rem(self):
        """
        Method for remainder operation.
        """
        if self._num_2 != 0:
            return self._num_1 % self._num_2
        raise ZeroDivisionError("Division by zero")

    def _square(self):
        """
        Method for square root operation.
        """
        if self._num_1 >= 0:
            return math.sqrt(self._num_1)
        raise ArithmeticError("Square root of a negative number")

    def calc(self):
        """
        Calculator function to perform the calculation based on the selected operator.
        """
        operations = {'+': self._add, '-': self._sub, '*': self._mul, '/': self._div,
                      '^': self._deg, '√': self._square, '%': self._rem}

        if self._operator not in operations:
            raise ValueError(f"Invalid operator: {self._operator}")

        self._result = round(operations[self._operator](), self._custom_round)

    def __str__(self):
        """
        String representation of the calculator instance.
        """
        self.calc()
        if self._operator == '√':
            return f"{self._operator} {self._num_1} = {self._result}"
        return f"{self._num_1} {self._operator} {self._num_2} = {self._result}"

    @property
    def result(self):
        """
        Property method for accessing the result.
        """
        return self._result

    @property
    def custom_round(self):
        """
        Property method for accessing custom_round.
        """
        return self._custom_round

    @custom_round.setter
    def custom_round(self, value):
        """
        Setter method for custom_round.
        """
        self._custom_round = value

    @property
    def num_1(self):
        """
        Property method for accessing num_1.
        """
        return self._num_1

    @num_1.setter
    def num_1(self, value):
        """
        Setter method for num_1.
        """
        self._num_1 = self._number_validate(value)

    @property
    def num_2(self):
        """
        Property method for accessing num_2.
        """
        return self._num_2

    @num_2.setter
    def num_2(self, value):
        """
        Setter method for num_2.
        """
        self._num_2 = self._number_validate(value)

    @property
    def operator(self):
        """
        Property method for accessing operator.
        """
        return self._operator

    @operator.setter
    def operator(self, value):
        """
        Setter method for operator.
        """
        self._operator = self._operator_validate(value)
