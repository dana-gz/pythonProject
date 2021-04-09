# 10.  Użytkownik podaje dowolną liczbę N.
# Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
# Załóżmy, że użytkownik podał N = 8
# Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def squaring(number):
    quadra = {}
    for i in range(number + 1):
        quadra.update({i: i ** 2})
    return quadra


number = int(input('Give a number: '))
print(squaring(number))

# druga wersja

def squaring2():
    entry = int(input('How many entries? : '))
    quadra2 = {}
    for i in range(entry):
        number2 = int(input('Give a number: '))
        quadra2.update({number2: number2 ** 2})
    return quadra2


print(squaring2())
