currencies = [
                ['BTC', 225188.40],
                ['BCH', 2067.95],
                ['ETH', 6915.50],
                ['USD', 3.8758],
                ['EUR', 4.6141]
            ]

option = input('Wymiana dotyczy: sprzedaży waluty [s] czy zakupu waluty [z]: ')
option = option.lower()
currency_code = input('Podaj kod waluty: ')
currency_code = currency_code.upper()
currency_code = currency_code.replace(' ', '')
currency_amount = int(input('Podaj kwotę waluty: '))


if option == 's':
    for i in range(len(currencies)):
        if currency_code == currencies[i-1][0]:
            print(f'Kurs waluty: 1 {currencies[i-1][0]} - {currencies[i-1][1]} PLN'
                f' - za {currency_amount} {currencies[i-1][0]} otrzymujesz {round(currency_amount*currencies[i-1][1],4)} PLN')
            i += 1


if option == 'z':
    for i in range(len(currencies)):
        if currency_code == currencies[i-1][0]:
            print(f'Kurs waluty: 1 {currencies[i-1][0]} - {currencies[i-1][1]} PLN'
                f' - za {currency_amount} {currencies[i-1][0]} płącisz {round(currency_amount*currencies[i-1][1],4)} PLN')
            i += 1

