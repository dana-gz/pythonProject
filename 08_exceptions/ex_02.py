# Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd.

items = (1, 0, 'a', 'b', 'test', 4, 6, 7, ['x', 'y'])
collected_errors = []
try:
    index = int(input('Give index number: '))
except ValueError as e:
    result = 0
    collected_errors.append(e)

try:
    value = input('Give index value: ')
except ValueError as e:
    result = 0
    collected_errors.append(e)


try:
    items[index] = value
except (TypeError, NameError) as e:
    result = 1
    collected_errors.append(e)

print(result)

for err in collected_errors:
    print(f' {err}')

