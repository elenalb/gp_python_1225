# return со значением


def s_calc():
    r_val = float(input("Укажите радиус цилиндра: "))
    h_val = float(input("Укажите высоту цилиндра: "))
    global s_side, s_circle
    # площадь боковой поверхности
    s_side = 2 * 3.14 * r_val * h_val
    # площадь основания цилиндра
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full


s_val = s_calc()
print(s_val)
# print(s_calc())

# return без значения
def s_calc_try_except():
    try:
        r_val = float(input("Укажите радиус цилиндра: "))
        h_val = float(input("Укажите высоту цилиндра: "))
    except ValueError:
        return
    # площадь боковой поверхности
    s_side = 2 * 3.14 * r_val * h_val
    # площадь основания цилиндра
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full


# print(s_calc_try_except())

# возврат набора значений
def s_calc_several_outputs():
    try:
        r_val = float(input("Укажите радиус цилиндра: "))
        h_val = float(input("Укажите высоту цилиндра: "))
    except ValueError:
        return
    # площадь боковой поверхности
    s_side = 2 * 3.14 * r_val * h_val
    # площадь основания цилиндра
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full, s_circle, s_side


s_full, s_circle, s_side = s_calc_several_outputs()
print(s_full)
print(s_circle)
print(s_side)
