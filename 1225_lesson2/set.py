# множества
# контейнер с неповторяющимися элементами, расположенными в случайном порядке!

my_set = set('aaaaabcdef')  # изменяемое множество
my_frozenset = frozenset('aaaaabcdef')  # неизменяемое множество
my_set1 = {1, 1, 1, 1, 2}

print(my_set)
print(my_frozenset)

# my_set.add('1')
# print(my_set)
# my_set.remove('1')
# print(my_set)
# my_set.discard('1')
# print(my_set)
# my_set.discard('a')
# print(my_set)
# pop_el = my_set.pop()
# print(pop_el)
# my_set.clear()
# print(my_set)

print(my_set == my_frozenset)

my_s = set('abcdef')
my_fs = frozenset('abc')
# вычитание множеств
print(my_s - my_fs)
# объединение множеств
print(my_s | my_fs)
