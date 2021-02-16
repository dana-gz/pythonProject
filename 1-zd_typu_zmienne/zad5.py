# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 

number_1 = int(input("Podaj dowolną liczbę:"))
number_2 = int(input("Podaj kolejną liczbę:"))

division = number_2 // number_1
rest = number_2 % number_1

print()
print(number_1, "mieści się", division, "w", number_2)
print("Reszta z tego dzielenia wynosi", rest)