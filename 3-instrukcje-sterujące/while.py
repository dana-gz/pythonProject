
cookies = 5
while cookies > 0:
    print('Zjedz ciastko')
    cookies = cookies - 1
    print('Zostało jeszcze ', cookies)
    print('---------------------------')

print('\nNo nie, znowu trzeba kupić ciastka!')


# 1. Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# vNapisz rozwiązanie zarówno z użyciem pętli while jak i for.

F = 0
while F < 201:
    F = F + 20
    print(5/9 * (F - 32), "stopni C")
print()

temp_F = 0
while temp_F < 201:
    temp_C = (5.0/9.0) * (temp_F - 32)
    print('Temperatura w F =', temp_F, 'na C to:', round(temp_C, 2))
    temp_F = temp_F + 20
print()

# 2. Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_number = 7
your_guess = int(input("Zgadnij o jaką liczbę chodzi:"))
while secret_number != your_guess:
    print(your_guess, "- to nie ta liczba")
    your_guess = int(input("Podaj liczbę:"))
    if secret_number == your_guess:
        print("Zgadłeś!")
