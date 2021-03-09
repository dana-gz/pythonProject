# 1. Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Elementy na liście posortuj alfabetycznie, a następnie wyświetl.

mountain_trip = ['latarka', 'śpiwór', 'plecak', 'kijki', 'mapa', 'kompas', 'rower']

mountain_trip_sorted = sorted(mountain_trip)
print(' * '.join(mountain_trip_sorted))

# sortowanie w  miejscu
# mountain_trip.sort()
# print(mountain_trip)
# ********************


# # 2. Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
print("Podaj 10 liczb całkowitych.")
numbers_uneven = []
for i in range(10):
    num = int(input("Podaj liczbę:"))
    if num % 2 != 0:
        numbers_uneven.append(num)
print("Liczby nieparzyste  to: ", numbers_uneven)


# 3 Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

# numbers = list(input("Podaj  liczby : "))
#
# if numbers[0] == numbers[-1]:
#     print('pierwszy i ostatni element są takie same')
#
# ********************

# numbers_2 = input("Podaj  liczby po przecinku: ")
# numbers_2 = numbers_2.split(',')
# print(numbers_2)
# print('pierwszy i ostatni element są takie same', numbers_2[0] == numbers_2[-1])
#
# ********************


counter = int(input("\nIle podasz liczb? "))

list_of_numbers = []
for i in range(counter):
    num = float(input("podaj liczbę:"))
    list_of_numbers.append(num)

if list_of_numbers[0] == list_of_numbers[-1]:
    print('pierwszy i ostatni element są takie same')
else:
    print('nie są takie same')


# 4 Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.


counter_1 = int(input("\nIle podasz elementów? "))
while counter_1 % 2 != 0:
    print("Liczba elementów musi  być parzysta.")
    counter_1 = int(input("Ile podasz elementów? "))

elements = []
for i in range(counter_1):
    element = input("Podaj element: ")
    elements.append(element)

mid_el = len(elements) // 2
if elements[mid_el-1] == elements[-mid_el]:
    print("2 środkowe elementy są takie same.")
else:
    print("2 środkowe elementy nie są takie same.")

# 5 Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach
# będzie znajdować się imię, nazwisko, zawód, np:
#     Dorota, Wellman, dziennikarka
#     Adam, Małysz, sportowiec
#     Robert, Lewandowski, piłkarz
#     Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika


people = [
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Krystyna", "Janda", "aktorka"]
]
print(people, "\n")

counter1 = len(people)
for index in range(counter1):
    #   print(' - '.join(row))
    print(index + 1, ' - '.join(people[index]))

print('________________')

for row in people:
    print(row[0], row[1], '-', row[2])


people = (['Dorota', 'Wellman', 'dziennikarka'], ['Adam', 'Małysz', 'sportowiec'], ['Krystyna', 'Janda', 'aktorka'])
