# конструкторы и методы


class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    # конструктор
    def __init__(self, auto_name):
        # объявляем атрибуты класса
        Auto.auto_count += 1
        self.auto_name = auto_name
        print(Auto.auto_count)

    def get_class_info(self):
        print(f"Информация о классе: auto_name = {self.auto_name}")


a1 = Auto("Mazda")
a1.get_class_info()
a2 = Auto("BMW")
a2.get_class_info()
a3 = Auto("Audi")
a3.get_class_info()

