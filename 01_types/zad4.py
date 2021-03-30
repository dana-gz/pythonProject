# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

number_1 = int(input("Podaj dowolną liczbę całkowitą:"))
number_2 = int(input("Podaj kolejną dowolną liczbę całkowitą:"))
number_3 = int(input("Podaj kolejną dowolną liczbę całkowitą:"))

multiplication = number_1 * number_2
division = multiplication / number_3

print()
print("Jeśli pomnożymy", number_1, "przez", number_2, "otrzymamy", multiplication,"." )
print("Jeśli następnie, otrzymany wynik mnożenia podzielimy przez", number_3, "otrzymamy", division, ".")