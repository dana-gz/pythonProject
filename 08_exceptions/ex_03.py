#3▹ Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika.
# Obsłuż błędy.

# items = [12.4, 4, 'sun', {'sky': 'niebo'}, True, False, 1 + 2, [], (1, 2, 3), {1,2,3}]
items = [1, 2.3, 0, "lala", {"Marta": 12}, (1, "jojo"), 14, 22222.111, "gimmie", {}, False]

try:
    index = int(input("Give me index 0 - 9:  "))
    my_division = 1 / items[index]
    print("The result: ", my_division)
except (TypeError, ZeroDivisionError) as err:
    print("Error: ", err)
except (ValueError, IndexError) as err:
    print('Incorrect index ->', err)
