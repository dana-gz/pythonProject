from h_category import category
from h_play import play


def main():
    """the game category is called from h_category, the game itself is called from h_play - the function play(),
    module h_displays is imported by h_play module and displays stage of the game"""
    animals = []
    birds = []
    flowers = []

    word = category(animals, birds, flowers)

    play(word)

    again = input("Play again? (Y/N): ").upper()
    while again != "Y" and again != "N":
        print('Check the input')
        again = input("Play again? (Y/N): ").upper()

    if again == 'Y':
        word = category(animals, birds, flowers)
        play(word)
    else:
        quit()


if __name__ == "__main__":
    main()
