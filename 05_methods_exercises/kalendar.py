# Podpowiedź: Zacznij od funkcji, która wyświetli dni 1 miesiąca.
# Uruchom ją dla każdego elementu listy dane. Pamiętaj, że tydzień ma 7 dni.

data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]
year = len(data)

for month in range(year):
    print(data[month][0], "\n")
    for i in data[month][1]:
        if i < 10 and (i + 1) % 7 != 0:
            print("{:02d}".format(i + 1), '', end='')
        if i == 6:
            print("{:02d}".format(i + 1), '')
        if i >= 10 and (i + 1) % 7 != 0:
            print(i + 1, '', end='')
        if i >= 10 and (i + 1) % 7 == 0:
            print(i + 1, '')
        i += 1
    print("\n")


def days(i):
    for i in data[month][1]:
        if i < 10 and (i + 1) % 7 != 0:
            print("{:02d}".format(i + 1), '', end='')
        if i < 10 and (i + 1) % 7 == 0:
            print("{:02d}".format(i + 1), '')
        if i >= 10 and (i + 1) % 7 != 0:
            print(i + 1, '', end='')
        if i >= 10 and (i + 1) % 7 == 0:
            print(i + 1, '')
    i += 1


def print_calendar():
    for month in range(year):
        print(data[month][0], "\n")
        days(i)
        print("\n")

print_calendar()
