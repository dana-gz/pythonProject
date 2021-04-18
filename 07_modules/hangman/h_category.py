import random


def categories(catt):
    """reading the words from a file"""
    filename = 'words.txt'
    try:
        with open(filename, 'r') as fopen:
            lines = fopen.readlines()
    except FileNotFoundError:
        print('File not found. Try again ;) ')
        quit()

    animals4 = []
    birds2 = []
    flowers0 = []
    line = []
    # word = category(animals, birds, flowers)
    for j in range(len(lines)):
        animals4 = lines[4].split(", ")
        birds2 = lines[2].split(", ")
        flowers0 = lines[0].split(", ")

    if catt == 'a':
        line = animals4[1:-1]
    elif catt == 'b':
        line = birds2[1:-1]
    elif catt == 'f':
        line = flowers0[1:-1]
    return line


def category(animals, birds, flowers):
    """choosing a category and a random word"""
    catt = input("Choose the category: animals [a], birds [b], flowers [f]: ").lower()
    while catt != 'a' and catt != 'b' and catt != 'f':
        print('Check the input')
        catt = input("Choose the category: animals [a], birds [b], flowers [f]: ").lower()
    line = []
    line = categories(catt)
    word = ''
    word = random.choice(line)
    return word.upper()
