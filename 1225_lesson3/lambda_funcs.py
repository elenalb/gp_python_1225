# lambda - анонимные функции

my_func = lambda p_1, p_2: p_1 ** p_2

# print(my_func(1, 2))

# print((lambda p_1, p_2: p_1 * p_2)(1, 3))

new_func = lambda *args: args

# print(new_func(1, 2, 3, True))


def named_func(param):
    return param ** 2


print(named_func(2))


new_lambda_func = lambda param: param ** 2

print(new_lambda_func(2))
