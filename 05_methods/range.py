# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”


def check_range(number, r1, r2):
    if r1 <= number <= r2:
        print(f'Tak, liczba {number} znajduje się w zakresie: {r1} - {r2}')
    elif r2 <= number <= r1:
        print(f'Tak, liczba {number} znajduje się w zakresie: {r2} - {r1}')
    else:
        print(f'Nie, liczba {number} jest poza zasięgiem zakresu.')


def main():
    number = int(input("Podaj liczbę: "))
    r1 = int(input("Podaj liczbę wyznaczająca zakres: "))
    r2 = int(input("Podaj liczbę wyznaczająca zakres: "))
    check_range(number, r1, r2)


main()

