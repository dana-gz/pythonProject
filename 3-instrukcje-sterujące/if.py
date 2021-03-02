# dish ="gzik"   # -error
# if dish == "pyzy"
#     reg = "wkp"
# print(reg)


balance = int(input('wpisz saldo:'))

if balance >= 5:
    print('Możesz kupić kawę')
else:
    print('Za mało na kawę')
print()


season = input("podaj porę roku:")

if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesień':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')
print()


x = 12
if x > 4:
    print("impreza")
elif x >= 3:
    print("pizza")
elif x >= 0:
    print("burgery")
else:
    print("kanapki")
print()


year = int(input("Wpisz rok:"))
leap_year = year % 4 == 0
feb = 29 if leap_year else 28
print("luty ma", feb, "dni")

# #oznacza to samo co
# if leap_year:
#     feb = 29
# else:
#     feb = 28
