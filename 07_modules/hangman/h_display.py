def display_hangman(tries):
    """function displays the game stage"""
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