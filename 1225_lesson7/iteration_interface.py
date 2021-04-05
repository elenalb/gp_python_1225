# интерфейс итерации

my_list = [30, 105.6, 'test', False]
# for el in my_list:  # __iter__(), __next__(), StopIteration
#     print(el)


class Iterator:
    """
    Объект-итератор
    """
    def __init__(self, start=0):
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class IterObj:
    """
    Объект, поддерживающий интерфейс итерации
    """
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        return Iterator(self.start)


obj = IterObj(start=1)
# for el in obj:
#     print(el)


class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


iterobj = Iter(start=1)
print(iterobj)
for el in iterobj:
    print(el)

# iterobj = Iter(start=1)
# for el in iterobj:
#     print("второй раз")
#     print(el)
