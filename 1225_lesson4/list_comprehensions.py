# генераторы списков

my_list = [1, 2, 3]
new_list = [el * 2 for el in my_list]

print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

new_list_1 = []
for el in my_list:
    new_list_1.append(el * 2)

print(f"Новый список: {new_list_1}")

lines = [line.strip() for line in open("text.txt")]
print(f"Строки из файла: {lines}")

new_list_if = [el for el in my_list if el > 1]
print(f"Новый список с условием: {new_list_if}")

str_1 = 'abc'
str_2 = 'd'
str_3 = 'efg'
sets = [i + j + k for i in str_1 for j in str_2 for k in str_3]
print(f"Вложенны циклы: {sets}")

my_tuple = (1, 2, 3)
new_tuple = (el * 2 for el in my_list)  # объект-итератор!

print(f"Исходный кортеж: {my_tuple}")
print(f"Новый кортеж: {new_tuple}")

for el in new_tuple:
    print(el)

# генераторы словарей и множеств
my_dict = {el: el * 2 for el in range(3)}
print(f"Генератор словаря: {my_dict}")

my_set = {el ** 2 for el in range(4)}
print(f"Генератор множества: {my_set}")
