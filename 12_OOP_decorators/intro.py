def example_function():

    def nested_function():
        print('Jestem w środku zagnieżdżenia')

    return nested_function


new_function = example_function()

new_function()

print('---------------------------------')


def closure():
    a = "closure"   # obiekt string

    def nested(b):
        return a * b  # instrukcja wykorzystująca obiekt z zakresu

    return nested


new_function = closure()
print(new_function(4))

print('---------------------------------')


def sound_decorator(func_as_param):
    def hau_nested():
        print('Hau ~ hau')
        func_as_param()
    return hau_nested


def pet_func():
    print('Pies to najlepszy przyjaciel człowieka')


pet_func()

print('---------------------------------')

dog = sound_decorator(pet_func)
dog()
dog()

print('---------------------------------')


@sound_decorator
def pet_func():
    print('Pies to najlepszy przyjaciel człowieka')


pet_func()


print('---------------------------------')


def pet_func():
    print('Jorki to małe pieski')


dog = sound_decorator(pet_func)

dog()

print('---------------------------------')


@sound_decorator
def new_pet():
    print('Kupię sobie psa!')


new_pet()
new_pet()


@sound_decorator
def new_pet():
    print('I jeszczę kota!')


new_pet()
