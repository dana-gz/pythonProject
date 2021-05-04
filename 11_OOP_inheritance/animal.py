class Animals:
    def __init__(self):
        print("I'm animal")

    def eat(self):
        print('am am am')

class Warm_blooded(Animals):
    def lie(self):
        print('I lie in the sun')

class Dog(Warm_blooded):
    def __init__(self):
        print("I'm Dog")

    def lie(self):
        print('-------')
        super().lie()
        print('I lie on the settee')

    def eat(self):
        print('I dig in')


dyzio = Dog()
dyzio.eat()
dyzio.lie()
print('\n')

s = Warm_blooded()
s.eat()
s.lie()