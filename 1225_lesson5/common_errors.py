# выявление ошибок при работе с файлами
# IOError, FileNotFound

try:
    f = open("example1")
    for line in f:
        print(line, end='')
except FileNotFoundError:
    print("Файл не найден!")
finally:
    f.close()

try:
    with open("example") as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print("Файл не найден!")
