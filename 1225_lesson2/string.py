# строки
# упорядоченный набор символов. неизменяемый тип!

my_str = "first_string"
# print(my_str)
# print(type(my_str))
my_str_1 = str(4)
# print(my_str_1)
# print(type(my_str_1))

# конкатенация
str1 = 'abc'
str2 = 'def'
# print(str1 + str2)

# взятие элемента по индексу
# print(my_str[6])

# извлечение среза [start:finish:step], default step = 1
# print(my_str)
# print(my_str[1:7:2])
# print(my_str[-1])
# print(my_str[::-1])  # разворачивание строки

# механизмы реверса строк
# 1 способ: срез с отрицательным шагом
# print(my_str[::-1])
# 2 способ: обратная итерация
# for el in reversed(my_str):
#     print(el, end='')
# print()
# 3 способ: реверс на месте
reversed_str = ''
str_symbols = list(my_str)
for el in range(len(my_str) // 2):
    tmp = str_symbols[el]
    str_symbols[el] = str_symbols[len(my_str) - el - 1]
    str_symbols[len(my_str) - el - 1] = tmp
reversed_str = ''.join(str_symbols)
# print(reversed_str)

# методы строк
print(len(my_str))  # длина строки
print(my_str.split('_'))
test_str = 'kasjhdjs s   dad \nsdsdsd    sadasd        sds  sdsd   '
print(test_str.split())
print(''.join(['a', 'b', 'c']))
print(my_str.title())
print(my_str.upper())  # str.lower()
print(my_str.count('s'))
