
# 1. Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”


things = ['plecak', 'narty', 'buty', 'spiwór', 'raki']
# for thing in things:
#     print ("W góry zabieram:", thing)

for index in range(5):
    print("W góry zabieram:", things[index])
print("Great, we are ready!")
print()

for index in things:
    print("W góry zabieram:", index)
print("Great, we are ready!")
print()


# 3. Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

sum_number = 0
for nr in range(1, 11):
    sum_number = sum_number + nr
    if nr == 10:
        print(sum_number)
    else:
        print(sum_number, end=', ')
print()

# 2. Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

ingredients = ['mąka', 'jajka', 'mleko', 'cukier', 'drożdże', 'masło']

for i in range(6):
    print("Dodaj", ingredients[i])
print("Wrzuć do pierkanika")
print("Podawaj schłodzone")
print()


# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

# n = int(input("podaj liczbę:"))
# factorial = 1
# for n in range(1, n+1):
#     factorial = factorial * n
#     print(factorial)


n = int(input("podaj liczbę:"))
factorial = 1
for n in range(1, n+1):
    factorial = factorial * n
    if factorial <= 8:
        print(factorial)
