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
currency_amount = float(input('Podaj kwotę waluty: '))


if option == 's':
    for i in range(len(currencies)):
        if currency_code == currencies[i-1][0]:
            quota = round(currency_amount*currencies[i-1][1], 4)
            print(f'Kurs waluty: 1 {currencies[i-1][0]} - {currencies[i-1][1]} PLN'
                  f' - za {currency_amount} {currencies[i-1][0]} otrzymujesz {quota} PLN')

            banknot_100 = int(quota // 100)
            banknot_50 = int((quota - banknot_100 * 100) // 50)
            banknot_20 = int((quota - banknot_100 * 100 - banknot_50 * 50) // 20)
            banknot_10 = int((quota - banknot_100 * 100 - banknot_50 * 50 - banknot_20 * 20) // 10)
            rest = quota - banknot_100 * 100 - banknot_50 * 50 - banknot_20 * 20 - banknot_10 * 10
            rest = round(rest, 2)
            exchange = {
                        '100 PLN': banknot_100,
                        '50 PLN': banknot_50,
                        '20 PLN': banknot_20,
                        '10 PLN': banknot_10,
            }
            banknots = list(exchange.keys())
            money = list(exchange.values())
            for m in range(len(money)):
                if money[m-1] == 1:
                    print("otrzymujesz", money[m-1], "banknot", banknots[m-1])
                elif 1 < money[m-1] < 5:
                    print("otrzymujesz", money[m-1], "banknoty", banknots[m-1])
                elif money[m-1] >= 5:
                    print("otrzymujesz", money[m-1], "banknotów", banknots[m-1])
                m += 1
            print(f'i {rest} PLN w monetach.')
            i += 1

if option == 'z':
    for i in range(len(currencies)):
        if currency_code == currencies[i-1][0]:
            print(f'Kurs waluty: 1 {currencies[i-1][0]} - {currencies[i-1][1]} PLN'
                  f' - za {currency_amount} {currencies[i-1][0]} płącisz '
                  f'{round(currency_amount*currencies[i-1][1],4)} PLN')
            i += 1
