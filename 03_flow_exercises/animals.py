"""
6. Napisz program, który zawiera listę zwierząt. Poproś użytkownika o 3 zwierzęta, a następnie sprawdź czy:
●	Wprowadzone napisy są zwierzętami z listy
●	Czy zawierają taka samą liczbę liter A
"""

animals = ['dog', 'cat', 'tiger', 'elephant', 'lion', 'zebra', 'cow', 'horse', 'bear', 'crocodile', 'giraffe', 'goat']

animal_1 = input('write an animal: ')
animal_2 = input('write an animal: ')
animal_3 = input('write an animal: ')

animal_x = [animal_1, animal_2, animal_3]

for i in range(len(animal_x)):
    print('occurence of letter "e" -', animal_x[i].count('e'))
    if animals.count(animal_x[i]) > 0:
        print(f'{animal_x[i].title()} is on the list.')
