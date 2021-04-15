#  Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku.
#  Napisz funkcję, która przyjmie wartości i wyświetli średnią.
#  Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def to_int():
    for i in range(len(numbers)):
        try:
            numbers[i] = int(numbers[i])
        except ValueError as e:
            numbers[i] = 0
            err.append(1)
            collected_errors.append(e)
    return numbers, err, collected_errors

collected_errors = []
err = []

numbers = input('Give some numbers separated by [,]: ')
numbers = numbers.replace(' ', '')
numbers = numbers.replace(',,', ',')
numbers = numbers.split(',')

to_int()

valid_items = len(numbers) - len(err)
# number of all items ('0' for error included) -  number of '0' for error
# for calculating the mean - errors are not taken into account

# the_mean = mean_value()
# print(the_mean)

summ = 0
for i in range(len(numbers)):
    summ += numbers[i]
mean = summ / valid_items
print('The mean is: ', mean)

