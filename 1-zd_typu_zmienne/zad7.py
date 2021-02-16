# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

pln = int(input("Podaj kwotę pieniędzy którą weźmiesz na wakacje [PLN]:"))
k_usd = 3.6940
k_eur = 4.4891

usd = int(pln // k_usd)
eur = int(pln // k_eur)

print()
print("w przeliczeniu wg średnich kursów walut podanych przez NBP z dnia 16.02.2021")
print("podana przez Ciebie kwota stanowi równowartość", usd, "USD lub", eur, "EUR.")

