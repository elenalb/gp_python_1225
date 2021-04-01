# полиморфизм


# перегрузка методов
class Auto:
    def auto_start(self, param1, param2=None):
        if param2:
            print("Param2 is not None!")
            return param1 + param2
        return param1 ** 2


a = Auto()
print(a.auto_start(10))
print(a.auto_start(10, 10))


# переопределение методов
class Transport:
    def show_info(self):
        print("Родительский класс Trasport")


class Bus(Transport):
    def show_info(self):
        print("Дочерний класс Bus")


class Bicycle(Transport):
    def show_info(self):
        print("Дочерний класс Bicycle")


t = Transport()
t.show_info()

b = Bus()
b.show_info()

bc = Bicycle()
bc.show_info()
