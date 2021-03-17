# Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb.
# minimum_of(a, b, c).

def maximum_of():
    number_a = int(input('Write number: '))
    number_b = int(input('Write number: '))
    number_c = int(input('Write number: '))

    if number_a < number_b:
        number_a, number_b = number_b, number_a

    if number_a < number_c:
        number_a, number_c = number_c, number_a

    if number_b < number_c:
        number_b, number_c = number_c, number_b

    numbers = [number_a, number_b, number_c]

    maximum = numbers[0]

    print(f'Maksymalna wartość to {number_a}')

# ------ main part ----------


maximum_of()
