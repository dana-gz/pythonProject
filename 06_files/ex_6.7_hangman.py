import random


def category(animals, birds, flowers):
    cat = input("Choose the category: animals [a], birds [b], flowers [f]: ").lower()
    if cat == 'a':
        word = random.choice(animals)
    elif cat == 'b':
        word = random.choice(birds)
    elif cat == 'f':
        word = random.choice(flowers)

    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Lets play hangman')
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input('Guess a letter or a word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter.", guess)

            elif guess not in word:
                tries -= 1
                print(guess, 'is not in the word.')
                guessed_letters.append(guess)

            else:
                print('Excelent', guess, 'is in the word.')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '-' not in word_completion:
                    guessed == True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed the word', guess)

            elif guess != word:
                print(guess, 'is not in the word.')
                tries -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(word_completion)
        print('\n')

    if guessed:
        print("Congrats,  you guessed the word! You won the game")

    else:
        print('Sorry, you ran  out of tries. The word was' + word + 'Maybe next time.')


def display_hangman(tries):
    stages = []

    stages = ['''
                   +---+
                    O   |
                   /|\  |
                   / \  |
                  ===''', '''
                    +---+
                    O   |
                   /|\  |
                   /    |
                      ===''', '''
                    +---+
                     O  |
                    /|\ |
                     |
                      ===''', '''
                    +---+
                     O  |
                    /|  |
                     |
                      ===''', '''
                    +---+
                     O |
                     | |
                       |
                      ===''', '''
                    +---+
                     O |
                       |
                       |
                       ===''', '''
                    +---+
                        |
                        |
                        |
                        ==='''
              ]
    return stages[tries]


filename = 'words.txt'
with open(filename, 'r') as fopen:
    lines = fopen.readlines()

animals = []
birds = []
flowers = []

for j in range(len(lines)):
    animals4 = lines[4].split(", ")
    animals = animals4[1:-1]
    birds2 = lines[2].split(", ")
    birds = birds2[1:-1]
    flowers0 = lines[0].split(", ")
    flowers = flowers0[1:-1]


def main():
    word = category(animals, birds, flowers)
    play(word)

    while input("Play again? (Y/N)").upper() == "Y":
        word = category(animals, birds, flowers)
        play(word)


if __name__ == "__main__":
    main()
