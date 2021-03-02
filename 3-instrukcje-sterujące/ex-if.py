# 1. Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat
# “Twoja liczba jest podzielna przez 3”.

number = int(input("podaj liczbę: "))
if number % 3 == 0:
    print("Twoja liczba jest podzielna przez 3")
else:
    print(number, 'nie jest podzielne przez 3')
print()

# 3. Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. 
# W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

rate_1 = int(input("podaj ocenę 1-10: "))
rate_2 = int(input("podaj ocenę 1-10: "))
rate_3 = int(input("podaj ocenę 1-10: "))

rate = (rate_1 + rate_2 + rate_3) / 3

if rate > 7:
    print("bardzo dobra")
elif rate >= 5:
    print("przeciętna")
else:
    print("nie warta uwagi")
print()

# 5. w pliku password

# 2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

number_1 = int(input("podaj liczbę całkowitą:"))
number_2 = int(input("podaj kolejną liczbę całkowitą:"))

the_sum = number_1 + number_2

if the_sum > 100:
    print("wynik:", the_sum)
else:
    print("Koniec")
print()

# 4. Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

signs = input("wpisz ciąg znaków: ")

if len(signs) > 5:
    signs = signs.replace('a', 'z')
    print(signs)
else:
    print("mniej niż 5 znaków")
print()

# 6. Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

number_x = 75
number_y = int(input("Podaj numer od 1 do 100: "))

if number_y == number_x:
    print("gratulacje!")
else:
    print("pudło!")
print()

# 7. Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli
# w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

correct_bmi = (18.5, 24.99)
overweight_bmi = (25, 29.99)

weigh = int(input('Podaj swoją wagę w [kg]:'))
height_cm = int(input('Podaj swój wzrost w [cm]:'))
height_m = height_cm / 100
your_bmi = weigh / (height_m ** 2)
your_bmi_rounded = round(your_bmi, 2)
print('Twoje BMI to:', your_bmi, '.')
print('Twoje BMI po zaokrągleniu to:', your_bmi_rounded, '.')

# if your_bmi >= 18.5 and your_bmi < 25:
if your_bmi == correct_bmi:
    print("waga prawidłowa")
if your_bmi == overweight_bmi:
    print("nadwaga")
if your_bmi >= 30:
    print("otyłość")


# 8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

number_a = int(input("podaj liczbę: "))
number_b = int(input("podaj liczbę: "))
number_c = int(input("podaj liczbę: "))

# 8.1
abc = (number_a, number_b, number_c)
abc_sorted = sorted(abc)
print(abc_sorted)

# 8.2
if number_a > number_b:
    number_a, number_b = number_b, number_a

if number_a > number_c:
    number_a, number_c = number_c, number_a

if number_b > number_c:
    number_b, number_c = number_c, number_b

print(number_a, number_b, number_c)
