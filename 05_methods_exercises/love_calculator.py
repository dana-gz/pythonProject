letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's'
           't', 'u', 'v', 'w', 'y', 'z']

lover1 = input('Your name: ')
lover2 = input('Your lover name: ')
love = 'love'
table = []


def preparation(lover1, lover2):
    string = lover1 + lover2 + love
    for i in letters:
        value = string.count(i)
        # jeśli brak jakiejś litery to nie dodaje '0' do tabeli
        if value > 0:
            table.append(value)
    return table


def odds():
    tab = preparation(lover1, lover2)
    a = len(tab)
    while a > 2:
        tab[0] = tab[0] + tab[-1]
        tab.remove(tab[-1])
        a = len(tab)
    # jeśli pierwszy element jest większy lub równy '10' to trzeba dodawanie wykonać do końca
    if tab[0] >= 10:
        num = tab[1] + tab[0]
    # jeśli pierwszy element jest mniejszy niż 10 to jest to cyfra dziesiątek w obliczanym procencie
    else:
        num = tab[1] + 10*tab[0]
    return num

# przykłady wysokiego dopasowania to Jan i Beata lub Max i Iwona;


num = odds()
print('The odds are', num, '%.')
