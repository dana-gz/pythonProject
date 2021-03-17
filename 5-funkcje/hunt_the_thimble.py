# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
import random


def play():
    random_1 = random.randrange(1, 100)
    tries = int(input("Define number of tries: "))
    for i in range(tries):
        guess = int(input("Write number [0] to [100]: "))

        if guess == random_1:
            print("You guessed !")
            break

        elif (guess - random_1) > 20 or (random_1 - guess) > 20:
            print("cold")

        elif (guess - random_1) <= 20 or (random_1 - guess) <= 20:
            print("warm")

    if guess != random_1:
        print("Computer won.")


def hunt_the_thimble():
    play()
    while input("Play again? (Y/N) ").upper() == "Y":
        play()

# -------------- main part -------------


hunt_the_thimble()
