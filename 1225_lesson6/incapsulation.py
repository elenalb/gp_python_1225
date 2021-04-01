# модификаторы доступа
# Public - публичный - var
# Protected - защищенный - _var
# Private - приватный - __var


class Auto:
    def __init__(self):
        print("Класс Auto")
        self.auto_name = "Mazda"
        self._auto_year = 2015
        self.__auto_model = "123"


a = Auto()
print(a.auto_name)

# Инкапсуляция - механизм сокрытия данных


class MyClass:
    _attr = "protected attr"

    def _method(self):
        print("Protected method")


mc = MyClass()
print(mc._attr)
mc._method()


class MyClassPrivate:
    __attr = "private attr"

    def __method(self):
        print("private method")


mcp = MyClassPrivate()
print(mcp._MyClassPrivate__attr)
mcp._MyClassPrivate__method()
