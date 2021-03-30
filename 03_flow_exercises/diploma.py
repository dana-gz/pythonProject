"""
Tekst 1 strony A4 to 2500 znaków i około 300 słów.
Praca dyplomowa powinna zajmować co najmniej 25 str A4.
Użytkownik programu podaje jakiego przelicznika użyje - znaki czy słowa. Następnie program pyta:
"Ile {znaków/slow} pracy dyplomowej do tej pory napisałeś?". Użytkownik odpowiada.
●	Dla liczby stron mniejszej niż 20, komputer wyświetla: "tak mało? masz jeszcze {liczba stron} do napisania".
●	Dla liczby 20-25 stron powinni pojawić hasło dopingujące "niewiele brakuje, walcz dalej"
●	Dla liczby powyżej 25 stron - gratulacje ;D.
"""

your_pages = 0
conversion_factors = ['character', 'word']

conversion_factor = input('Choose conversion factor: character[ch] or word[w]: ')
if conversion_factor == 'ch':
    characters = int(input('How many characters have written so far?: '))
    your_pages = characters / 2500
    pages_left = 25 - your_pages
    if your_pages < 20:
        print(f'Too little. You have still {pages_left} to be written')
    if 20 <= your_pages < 25:
        print('Keep up, go on')
    if your_pages >= 25:
        print('Congratulation! Good job!')

if conversion_factor == 'w':
    words = int(input('How many words have written so far?: '))
    your_pages = words / 300
    pages_left = 25 - your_pages
    if your_pages < 20:
        print(f'Too little. You have still {pages_left} to be written')
    if 20 <= your_pages < 25:
        print('Keep up, go on')
    if your_pages >= 25:
        print('Congratulation! Good job!')
