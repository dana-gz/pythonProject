# print(property())
# print(property().getter)
# print(property().setter)
# print(property().deleter)

class Student:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age
        self.email = name + '.' + last + '@university.com'

    def