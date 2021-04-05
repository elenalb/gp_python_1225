# переопределение методов


class Parent:
    def __init__(self):
        print("Конструктор класса-родителя")

    def method(self):
        print("Метод method() класса-родителя")


class Child(Parent):
    def __init__(self):
        print("Конструктор класса-потомка")
        # Parent.__init__(self)
        super().__init__()

    def method(self):
        Parent.method(self)
        print("Метод method() класса-потомка")


c = Child()
c.method()
