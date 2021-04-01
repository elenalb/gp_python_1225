# именные функции
def func_name(arg_1, arg_2):
    # тело функции
    return arg_1 + arg_2


print(func_name(1, 2))
print(func_name('abc', 'cde'))


def ext_func(var_1):
    def int_func(var_2):
        return var_1 + var_2
    return int_func


f_obj = ext_func(1)
print(f_obj(2))


def my_func():
    pass


print(my_func())
