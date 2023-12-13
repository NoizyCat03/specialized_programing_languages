import logging

from calculator import Calculator, CalculationSettings


def execute_lab1():
    logging.info("Executing lab work 1")
    valid_operators = ['+', '-', '*', '/', '^', '%', 'sqrt']
    flag = True
    calculator = Calculator("data.json")
    calc_settings = CalculationSettings()
    while flag:
        print("Program options:\n1 - make calculation\n2 - see calculation history\n"
              "3 - clear memory\n4 - change calculation settings\n0 - exit")
        option = int(input("Choose option:\n"))
        if option == 1:
            calculator.setup_calculator(valid_operators)
            print("Result:")
            result = calculator.do_operation()
            print(f"{result:.{calc_settings.digits_after_point}f}")
        elif option == 2:
            calculator.print_history()
        elif option == 3:
            calculator.clear_memory()
        elif option == 4:
            calc_settings.settings_interface()
        elif option == 0:
            flag = False


if __name__ == "__main__":
    execute_lab1()
