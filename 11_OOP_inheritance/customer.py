import datetime as t


class Customer:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def register(self):
        days = len(self.name) + len(self.surname)
        today = t.datetime.today()
        register_at = today + t.timedelta(days)
        return register_at.strftime('%d-%m-%Y')


if __name__ == '__main__':
    user = Customer('John', 'Black', 'johny@gmail.com')
    print(user.register())


