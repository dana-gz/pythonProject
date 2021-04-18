from h_display import display_hangman


def play(word):
    """the game itself"""
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
        print("Congrats! You guessed the word! You won the game.")

    else:
        print('Sorry, you ran out of tries. The word was ' + word + '. Maybe next time.')
