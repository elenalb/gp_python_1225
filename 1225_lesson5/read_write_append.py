"""
режимы доступа к файлу
r - read, default
w - write, содержимое файла удаляется, если файла нет, создается новый
x - write, создает файл, если его нет, если файл есть - ошибка!
a - append, добавляет информацию в конец файлы
b - binary
t - text
+ - read/write
"""

# # режим x
# f_1 = open("file_to_write", "w")
# f_2 = open("file_to_write_x", "x")
#
# f_1.close()
# f_2.close()

# # режим a
# file_to_append = open("example", "a")
# file_to_append.write("\nappended line")
# # file_to_append.close()
#
# # режим +
# with open("file_to_write", "w+") as f:
#     f.write("new string!")
#     f.seek(0)
#     content = f.read()
#     print(f"File content: {content}")

# параметры файлового объекта
"""
file.closed - открыт или закрыт файл
file.mode - режим открытия файла
file.name - имя файла
"""
# print(f"file_to_append.closed: {file_to_append.closed}")
# print(f"file_to_append.mode: {file_to_append.mode}")
# print(f"file_to_append.name: {file_to_append.name}")
#
# print(f"f.closed: {f.closed}")
# print(f"f.mode: {f.mode}")
# print(f"f.name: {f.name}")

# # указатель в файле
# f = open("example")
#
# # f.tell() - позиция указателя в файле
# print(f"Позиция указателя перед чтением файла: {f.tell()}")
# content = f.readlines()
# print(f"File content: {content}")
# print(f"Позиция указателя после чтением файла: {f.tell()}")
# content = f.readlines()
# print(f"File content: {content}")
# # перемещение указателя в файле
# f.seek(0)
# print(f"Позиция указателя после перемещения: {f.tell()}")
# content = f.readlines()
# print(f"File content: {content}")
#
# f.close()

# # print в файл
# with open("print_to_file", "w") as f:
#     print("Some print to show how to print to file", file=f)
