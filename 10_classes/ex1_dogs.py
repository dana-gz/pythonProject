class Dog:
    def __init__(self, name, bred, age, hair):
        self.name = name
        self.bred = bred
        self.age = age
        self.hair = hair

    def bark(self):
        return 'hau' * self.age

    def frisk(self):
        return 'left - right' * self.age

#
# def bark(counter):
#     return 'hau' * counter
#
#
# dog = {
#     'name': 'Figa',
#     'bred': 'kundelek',
#     'age': 1.5
# }
#


figa = Dog('Figa', 'kundelek', 2, 'brown')
print(figa.name, figa.bred, figa.age, figa.hair)

dyzio = Dog('Dyzio', 'coton de tulear', 4, 'white')
print(dyzio.name, dyzio.bred, dyzio.age, dyzio.hair)

print(figa.bark())
print(dyzio.bark())
print(dyzio.frisk())

print(Dog.bark(dyzio))