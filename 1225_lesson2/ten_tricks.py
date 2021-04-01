# 1. объединение списков без циклов
my_list = [[1, 2], [2, 3]]
merged_list = sum(my_list, [])

# 2. поиск уникальных элементов в списке
print(list(set(merged_list)))

# 3. обмен значениями через кортежи
var1, var2 = 1, 2
print(var1, var2)
var1, var2 = var2, var1
print(var1, var2)

# 4. вывод значения несуществующего ключа в словаре
my_dict = {1: 'one', 2: 'two'}
print(my_dict.get(3))

# 5. поиск самых часто встречающихся элементов списка
print(max(set(merged_list), key=merged_list.count))

# 6. распаковка последовательностей при неизвестном количестве элементов - *
el1, *el2, el3 = merged_list
print(el1, el2, el3)
el1, el2, el3, el4, *el5 = merged_list
print(el1, el2, el3, el4, el5)

# 7. вывод print() без переноса строки
# for el in merged_list:
#     print(el, end='/')

# 8. сортировка словаря по значениям
my_dict = {'python': 1991, 'java': 1995}
print(sorted(my_dict, key=my_dict.get))

# 9. нумерованные списки
for ind, el in enumerate(['zero', 'one', 'two', 'three']):
    print(ind, el)

# 10. транспонирование матрицы
# 1 2 3
# 2 3 4
# [[1, 2, 3], [2, 3, 4]]

# транспонирование матрицы:
# 1 2
# 2 3
# 3 4

old_matrix = [[1, 2, 3], [2, 3, 4]]
transp_matrix = zip(*old_matrix)
print(list(transp_matrix))
