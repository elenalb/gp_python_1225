# создание собственных исключений
# Exception
# ZeroDivisionError
# IndexError
# KeyError
# FileNotFoundError
# TypeError
# ValueError

import traceback

try:
    res = 100 / 1
except ZeroDivisionError:
    print("Деление на ноль недопустимо!")
else:
    print(f"Результат деления: {res}")
finally:
    print("Программа завершена")


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите четное число: ")
try:
    digit = int(inp_data)
    if digit % 2 != 0:
        raise OwnError("Вы ввели нечетное число!")
except ValueError:
    print("Вы ввели не число!")
except OwnError as err:
    print(err)
else:
    print(f"All OK! Вы ввели число {digit}")


def division(a, b):
    return a / b


try:
    res = division(1, 0)
except Exception as exc:
    print(f"Ошибка:\n {traceback.format_exc()}")
