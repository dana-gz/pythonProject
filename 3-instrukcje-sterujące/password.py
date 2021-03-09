# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.


#  tylko  1b i 3  działają ale  odpytują  krok po  kroku
#  - 1a, 2 i 4 mają  problem, który  pokazałam na screenach w mailu - dlaczego?


# 1a

password = input('wpisz hasło:')

length_correct = len(password) >= 8
includes_letters_and_digits = password.isalnum() and not password.isdigit() and not password.isalpha()
at_least_one_capital_letter = not password.islower()

if not length_correct:
    print("Hasło musi mieć długość conajmniej 8 znaków")

if not includes_letters_and_digits:
    print("Hasło musi składać się z liter i cyfr")

if not at_least_one_capital_letter:
    print("Hasło musi zawierać conajmniej 1 dużą literę")

else:
    print("Hasło zostało utworzone")


# 1b

password = input('wpisz hasło:')

length_correct = len(password) >= 8
includes_letters_and_digits = password.isalnum() and not password.isdigit() and not password.isalpha()
at_least_one_capital_letter = not password.islower()

if not length_correct:
    print("Hasło musi mieć długość conajmniej 8 znaków")

elif not includes_letters_and_digits:
    print("Hasło musi składać się z liter i cyfr")

elif not at_least_one_capital_letter:
    print("Hasło musi zawierać conajmniej 1 dużą literę")

else:
    print("Hasło zostało utworzone")


# 2.
"""
password = input('wpisz hasło:')

if len(password) < 8:
    print("Hasło musi mieć długość conajmniej 8 znaków")
if password.islower():
    print("Hasło musi zawierać conajmniej 1 dużą literę")
if password.isalpha() or password.isdigit() or (not password.isalnum()):
        print("Hasło musi składać się z liter i cyfr")
else:
    print("Hasło zostało utworzone")
"""

# 3.

# password = input('wpisz hasło:')
#
# if len(password) >= 8:
#     if password.isdigit() == False and password.isalpha() == False:
#         if password.islower() == False:
#             print("Hasło zostało utworzone")
#         else:
#             print("Hasło musi zawierać conajmniej 1 dużą literę")
#     else:
#         print("Hasło musi zawierać litery, cyfry i conajmniej 1 dużą literę")
# else:
#     print("Hasło musi mieć długość conajmniej 8 znaków")


# 4.
"""
password = input('wpisz hasło:')

if len(password) < 8:
    print("długość conajmniej 8 znaków")
if password.islower():
    print("conajmniej 1 dużą literę")
if password.isalpha():
    print("Hasło powinno składać z liter i cyfr")
elif password.isdigit():
    print("Hasło powinno składać z liter i cyfr")
elif (not password.isalnum()):
    print("Hasło powinno składać z liter i cyfr")
else:
    print("hasło utworzone")
"""
