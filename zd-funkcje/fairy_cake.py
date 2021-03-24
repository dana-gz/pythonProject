features = {'a': 'spryciarz', 'b': 'spóźnialski', 'c': 'naerwus', 'd': 'leniuszek', 'e': 'kujon','f': 'pedant',
            'g': 'cwaniak', 'h': 'flirciarz', 'i': 'obibok', 'j': 'szaleniec', 'k': 'maniak selfie',
            'l': 'perfekcjonista', 'm': 'czekoladoholik', 'n': 'wredota', 'o': 'poważny', 'p': 'nieogar',
            'r': 'złośliwiec', 's': 'urodzony geniusz', 't': 'śpioch', 'u': 'uparciuch', 'w': 'śmieszek',
            'm': 'marzyciel'}

letters = list(features.keys())
feature = list(features.values())


def augury():
    name = input('Jak masz na imię?: ')
    letter = name[0]
    letter = letter.lower()
    x = letters.index(letter)

    print(f'Twoje imię zaczyna się na literę {name[0]}. Twoja cecha wiodąca to - {feature[x]}')

augury()

while input("Play again? (Y/N)").upper() == "Y":
    augury()




