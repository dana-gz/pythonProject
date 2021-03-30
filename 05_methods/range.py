# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”

#WYSYPUJE  SIE....

def numbers():
    number = int(input("Podaj liczbę: "))
    range_end1 = int(input("Podaj liczbę wyznaczająca zakres: "))
    range_end2 = int(input("Podaj liczbę wyznaczająca zakres: "))
    r1 = range(range_end1, range_end2)
    r2 = range(range_end2, range_end1)
    return number, r1, r2



def check_range(number, r1, r2):
    if number in r1:
        print(f'tak, liczba {number} znajduje się w zadanym zakresie')

    elif number in r2:
        print(f'tak, liczba {number} znajduje się w żądanym zakresie')

    else:
        print (f'nie, liczba {number} jest poza zasięgiem zakresu')


def main():
    numbers()
    check_range()



main()

