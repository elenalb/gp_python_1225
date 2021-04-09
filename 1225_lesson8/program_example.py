# пример ООП-программы
# - сформулировать задачу
# - определить объекты предметной области, которые участвуют в решении задачи
# - выделить классы, на основе которых генерируются объекты
# - установить основные атрибуты и методы объектов
# - создать классы, их атрибуты и методы
# - создать объекты классов
# - выполнить итоговое решение задачи

# виртуальная модель образовательного процесса
# объекты: студенты, преподаватель, знания
# классы: Teacher, Student, Subject
# Persona - родительский класс для Teacher & Student, self.name, self.surname
# Teacher: to_teach()
# Student: to_take()
# Subject: my_list()


class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name and surname: {self.name} {self.surname}"


class Teacher(Persona):
    def to_teach(self, subject, *students):
        for student in students:
            student.to_take(subject)


class Student(Persona):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge_base = []

    def to_take(self, subject):
        self.knowledge_base.append(subject)


class Subject:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def my_list(self):
        return self.subjects


s = Subject("math", "physics", "python")
t = Teacher("Elena", "Babenko")
print(t)

s_1 = Student("Ivan", "Ivanov")
s_2 = Student("Petr", "Petrov")
s_3 = Student("Vladimir", "Vladimirov")
print(f"s_1: {s_1}, s_2: {s_2}, s_3: {s_3}")

t.to_teach(s, s_1, s_2, s_3)
print(s_1.knowledge_base[0].my_list())
print(s_2.knowledge_base[0].my_list())
print(s_3.knowledge_base[0].my_list())

subj = Subject("chemistry")
t.to_teach(subj, s_1)
print(s_1.knowledge_base)
for knowledge in s_1.knowledge_base:
    print(knowledge.my_list())
for knowledge in s_2.knowledge_base:
    print(knowledge.my_list())
