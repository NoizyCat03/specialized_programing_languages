from calculator import ModernCalculator


def execute_lab2():
    valid_operators = ['+', '-', '*', '/', '^', '%', 'sqrt']
    calc = ModernCalculator(valid_operators)
    calc.do_operation()


if __name__ == '__main__':
    execute_lab2()
