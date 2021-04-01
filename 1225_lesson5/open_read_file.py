# открытие
# f = open("example", "r")  # r - открыт на чтение

# second_file = open(r"C:\Users\elena.babenko\PycharmProjects\geekbrains_python\test_file")
# # \n, \s, \t, \p

# # чтение
# content = f.read()  # считывает файл полностью
# print(content)

# string_from_file = f.readline()  # считывает файл построчно
# print(f"Строка из файла: {string_from_file}")

# strings_from_file = f.readlines()  # список всех строк в файле
# print(strings_from_file)

# чтение файла по частям
# for line in f:
#     print(line, end='')

# while True:
#     file_content = f.read(10)  # количество байт, которое необходимо считать
#     print(file_content)
#
#     if not file_content:
#         break

# чтение бинарных файлов
# my_f = open("path_to_file", "rb")  # read binary

# # запись в файл
# out_file = open("file_to_write", "w")  # w - write, открытие на запись
# # out_file.write("some string\nanother string")
# lines = ['some string\n', 'another string\n', 'third string']
# out_file.writelines(lines)
# out_file.close()

# # закрытие !
# f.close()


# менеджер контекста - сам закрывает файл!

# f = open("example")
# for line in f:
#    print(line, end='')
# f.close()

with open("example") as f:
    for line in f:
        print(line, end='')
