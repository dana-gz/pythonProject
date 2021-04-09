"""
Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.

    Program zacznie ze stworzonym słownikiem o trzech kluczach:

            marka (str)

            model (str)

            rocznik (int)

    Wypisze ten słownik na ekran (bez żadnego formatowania)

    Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:

        “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”

    Jeśli nie spełnia powyższego warunku, wypisze komunikat:

        “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”

    Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
    aby zobaczyć, czy progam również zmienia swoje zachowanie.
"""


def is_antiquity(car_age):
    if car_age >= 25:
        print(f'Gratulacje! Twój samochód {car["brand"]} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samchód {car["brand"]} jest jeszcze zbyt młody')


car = {'brand': 'renaut', 'model': 'megane', 'year': 1989, 'original_parts': True}
print(car)

car_age = 2021 - car['year']

is_antiquity(car_age)
