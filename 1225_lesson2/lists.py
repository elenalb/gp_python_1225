# списки
# упорядоченный изменяемый набор объектов

print(list('abc'))

my_list = ['1', 3, True]

# методы списков
my_list.append('string')
print(my_list)

my_list.append([1, 2])
print(my_list)

my_list.extend([1, 2])
print(my_list)

my_list.insert(0, False)
print(my_list)

my_list.remove(True)
print(my_list)

my_list.pop(0)
print(my_list)

print(my_list.count(1))

my_list.reverse()
print(my_list)

# копия списка
my_list_1 = my_list.copy()
print(my_list_1)
my_list.clear()
print(my_list)
print(my_list_1)


# операторы is и in
print((1 and None) in my_list_1)

# is - тождественность
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3, 4, [1, 2, 3]]
print('list1 is list2', list1 is list2)
print('list1 == list2', list1 == list2)
print('list1 in list3', list1 in list3)
for el in list1:
    if el in list3:
        print(f'{el} is in list3')

list2 = list1

print(list1 is list2)

