# перегрузка операторов
# __init__() - конструктор объектов класса
# __del__() - деструктор
# __str__() - print()
# __add__() - +
# __setattr__() - присваивание - =
# __getitem__() - извлечение элемента по индексу
# __call__() - обращение к экземпляру класса как к функции
# __gt__() - >
# __lt__() - <
# __ge__() - >=
# __le__() - <=
# __eq__() - ==
# __iadd__() - +=
# __isub__() - -=


# # __init__()
# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#
# mc = MyClass("param")
# print(mc.param)


# # __del__()
# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __del__(self):
#         print(f"Удаляем объект {self.param} класса MyClass")
#
#
# mc = MyClass("param")
# del mc


# # __str__()
# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __str__(self):
#         return f"Объект с параметрами: {self.param}"
#
#
# mc = MyClass("param")
# print(mc)


# # __add__()
# class MyClass:
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
#
#     def __str__(self):
#         return f"Объект с параметрами: {self.param1}, {self.param2}"
#
#     def __add__(self, other):
#         return MyClass(self.param1 + other.param2, other.param1 + self.param2)
#
#
# mc1 = MyClass(10, 20)
# mc2 = MyClass(30, 40)


# # __setattr__()
# class MyClass:
#     def __setattr__(self, attr, value):
#         if attr == 'param1':
#             self.__dict__[attr] = value
#         else:
#             print(f"Атрибут {attr} недопустим!")
#
#
# mc = MyClass()
# mc.param1 = 50
# print(mc.param1)
# mc.param2 = 30


# # __call__()
# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __call__(self, newparam):
#         self.param = newparam
#
#     def __str__(self):
#         return f"Параметр объекта: {self.param}"
#
#
# mc = MyClass("abc")
# print(mc)
# mc("def")
# print(mc)


# # __lt__() - <
# class Salary:
#     param = 50000
#
#     def __lt__(self, other):
#         print("Оклад меньше премии?")
#         return self.param < other.param
#
#
# class Prize:
#     param = 10000
#
#     def __lt__(self, other):
#         print("Премия меньше оклада?")
#         return self.param < other.param
#
#
# s = Salary()
# p = Prize()
#
# check = (p < s)
# print(check)
