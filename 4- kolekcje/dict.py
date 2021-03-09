# 1 Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik dict_from_list.

list_to_dict = [
    ['aaa', 'a1'],
    ['bbb', 'b1'],
    ['ccc', 'c1']
]

dict_from_list = dict(list_to_dict)
print(dict_from_list)


# 2 Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe. Przekształć ją w słownik dict_from_tuples.

tuples_to_dict = (
                (1, 11),
                ("1a", "11a"),
                (2, 22),
                ("2a", "22a"),
                (3, 33),
                ("3a", "33a")
                )
dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)

# 3 Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją

n = int(input("\nGive me the number of row & columns N = "))
tab = [['-'] * n] * n

for row in tab:
    print(' '.join(row), "\n")

# 4. Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.

x = 1
y = 1
for x in range(1, 11):
    while y <= 10:
        print("{:3}".format(x * y), end=" ")
        y += 1
    y = 1
    print("\n")

# 5 W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
# Zadbaj o sposób wyświetlania np.:
#     szybko : 5
#     zbudź : 1

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""


poem = poem.lower()
poem = poem.replace(',', '')
poem = poem.split()


poem_dict = {}
for word in poem:
    if word in poem_dict:
        poem_dict[word] += 1
        ...
    else:
        poem_dict[word] = 1

for key, value in poem_dict.items():
    print(key, ':', value)


# 6. Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.
# >>> days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
days_l = list(days.values())
months_l = list(days.keys())
days_and_months = months_l + days_l

months_days_shorted = []
for i in days_and_months:
    if i not in months_days_shorted:
        months_days_shorted.append(i)
print("\n", months_days_shorted, "\n")


# 7. Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
# >>>  example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

shorted_list = []
for i in example_list:
    if i not in shorted_list:
        shorted_list.append(i)

shorted_tuple = tuple(shorted_list)
print(shorted_tuple, "\n")
print("min value element : ", min(shorted_tuple))
print("max value element : ", max(shorted_tuple))

# 8. Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

Denmark = ['Ida', 'Emma', 'Alma', 'Ella', 'Sofia', 'Freja', 'Josefine', 'Clara', 'Anna', 'Karla']
England = ['Olivia', 'Amelia', 'Emily', 'Isla', 'Ava', 'Jessica', 'Isabella', 'Lily', 'Ella', 'Mia']
Finland = ['Aino', 'Aada', 'Sofia', 'Eevi', 'Olivia', 'Lilja', 'Helmi', 'Ellen', 'Emilia', 'Ella']
France = ['Emma', 'Louise', 'Jade', 'Alice', 'Chloé', 'Lina', 'Mila', 'Léa', 'Manon', 'Rose']
Germany = ['Mia', 'Emma', 'Hanna', 'Sofia', 'Anna', 'Emilia', 'Lina', 'Marie', 'Lena', 'Mila']
Greece = ['Maria', 'Eleni', 'Aikaterini', 'Vasiliki', 'Sophia', 'Angeliki', 'Georgia', 'Dimitra', 'Konstantina',
          'Paraskevi']
Hungary = ['Hanna', 'Anna', 'Jázmin', 'Lili', 'Zsófia', 'Emma', 'Luca', 'Boglárka', 'Zoé', 'Nóra']
Ireland = ['Emily', 'Emma', 'Ava', 'Sophie', 'Amelia', 'Ella', 'Lucy', 'Grace', 'Chloe', 'Mia']
Italy = ['Sofia', 'Giulia', 'Aurora', 'Alice', 'Ginevra', 'Emma', 'Giorgia', 'Greta', 'Beatrice', 'Anna']
Poland = ['Zuzanna', 'Julia', 'Lena', 'Maja', 'Hanna', 'Zofia', 'Amelia', 'Alicja', 'Aleksandra', 'Natalia']

forenames = Denmark + England + Finland + France + Greece + Germany + Hungary + Italy + Ireland + Poland
names_selected = []

fn = len(forenames)
for i in range(fn):
    forenames.count(forenames[i])
    if forenames.count(forenames[i]) > 2 and forenames[i] not in names_selected:
        names_selected.append(forenames[i])
print('\n', names_selected, '\n')


# 9. 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

subjects = []

for n in range(5):
    print("Podaj 4 przedmioty szkolne: ")
    for i in range(4):
        subject = input("przedmiot szkolny: ")
        subject = subject.lower()
        subjects.append(subject)
    print("Dziękuję! \n")
print(subjects)


popularity = []
for i in range(20):
    subjects.count(subjects[i])
    popularity.append(subjects.count(subjects[i]))
    i += 1


maxi = []
for i in range(20):
    subjects.count(subjects[i])
    if subjects.count(subjects[i]) == max(popularity) and subjects[i] not in maxi:
        maxi.append(subjects[i])
        i += 1

print(maxi)


# 10.  Użytkownik podaje dowolną liczbę N.
# Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
# Załóżmy, że użytkownik podał N = 8
# Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# może później idę spać  :)...
