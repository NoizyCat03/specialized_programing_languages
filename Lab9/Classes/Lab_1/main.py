
history = []

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))
    if check == 'так':
        try:
            count = int(input("Введіть кількість знаків після коми: "))
            number_1 = int(input("Введіть число №1: "))
            number_2 = int(input("Введіть число №2: "))
            operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %" "): "))
            lst = ['+', '-', '*', '/', '^', '√', '%']
            while True:
                if operator in lst:
                    if operator == '^':
                        operator = '**'
                    break
                else:
                    print("Помилка при введені оператора, введіть ще раз")
                    operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                         "): "))
        except ValueError:
            print("Помилка вводу одного з чисел")
            continue
        try:
            if operator != '√':
                result = round(eval(f"{number_1} {operator} {number_2}"), count)
                message = f"Обчислення: {number_1} {operator} {number_2} = {result}"
            else:
                import math
                result = (round(math.sqrt(number_1), 2))
                message = f"Обчислення: {operator} {number_1}   = {result}"
        except ZeroDivisionError:
            print("Ділення на нуль неможливо")
            continue
        except SyntaxError:
            print("Помилка арифметичної операції")
            continue
        print(message)
        history.append(message)
        output = input("Показати історію:(введіть так, якщо бажаєте) ")
        if output == 'так':
            print([result for result in history])
        else:
            continue
    else:
        break
        