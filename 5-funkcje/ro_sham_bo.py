# Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

from random import randint


def gamer_turn(gamer):
    print('ty:', gamer)


def comp_turn(comp):
    if comp == 1:
        comp = 'p'
    elif comp == 2:
        comp = 'k'
    else:
        comp = 'n'
    print('vs:', comp)
    return comp


def results(gamer, comp, result):
    # gamer_wins =
    if (gamer == 'k' and comp == 'n') or (gamer == 'p' and comp == 'k') or (gamer == 'n' and comp == 'p'):
        result = 3
    # comp_wins =
    elif (gamer == 'n' and comp == 'k') or (gamer == 'k' and comp == 'p') or (gamer == 'p' and comp == 'n'):
        result = 2
    # draw =
    elif gamer == comp:
        result = 1
    # error =
    elif gamer != ['k', 'p', 'n', 'stop']:
        result = 0
    return result


def round1(result, summary):
    if result == 3:     # gamer_wins:
        summary += 1
        print('wygrywasz rundę!')
    elif result == 2:   # comp_wins:
        summary -= 1
        print('rundę wygrywa komputer!')
    elif result == 1:   # draw:
        print('remis')
    elif result == 0:   # error:
        print("ooo chyba pomyłka...")
    return summary


def summary_result(summary):
    print('----------------------------------------------------')
    if summary > 0:
        print(f'Wynik gry: {summary} - Wygrywasz !')
    elif summary < 0:
        print(f'Wynik gry: {summary} - Wygrywa komputer !')
    else:
        print(f'Wynik gry: {summary} - Remis')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


def main():
    summary = 0
    try_no = int(input("Podaj liczbę rund w grze: "))
    print('Aby zakończyć grę wpisz: stop')

    for i in range(try_no):
        gamer = input('papier (p), kamień (k), czy nożyce (n) ? ')
        gamer = gamer.lower()
        if gamer == 'stop':
            break
        gamer_turn(gamer)
        # comp = randint(1, 3)
        comp = comp_turn(randint(1, 3))
        result = 0
        result = results(gamer, comp, result)
        summary = round1(result, summary)
        summary_result(summary)

# rozpocznij program


main()
