#  Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku.
#  Napisz funkcję, która przyjmie wartości i wyświetli średnią.
#  Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

collected_errors = []
err = []
numbers = []

numbers = input('Give some numbers separated by [,]: ')
numbers = numbers.replace(' ', '')
numbers = numbers.replace(',,', ',')
numbers = numbers.split(',')
x_0 = numbers.count('0')
# counter of '0' introduced deliberately

print(x_0)

for i in range(len(numbers)):
    try:
        numbers[i] = int(numbers[i])
    except ValueError:
        numbers[i] = 0
        err.append(1)

print('err', len(err))

numbers_st = []
numbers_st = [str(i) for i in numbers]

print(numbers_st)
print(numbers)
print(len(numbers))

x_00 = numbers_st.count('0')


print(x_0)
print(numbers)



# numbers = [int(i) for i in numbers]
# print(numbers)