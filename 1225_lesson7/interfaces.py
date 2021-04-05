# интерфейсы
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method1(self):
        pass

    @abstractmethod
    def my_method2(self):
        pass


class MyClass(MyAbstractClass):
    def my_method1(self):
        print("my_method1()")

    def my_method2(self):
        print("my_method2()")

    def my_method3(self):
        print("my_method3()")


mc = MyClass()
mc.my_method2()
mc.my_method3()
