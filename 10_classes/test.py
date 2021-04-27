# class Student:
#
#     university = 'New York Academy'
#
#     def __init__(self, name, last, age):
#         self.name = name
#         self.last = last
#         self.age = age
#
#     def email(self):
#         return'{}{}.{}@university.com'.format(university,self.name, self.last)
#
# obj_anna = Student('anna', 'kowalska', 23)
#
# print(obj_anna.email())
# print(Student.email(obj_anna))


class Student:

    university = 'New York Academy'

    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age

    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)


obj_anna = Student('anna', 'kowalska', 23)
print(obj_anna.email)
print(Student.email(obj_anna))
print(obj_anna.university)



class Student:
    # class variable
    stream = "COE"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


# Driver's code
a = Student("Shivam", 3425)
b = Student("Sachin", 3624)
#
# print(a.stream)
# print(b.stream)
print(Student.stream)

print(a.name)
print(a.roll_no)
print(a.stream)
print(b.name)
print(b.roll_no)
print(b.stream)
# Class variables can be accessed
# using class name also

print('\n')
grocery = ['bread', 'milk', 'butter']
for index, value in enumerate(grocery):
    print(index, value)
print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)