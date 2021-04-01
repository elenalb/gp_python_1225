# for in
# for [переменная-итератор] in [последовательность]:
#    [действия с переменной-итератором, например]

for i in "abc":
    print(i)

for el in [1, 2, 3]:
    print(el)

my_dict = {1: 'one', 2: 'two'}

for key, value in my_dict.items():
    print(f"{key} = {value}")

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
is_list1_in_list2 = None
for el in list1:
    if el not in list2:
        is_list1_in_list2 = False
        break
    else:
        is_list1_in_list2 = True
print(is_list1_in_list2)
