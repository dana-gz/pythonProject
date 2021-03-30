# Poproś użytkownika o wymiary pokoju. Sprawdź czy w pokoju zmieści się duża kanapa.

room = [int(input('Podaj długość pokoju: ')), int(input('Podaj szerokość pokoju: '))]
if room[0] < room[1]:
    room.sort()

settee = [int(input('Podaj długość kanapy: ')), int(input('Podaj szerokość kanpy: '))]
if settee[0] < settee[1]:
    settee.sort()

if room[0] > settee[0] and room[1] > settee[1]:
    print('Kanapa zmnieści się w pokoju.')
else:
    print('Niestety kanapa jest za duża.')
