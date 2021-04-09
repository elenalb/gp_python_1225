# стандартные атрибуты и методы
# __name__
# __module__
# __dict__
# etc


class User:
    """
    class User contains info about user
    """
    def __init__(self, name, login, password, email):
        self.name = name
        self.login = login
        self.password = password
        self.email = email

    def get_data(self):
        print(f"Имя: {self.name}, логин: {self.login}, "
              f"пароль: {self.password}, почта: {self.email}")


u = User("Ivan", "ivan1999", "1q2w3e", "ivan@gmail.com")
u.get_data()
print(f"__name__: {User.__name__} \n__module__: {User.__module__} \n"
      f"__dict__: {User.__dict__} \n__doc__: {User.__doc__} \n"
      f"__init__: {User.__init__} \n__class__: {User.__class__}")
