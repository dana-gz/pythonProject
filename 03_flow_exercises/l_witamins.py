"""
2. Stwórz listę witamin. Utwórz drugą listę, która zawiera 2-3 zdania o każdej witaminie.
Napisz pętle, która wyświetli pary witamina - opis.
Np.  "witamina C - ma właściwości przeciw utleniające..."
Czy wiesz jaka struktura pozwoliłaby wygodniej przechować pary klucz wartość?
"""

vitamins = ['a', 'b', 'c', 'd', 'e', 'k']
about_vitamins = ['about a', 'about b', 'about c', 'about d', 'about e', 'about k']
i = len(vitamins)

while i > 0:
    print(f'{vitamins[i-1]} - {about_vitamins[i-1]} ')
    i -= 1

print('************************************************')

vitamins_summary = {
                    'a': 'about a',
                    'b': 'about b',
                    'c': 'about c',
                    'd': 'about d',
                    'e': 'about e',
                    'k': 'about k'
                    }

v = len(vitamins_summary)
v1 = list(vitamins_summary.keys())
v2 = list(vitamins_summary.values())

print(v)

while v > 0:
    print(f'{v1[v-1]} - {v2[v-1]} ')
    v -= 1