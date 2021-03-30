secret_number = 5
previous_guess = -100


while True:
    user_number = int(input("Give me your guess: "))
    if user_number == secret_number:
        break

    if abs(user_number - secret_number) < abs(previous_guess):
        print('warm!')
        previous_guess = abs(secret_number -user_number)
    else:
        print('cold!')


print("Congratulations - you guessed right!")