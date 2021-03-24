import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
           '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']

prize = {'I': '1000 000 zł',
         'II': '3 500 zł',
         'III': '100 zł',
         'IV': '10 zł'
        }

winner = list(prize.keys())
quota = list(prize.values())


your_guess = []
drawed = []
present = []

def guess():
    print('Give 6 numbers for lottery in range 1 - 50: ')
    while len(your_guess) < 6:
        number = input('number: ')
        if not number.isdigit():
            print('It is not a number.')
        elif number not in numbers:
            print('Number must be in range 1 - 50')
        elif number in your_guess:
            print('You have already given this number. Give another one.')
        else:
            your_guess.append(number)


def drawing():
    while len(drawed) < 6:
        draw = random.randrange(0, len(numbers))
        drawed.append(draw)


def checking():
    for i in range(6):
        if your_guess[i] in drawed:
            present.append(your_guess[i])
        i += 1


def summary():
    if len(present) < 3:
        print('Not this time. Try again!')
    elif len(present) == 3:
        print(f'You won {winner[3]} prize - {quota[3]}. Congratulation!')
    elif len(present) == 4:
        print(f'You won {winner[2]} prize - {quota[2]}. Congratulation!')
    elif len(present) == 5:
        print(f'You won {winner[1]} prize - {quota[1]}. Congratulation!')
    elif len(present) == 6:
        print(f'You won {winner[0]} prize - {quota[0]}. Congratulation!')

def main():
    guess()
    drawing()
    checking()
    summary()

main()




