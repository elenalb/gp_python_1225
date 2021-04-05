# декораторы
# @property


class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    @property
    def method(self):
        return f"Параметры класса: {self.param1}, {self.param2}"


mc = MyClass("first", "second")
print(mc.param1)
print(mc.method)


# 2000 - 2021 гг.
class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2021:
            self.__year = 2021
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"


a = Auto(2300)
print(a.year)
