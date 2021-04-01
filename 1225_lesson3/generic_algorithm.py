# алгоритм создания функции

# 1. Определяем название функции - информативное!
# 2. Определяем имена параметров
# 3. Описываем работу функции, аргументы, их типы в документации
# 4. Записываем логику функции


def rectangle_area_calc(length, width):
    """
    Возвращает расчет площади прямоугольника

    :param length: float, length of rectangle
    :param width: float, width of rectangle
    :return: float
    """
    return length * width


print(rectangle_area_calc(5, 15))
help(rectangle_area_calc)
