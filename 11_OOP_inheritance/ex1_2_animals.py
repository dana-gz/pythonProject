class Animals:
    def __init__(self, name):
        print(name, 'are the most advanced organisms on the planet.')

    def run(self):
        print('run\n', 20 * '*')


class Mammals(Animals):
    def __init__(self, mammal_name):
        print(mammal_name, 'communicate making sounds.')
        print(mammal_name, 'have mammary glands for milk production in females.')
        super().__init__(mammal_name)


    def suck(self):
        print('suck\n', 20 * '*')


class Cat(Mammals):
    def __init__(self, cat_name):
        print(cat_name, 'miaow')
        super().__init__(cat_name)


class Dog(Mammals):
    def __init__(self, dog_name):
        print(dog_name, 'bark')
        super().__init__(dog_name)


class Man(Mammals):
    def __init__(self, man_name):
        print(man_name, 'speak')
        super().__init__(man_name)




man = Man('People')
man.suck()

cat = Cat('Cats')
cat.suck()


dog = Dog('Dogs')
dog.suck()
dog.run()
dog.run()
dog.run()