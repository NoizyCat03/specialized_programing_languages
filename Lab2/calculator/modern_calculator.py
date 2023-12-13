import math

from Lab2.calculator import BaseCalculator


# Represent extended version of calculator that supports more operators
class ModernCalculator(BaseCalculator):

    def __init__(self, valid_operators: list[str]):
        super().__init__(valid_operators)

    # Perform loop of calculations
    def do_operation(self):
        while True:
            result = self.perform_operation()
            print(f"Result: {result}")
            answer = input("Do you want to perform another operation?(y/n)\n")
            if answer.lower() != 'y':
                break

    # Perform a single calculation
    def perform_operation(self):
        result = super().perform_operation()
        if result is None:
            if self._operator == '%':
                result = self._first_number % self._second_number
            elif self._operator == '^':
                result = self._first_number ** self._second_number
            elif self._operator == 'sqrt':
                result = self.__get_sqrt()
            else:
                print("Invalid operator")
        return result

    # Returns the square root of a number that user chose
    def __get_sqrt(self) -> float:
        print(f"Your numbers:\n1 - {self._first_number}\n2 - {self._second_number}")
        option = int(input("Choose the number that should be converted?\n"))
        if option == 1:
            if self._first_number < 0:
                print(f"Cannot get square of {self._first_number} because it is < 0")
            else:
                return math.sqrt(self._first_number)
        if option == 2:
            if self._second_number < 0:
                print(f"Cannot get square of {self._second_number} because it is < 0")
            else:
                return math.sqrt(self._second_number)
