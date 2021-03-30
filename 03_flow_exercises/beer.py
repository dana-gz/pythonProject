"""
W barze jest 30 L beczka piwa. Kufel piwa kosztuje 11 zł.
Nieuczciwy barman, uznał że może zarobić więcej, dlatego odlał z beczki 1/3 i zastąpił wodą gazowaną.
Następnie napisał "studenckie piwo za 5zł", a pozostałą część sprzedawał jako zwykle piwo za 11zł.
Czy rzeczywiście pomysł mu się udał? Porównaj, co gdyby piwo studenckie było za 6 zł
"""

barrel = 30
pint_price = 11
normal_takings = barrel/2 * pint_price

students_price = 6
cheated_takings = barrel/2 * students_price + 1/3 * barrel/2 * pint_price
cheated_takings_2 = 2/3 * barrel/2 * pint_price + barrel/2 * 2/3 * students_price

print(normal_takings, '-', cheated_takings, '-', cheated_takings_2)
