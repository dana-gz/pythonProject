"""
Standardowe limity prędkość wynoszą odpowiednio:
●	na autostradzie – 140 km/h,
●	na drodze ekspresowej dwujezdniowej – 120 km/h,
●	na drodze ekspresowej jednojezdniowej – 100 km/h,
●	na drodze jednojezdniowej dwukierunkowej – 90 km/
●	w terenie zabudowanym - 50 km/h
Poproś użytkownika o podanie dowolnej prędkości, a następnie wyświetl na jakiej drodze na pewno się nie porusza
(zgodnie z prawem).
Np. input: 112
Nie znajduje się po terenie zabudowany
Nie znajduje się po drodze dwujezdniowej
Nie znajduje się na drodze ekspresowej jednojezdniowej
"""

speed_limits = {
                50: 'w terenie zabudowanym',
                90: 'na drodze jednojezdniowej dwukierunkowej',
                100: 'na drodze ekspresowej jednojezdniowej',
                120: 'na drodze ekspresowej dwujezdniowej',
                140: 'na autostradzie'
               }

your_speed = int(input("Z jaką prędkością jedziesz?: "))

speed_limit = list(speed_limits.keys())
road = list(speed_limits.values())


for i in range(len(speed_limit)):
    if your_speed > speed_limit[i]:
        print(f'- Nie znajdujesz się {road[i]}')
        i += 1
