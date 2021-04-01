# random
import random

# генерация целых случайных чисел
print(random.randint(-100, 10))

print(random.randrange(10))
print(random.randrange(10, 11))  # нижняя граница в диапазон включается, верхня нет!
print(random.randrange(10, 20, 3))

# генерация дробных случайных чисел
print(random.random())  # float в диапазоне от 0 до 1
print(random.random() * 10)  # диапазон от 0 до 10
print(random.random() * (10 - 4) + 4)  # диапазон от 4 до 10

print(random.choice([1, 2, 3, 4]))
print(random.uniform(1, 10))  # вещественное число в указанном диапазоне
random.shuffle([1, 2, 3, 4])  # перемешивание последовательности элементов
# print(new_list)
