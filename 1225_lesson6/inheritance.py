# наследование


# родительский класс
class Transport:
    def transport_method(self):
        print("Это родительский класс")


# дочерний класс
class Auto(Transport):
    def auto_method(self):
        print("Это дочерний класс Auto")


a = Auto()
# a.auto_method()
# a.transport_method()


# множественное наследование
# несколько дочерних классов
class Bus(Transport):
    def bus_method(self):
        print("Это дочерний класс Bus")


b = Bus()
# b.bus_method()
# b.transport_method()


class Shape:
    def __init__(self, color, length, width):
        self.color = color
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color, length, width)
        # Shape.__init__(self, color, length, width)
        self.rectangle_p = 2 * (self.length * self.width)

    def get_perimeter(self):
        return self.rectangle_p


class Square(Rectangle):
    def __init__(self, color, a):
        super().__init__(color, a, a)


r = Rectangle("black", 10, 20)
print(r.color)
print(r.square())
print(r.get_perimeter())
s = Square("white", 10)
print(s.color)
print(s.square())
print(s.get_perimeter())


# несколько родителей
class Player:
    def __init__(self, name):
        self.name = name

    def player_method(self):
        print(f"Родительский класс Player. self.name = {self.name}")


class Navigator:
    def __init__(self, name):
        self.name = name

    def navigator_method(self):
        print(f"Родительский класс Navigator. self.name = {self.name}")


class MobilePhone(Player, Navigator):
    def __init__(self, name):
        super().__init__(name)

    def mobile_method(self):
        print("Дочерний класс MobilePhone")


mp = MobilePhone("Spotify")
mp.mobile_method()
mp.navigator_method()
mp.player_method()
