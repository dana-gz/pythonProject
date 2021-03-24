"""
Poproś użytkownika o podanie kilku imion. Przerwij, gdy użytkownik poda literę "Q"
Wyświetl każde imię dodając hello!
Zwróć uwagę, że imiona powinny składać się conajmniej z 3 liter, jeśli imię jest krótsze wyświetl "to nie jest imię"
"""
names = []
for i in range(5):
    name = input("Wpisz imię: ")
    print('Hello', name)
    names.append(name)
    if name == 'Q':
        break
    if len(name) < 3:
        print("To nie jest imię!")

print(names)

