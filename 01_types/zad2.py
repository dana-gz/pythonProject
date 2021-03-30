# Zadanie 2
# Napisz skrypt, ktory pobiera dwie wiadomosci od uzytkownika
# a nastepnie wyswietla je na ekranie poprzedzone ostrzezeniem "UWAGA: ..."
woj = str(input('Podaj województwo, dla którego przygotowane jest ostrzeżenie pogodowe:'))
pogoda = str(input('Podaj zagrożenia pogodowe które mogą wystąpić na obszarze województwa:'))

woj1 = woj + 'go'

print("UWAGA: \nDla terenu województwa: ", woj1, "mogą wystąpić następujące zjawiska pogodowe:", pogoda, ".\nProsimy o zachowanie ostrożności")