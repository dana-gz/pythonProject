# Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

from random import randint

elements = ['p', 'k', 'n', 'l', 's', 'q']
names = ['paper', 'stone', 'scissors', 'lizard', 'spock']


def gamer_turn(gamer):
    print('you:', gamer)


def comp_turn(comp):
    if comp == 1:
        comp = 'p'
    elif comp == 2:
        comp = 'k'
    elif comp == 3:
        comp = 'n'
    elif comp == 4:
        comp = 'l'
    else:
        comp = 's'
    print('vs:', comp)
    return comp


def results(gamer, comp, result):
    # gamer_wins =
    if (gamer == 'k' and comp == 'n') or (gamer == 'p' and comp == 'k') or (gamer == 'n' and comp == 'p') \
            or (gamer == 'k' and comp == 's') or (gamer == 'p' and comp == 'l') or (gamer == 'n' and comp == 's')\
            or (gamer == 's' and comp == 'l') or (gamer == 's' and comp == 'p') or (gamer == 'l' and comp == 'n')\
            or (gamer == 'l' and comp == 'k'):
        result = 3
    # comp_wins =
    elif (gamer == 'n' and comp == 'k') or (gamer == 'k' and comp == 'p') or (gamer == 'p' and comp == 'n') \
            or (gamer == 's' and comp == 'k') or (gamer == 'l' and comp == 'p') or (gamer == 's' and comp == 'n')\
            or (gamer == 'l' and comp == 's') or (gamer == 'p' and comp == 's') or (gamer == 'n' and comp == 'l')\
            or (gamer == 'k' and comp == 'l'):
        result = 2
    # draw =
    elif gamer == comp:
        result = 1
    # error =
    elif gamer != elements:
        result = 0
    return result


def round1(result, summary):
    if result == 3:     # gamer_wins:
        summary += 1
        print('You win the round!')
    elif result == 2:   # comp_wins:
        summary -= 1
        print('Computer wins the  round!')
    elif result == 1:   # draw:
        print('Draw')
    elif result == 0:   # error:
        print("Something went wrong..")
    return summary


def summary_result(summary):
    print('----------------------------------------------------')
    if summary > 0:
        print(f'Game result: {summary} - You win !')
    elif summary < 0:
        print(f'Game result: {summary} - Computer wins !')
    else:
        print(f'Game result: {summary} - Draw ')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


def game(level, try_no):
    summary = 0
    for i in range(try_no):
        text = ''
        for j in range(level):
            text += names[j] + ' (' + elements[j] + ') '
        gamer = input(text)
        gamer = gamer.lower()

        if gamer == 'q':
            break
        gamer_turn(gamer)
        comp = comp_turn(randint(1, level))
        result = 0
        result = results(gamer, comp, result)
        summary = round1(result, summary)
        summary_result(summary)


def main():
    try_no = ''
    while type(try_no) != int:
        try:
            try_no = int(input("Give the number of rounds in the game: "))
        except ValueError:
            print("Value must be a number")

    print('S - Start')
    print('P - Difficulty level')
    print('Q - Quit')
    level = input('high (h), low (l) : ').lower()
    while level != 'l' and level != 'h':
        level = input('high (h), low (l) : ').lower()
    if level == 'l':
        game(3, try_no)
    elif level == 'h':
        game(5, try_no)


# rozpocznij program


main()
