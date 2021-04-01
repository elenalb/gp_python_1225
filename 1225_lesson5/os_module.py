import os

# os.remove("print_to_file")

# os.rename("new_example", "example")

# print(os.listdir())

# os.path - выполнение операций с путями
path_to_dir = os.path.join(r"C:\Users", "elena.babenko", "PycharmProjects", "geekbrains_python")
print(os.path.basename(r"C:\Users\elena.babenko\geekbrains_python\test_file"))
print(os.path.dirname(r"C:\Users\elena.babenko\geekbrains_python"))
print(os.path.exists(r"C:\Users\elena.babenko\PycharmProjects\geekbrains_python\test_file"))
print(os.path.isfile(r"C:\Users\elena.babenko\PycharmProjects\geekbrains_python\test_file"))
print(os.path.isdir(path_to_dir))

print(os.path.join(r"C:\Users", "elena.babenko", "PycharmProjects", "geekbrains_python"))
print(os.path.split(r"C:\Users\elena.babenko\PycharmProjects\geekbrains_python\test_file"))
