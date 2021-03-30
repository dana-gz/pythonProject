""""
Poprosić użytkownika o podanie zakresu temperatur, które wg niego są optymalne do uprawiania sportów outdoorowych.
Użytkownik powinen podać 2 wartość w jednej lini jako zakres oddzielony znakiem specjalnym np. 16 - 23.
Następnie poproś o podanie aktualnej temperatury na dworze.
Sprawdź czy dziś można uprawiać sport na dworze i wyświetl komunikat - temperatura idealna do uprawiania sportów outdoorowych
/ pogoda nie sprzyja... .
"""

optimal = input('What temperature is good for outdoor sports? Write the lowest and the highest possible separated with - : ')

optimal.replace(" ","")
optimal = optimal.split("-", 2)
print(optimal)
lowest = int(optimal[0])
print(lowest)
highest = int(optimal[-1])
print(highest)


if highest < lowest:
    h = highest
    l = lowest
    highest = l
    lowest = h

outdoor_temp = int(input('check the outdoor temperature: '))

for i in range(lowest, highest):
    i += 1
    if i == outdoor_temp:
        print("The temperature is all right - Go sport")

# under_l = int(round(optimal[0]) * 0.9)
# above_h = int(round(optimal[-1]) * 1.1)
#
#
# for i in range(highest, above_h):
#     i += 1
# if i == outdoor_temp:
#         print("The temperature could be colder but you can - go sport anyway")
#
# for i in range(under_l, lowest):
#     i += 1
#     if i == outdoor_temp:
#         print("The temperature could be warmer but you can - go sport anyway")
#
# if outdoor_temp > above_h:
#     print("It's too hot for outdoor sports.")
#
# if outdoor_temp < under_l:
#     print("It's too cold for outdoor sports.")


