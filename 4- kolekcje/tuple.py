# 1. Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie
# np. “Mój pies, rasy border collie wabi się Dyzio”.

my_pet = ('pies', 'mieszaniec', 'Rocky')

type_of_pet, race, name = my_pet

sentence = f"Mój {my_pet[0]}, rasy {my_pet[1]} wabi się {my_pet[2]}."
print(sentence, "\n")

# 2. Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

pets = ('dog', 'cat', 'hamster', 'cat', 'cat', 'dog', 'canary')

all_pets = len(pets)
for i in range(all_pets):
    pets.count(pets[i])
    if pets.count(pets[i]) > 1 and pets[i] != pets[i > 1]:
        print(pets[i], 'x', pets.count(pets[i]))
    i += 1
print()


# 3. Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.

my_munbers = (1, 3, 44, 5, 66, 6, 9)
your_number = int(input('Podaj liczbę całkowitą: '))

x = len(my_munbers)
for i in range(x):
    if my_munbers[i] == your_number:
        print('Twoja liczba ma indeks ', my_munbers.index(your_number), "\n")
    i += 1
