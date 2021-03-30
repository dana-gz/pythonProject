name_1 = input('podaj imię: ')
name_2 = input('podaj imię: ')

if name_1.isalpha():
    print(f'ok {name_1} składa się z liter')
if name_2.isalpha():
    print(f'ok {name_2} składa się z liter\n')

name_1 = name_1.title()
print(name_1)
name_2 = name_2.title()
print(name_2, '\n')

if len(name_1) == len(name_2):
    print('oba imona zawierają tą samą liczbe liter')
else:
    print('imona zawierają różną: liczbe liter\n')

if name_1[0] == name_2[0]:
    print('imiona zaczynają się na tą samą literę')
else:
    print('imiona nie zaczynają się na tą samą literę')
