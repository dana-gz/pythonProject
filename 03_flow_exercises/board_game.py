"""
W wypożyczalni Gierka za wypożyczenie gry planszowej trzeba zapłacić 8 zł za 3 dni
i dodatkowo po 2,50 zł za każdy kolejny dzień wypożyczenia.
Natomiast w wypożyczalni Planszówka płaci się 12 zł za 3 dni i po 2 zł za każdy kolejny dzień.
Zapytaj użytkownika po jakiej liczbie dni oddał grę, wyświetl w której wypożyczalni byłoby taniej?
"""

days = int(input("Po ilu dniach oddałeś grę? : "))
gierka_cost = 8
planszowka_cost = 12


if days > 3:
    gierka_cost = 8 + (days - 3) * 2.5

if days > 3:
    planszowka_cost = 12 + (days - 3) * 2.5

print(f'Koszt wypożyczenia gry przez {days} dni w wypożyczalnie "Planszówka" to {planszowka_cost} zł.')
print(f'Koszt wypożyczenia gry przez {days} dni w wypożyczalnie "Gierka" to {gierka_cost} zł.')

if planszowka_cost < gierka_cost:
    print('W wypożyczalni "Planszówka" wychodzi taniej.')
elif planszowka_cost > gierka_cost:
    print('W wypożyczalni "Gierka" wychodzi taniej.')
