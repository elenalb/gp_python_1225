# статические методы


class Auto:
    @staticmethod
    def get_class_info():
        print("Информация о классе")


Auto.get_class_info()


class MyClass:
    @staticmethod
    def sum_1(param1, param2):
        return param1 + param2

    def sum_2(self, param1, param2):
        return param1 + param2

    def sum_3(self, param1, param2):
        return MyClass.sum_1(param1, param2)


print(MyClass.sum_1(10, 20))
mc = MyClass()
print(mc.sum_2(20, 30))
print(mc.sum_1(30, 40))
print(mc.sum_3(40, 50))


# классовый метод


class MyClass1:
    @classmethod
    def class_method(cls, param):
        print(cls, param)


MyClass1.class_method('param')
mc = MyClass1()
mc.class_method('param')
