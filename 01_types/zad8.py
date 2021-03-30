# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

pln = int(input("Podaj kwotę pieniędzy którą weźmiesz na wakacje [PLN]:"))
k_eur = 4.4891

eur = int(pln // k_eur)
b_5 = eur // 5
r_5 = eur % 5

b_10 = eur // 10
r_10 = eur % 10

b_20 = eur // 20
r_20 = eur % 20

b_50 = eur // 50
r_50 = eur % 50

print()
print("w przeliczeniu wg średniego kursu EUR podanego przez NBP w dniu 16.02.2021")
print("podana przez Ciebie kwota stanowi równowartość", eur, "EUR.")
print()
print("Kwota ta  może zostać wypłacona jako:")
print (b_5, "banknotów 5 EUR i", r_5, "EUR w monetach,")
print (b_10, "banknotów 10 EUR i", r_10, "EUR w innych nominałach,")
print (b_20, "banknotów 20 EUR i", r_20, "EUR w innych nominałach,")
print (b_50, "banknotów 50 EUR i", r_50, "EUR w innych nominałach.")