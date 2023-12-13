import logging


# Represents calculation settings
class CalculationSettings:

    # Calculating settings constructor
    def __init__(self, digits_after_point=2):
        logging.debug("Initialize calculation settings")
        self.__digits_after_point = digits_after_point

    # Setting interface
    def settings_interface(self):
        logging.info("Executing setting interface")
        flag = True
        while flag:
            option = int(input("Enter setting option:\n1 - change number of digits after point\n"
                               "0 - exit\n"))
            if option == 1:
                digits = int(input("Enter number of digits\n"))
                self.digits_after_point = digits
            elif option == 0:
                flag = False
            else:
                print("Invalid option entered")
                flag = False

    # Digits after point getter
    @property
    def digits_after_point(self):
        logging.info("Getting digits after point data")
        return self.__digits_after_point

    # Digits after point setter
    @digits_after_point.setter
    def digits_after_point(self, value):
        logging.info("Setting digits after point data")
        if type(value) != int:
            print("Value should be integer")
        elif value < 0:
            print("You cannot set value smaller then 0")
        else:
            self.__digits_after_point = value
