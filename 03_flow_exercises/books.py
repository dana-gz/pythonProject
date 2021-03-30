"""
3. Pozwól użytkownikowi wymienić dowolną liczbę książek po przecinku.
Następnie zapytaj użytkownika o ocenę każdej książki w skali od 1-5.
Wyświetl parami tytuł książki - ocena.
"""

books = input("Wymień książki które chciałbyś ocenić: ")
books = books.replace(' ', '')
books = books.split(',')
rates = []
i = len(books)
n = len(books)

for book in range(i):
    rate = int(input(f'Wprowadź ocenę książki {books[i-1]} : '))
    rates.append(rate)
    print(f'{books[i-1]} - rate: {rate}')
    i -= 1

rates.reverse()

while n > 0:
    print(books[n-1], '- ', '*' * rates[n-1])
    n -= 1

