# области видимости
# глобальная, локальная и нелокальная

# локальная


def s_calc(r_val, h_val):
    global s_side, s_circle
    # площадь боковой поверхности
    s_side = 2 * 3.14 * r_val * h_val
    # площадь основания цилиндра
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full


s_val = s_calc(1, 3)
# print(s_val)
# print(s_side)
# print(globals())  # словарь со всеми глобальными переменными


# нелокальная область
def ext_func():
    my_var = 0

    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var

    return int_func


# func_obj = ext_func()
# print(func_obj())
# print(func_obj())
