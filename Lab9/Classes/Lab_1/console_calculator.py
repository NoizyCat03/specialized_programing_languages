import math

from Classes.Lab_2.operators import OPERATORS

_num_1 = 0
_num_2 = 0
_operator = '+'
_custom_round = 0
result = 0


def _number_validate(num):
    """
    Number validation method.
    """
    try:
        num = float(num)
        return num
    except ValueError as exc:
        raise ValueError(f"Parameter '{num}' is not a number") from exc


def _operator_validate(symbol):
    """
    Operator validation method.
    """
    if symbol not in OPERATORS:
        raise ValueError(f"Operator is not in {OPERATORS}!")
    return symbol


def _add():
    """
    Method for addition operation.
    """
    return _num_1 + _num_2


def _sub():
    """
    Method for subtraction operation.
    """
    return _num_1 - _num_2


def _mul():
    """
    Method for multiplication operation.
    """
    return _num_1 * _num_2


def _div():
    """
    Method for division operation.
    """
    if _num_2 != 0:
        return _num_1 / _num_2
    raise ZeroDivisionError("Division by zero")


def _deg():
    """
    Method for exponentiation operation.
    """
    return _num_1 ** _num_2


def _rem():
    """
    Method for remainder operation.
    """
    if _num_2 != 0:
        return _num_1 % _num_2
    raise ZeroDivisionError("Division by zero")


def _square():
    """
    Method for square root operation.
    """
    if _num_1 >= 0:
        return math.sqrt(_num_1)
    raise ArithmeticError("Square root of a negative number")


def calc():
    """
    Calculator function to perform the calculation based on the selected operator.
    """
    operations = {'+': _add, '-': _sub, '*': _mul, '/': _div,
                  '^': _deg, '√': _square, '%': _rem}

    if _operator not in operations:
        raise ValueError(f"Invalid operator: {_operator}")
    result = round(operations[_operator](), _custom_round)


def __str__():
    """
    String representation of the calculator instance.
    """
    calc()
    if _operator == '√':
        return f"{_operator} {_num_1} = {result}"
    return f"{_num_1} {_operator} {_num_2} = {result}"
