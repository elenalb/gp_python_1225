# класс
# CamelCase
# MyNewClass


class Auto:
    # атрибуты класса
    auto_name = "Lexus"
    auto_model = "R1234"
    auto_year = 2015

    # методы класса
    def on_auto_start(self):
        print("Заводим автомобиль")

    def on_auto_stop(self):
        print("Останавливаем автомобиль")


# экземпляр (объект) класса
a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# a.on_auto_start()
# a.on_auto_stop()


# атрибуты
class Auto1:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def on_auto_start(self, auto_name, auto_model, auto_year):
        print("Заводим автомобиль")
        # атрибуты экземпляра
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto1.auto_count += 1

    def on_auto_stop(self):
        print("Останавливаем автомобиль")


a1 = Auto1()
a1.on_auto_start("Lexus", "123", 2015)
print(a1.auto_name)
print(a1.auto_model)
print(a1.auto_count)

a2 = Auto1()
a2.on_auto_start("Audi", "345", 1995)
print(a2.auto_name)
print(a2.auto_model)
print(a2.auto_count)
