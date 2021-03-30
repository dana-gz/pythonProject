""""
Poprosić użytkownika o podanie zakresu temperatur, które wg niego są optymalne do uprawiania sportów outdoorowych.
Użytkownik powinen podać 2 wartość w jednej linii jako zakres oddzielony znakiem specjalnym np. 16 - 23.
Następnie poproś o podanie aktualnej temperatury na dworze.
Sprawdź czy dziś można uprawiać sport na dworze i wyświetl komunikat - temperatura idealna do uprawiania sportów outdoorowych
/ pogoda nie sprzyja... .
"""

optimal = input('What temperature is good for outdoor sports? Write the lowest and the highest possible separated with - : ')

optimal = optimal.replace(" ","")
optimal = optimal.split("-", 2)

outdoor_temp = int(input('Check the outdoor temperature: '))

if int(optimal[0]) > int(optimal[-1]):
   optimal.sort()

if int(optimal[0]) <= outdoor_temp <= int(optimal[-1]):
    print("The temperature is all right. Go sport !")

x = (int(optimal[-1]) - int(optimal[0]))

if int(optimal[0]) - 0.1 * x <= outdoor_temp < int(optimal[0]):
    print("It could be warmer, but go sport anyway!")

if int(optimal[-1]) < outdoor_temp <= int(optimal[-1]) + 0.1 * x:
    print("It could be colder, but go sport anyway!")