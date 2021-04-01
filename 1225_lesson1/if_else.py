
a = int(input("Enter digit: "))
if a % 2 == 0:
    if a > 10:
        print("a = ", a)
    print("a is even")  # блок кода 1
else:
    print("a is odd")  # блок кода 2

# инструкции на одном уровне вложенности - elif
color = input("Enter some color: ")
if color == "red":
    print("красный")
elif color == "blue":
    print("синий")
elif color == "green":
    print("зеленый")
else:
    print("Цвет неизвестен!")
