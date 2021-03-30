import random
from random import randint

# 1. Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).# Następnie powitaj każdą osobę na liście.

names = "Ada, Ola, Grześ, Jula"
names = names.replace(' ', '').split(',')
for n in names:
    print('Hello', n, '!')
print()

# names = "Ania, Jola, Kasia"
# names.replace(" ", "").split(",")
# for n in names:
#     print("Hello ", n)


# 2. Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = input("Wpisz tekst:")

# 2a.
t = len(text)
for n in range(1, t, 2):
    print(text[n])

# 2b.
print(text[1::2])
print()

# 3. W podanym przez użytkownika ciągu wejściowym
# policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

sentence = input("Wpisz zdanie:")
sentence_l = len(sentence)
count_lower = 0
count_upper = 0
count_digit = 0

for i in sentence:
    if i.islower():
        count_lower = count_lower + 1
    elif i.isupper():
        count_upper = count_upper + 1
    elif i.isdigit():
        count_digit = count_digit + 1

count_special = sentence_l - count_lower - count_upper - count_digit

print("małe litery -", count_lower)
print("wielkie litery -", count_upper)
print("cyfry -", count_digit)
print("znaki specjalne -", count_special)
print()


# 5. Stwórz grę ciepło zimno. Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf. Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz. Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.


random_1 = random.randrange(1, 100)
# print(random_1)

guess = int

for i in range(6):
    guess = int(input("podaj liczbę: "))

    if guess == random_1:
        print("zgadłeś !")
        break

    elif (guess - random_1) > 20 or (random_1 - guess) > 20:
        print("zimno")

    elif (guess - random_1) <= 20 or (random_1 - guess) <= 20:
        print("ciepło")

if guess != random_1:
    print("Wygrał komputer.")

print()

# 4 Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur. Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’


summary = 0
try_no = int(input("Podaj liczbę rund w grze: "))
print('Aby zakończyć grę wpisz: stop')

for i in range(try_no):

    gamer = input('papier (p), kamień (k), czy nożyce (n) ? ')
    if gamer == 'stop':
        break
    print('ty:', gamer)

    comp = randint(1, 3)
    if comp == 1:
        comp = 'p'
    elif comp == 2:
        comp = 'k'
    else:
        comp = 'n'
    print('vs:', comp)

    gamer_wins = (gamer == 'k' and comp == 'n') or (gamer == 'p' and comp == 'k') or (gamer == 'n' and comp == 'p')
    comp_wins = (gamer == 'n' and comp == 'k') or (gamer == 'k' and comp == 'p') or (gamer == 'p' and comp == 'n')

    if gamer_wins:
        summary = summary + 1
        print('wygrywasz rundę!')
        if summary > 0:
            print("Wynik gry: Wygrywasz !")
        elif summary < 0:
            print("Wynik gry: Wygrywa komputer !")
        else:
            print("Wynik gry: Remis")
    if comp_wins:
        summary = summary - 1
        print('rundę wygrywa komputer!')
        if summary > 0:
            print("Wynik gry: Wygrywasz !")
        elif summary < 0:
            print("Wynik gry: Wygrywa komputer !")
        else:
            print("Wynik gry: Remis")

    elif gamer == comp:
        print('remis')
        if summary > 0:
            print("Wynik gry: Wygrywasz !")
        elif summary < 0:
            print("Wynik gry: Wygrywa komputer !")
        else:
            print("Wynik gry: Remis")

    elif gamer != 'k' and gamer != 'p' and gamer != 'n' and gamer != 'stop':
        print("ooo chyba pomyłka...")
        if summary > 0:
            print("Wynik gry: Wygrywasz !")
        elif summary < 0:
            print("Wynik gry: Wygrywa komputer !")
        else:
            print("Wynik gry: Remis")
