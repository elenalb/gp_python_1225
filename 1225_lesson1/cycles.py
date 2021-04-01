# while

number = int(input("Введите число: "))
while number < 10:
    print("Number =", number)
    number += 1  # number = number + 1
print("Программа завершена!")

# бесконечный цикл! так делать не нужно!
# while number > 0:
#     print("!", end='')
#     number += 1

# операторы break, continue
while True:
    number += 1
    if number > 15:
        break
    if number % 2 == 0:
        print("Number", number, "is even")
        continue
    print("Number =", number)
