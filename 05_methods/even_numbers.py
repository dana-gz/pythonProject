# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów

def even_numbers():
    counter = int(input("How many numbers do you want to enter? "))

    numbers = []
    for i in range(counter):
        number = int(input('Enter a number: '))
        if number % 2 == 0:
            numbers.append(number)
        i += 1
    print(numbers)

# ------ main part ---------


even_numbers()
