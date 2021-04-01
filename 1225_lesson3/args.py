# аргументы функций
# позиционные, именованные, обязательные и необязательные


# позиционные
def first_func(var_1, var_2):
    return var_1 + var_2


# print(first_func(1, 2))


# именованные
def second_func(var_2, var_1):
    return var_1 + var_2


# print(second_func(var_1=1, var_2=2))


# обязательные
def third_func(var_1, var_2):
    return var_1 * var_2


# print(third_func(1, 2))


# необязательные
def fourth_func(var_1, var_2=2):
    return var_1 * var_2


# print(fourth_func(1, var_2=10))


# args, kwargs
def my_func(*args):
    return args


print(my_func(10, 'str', False))


def kwargs_func(**kwargs):
    return kwargs


print(kwargs_func(var_1=1, var_2=True, var_3='str'))


def new_func(*param):
    return param


print(new_func(1, 3, 3))
