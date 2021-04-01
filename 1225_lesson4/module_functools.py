from functools import reduce, partial


# функция reduce()
def my_func(first_el, second_el):
    return first_el + second_el


print(reduce(my_func, [10, 20, 30, 40]))

# функция partial()
new_func = partial(my_func, 2)
print(new_func(4))
