burning = 6.4
route = 120
price = 5.04
cost = (route / 100) * burning * price
cost_round = round(cost, 2)
print("Koszt mojej wyprawy to :", cost_round, ".\n")

print ("A teraz Ty:\n")


burning_1 = float(input("Podaj spalanie twojego samochodu na 100 km:"))
route_1 = int(input("Podaj przewidywaną długość trasy [km]:"))
price_1 = float(input("Podaj cenę paliwa [zł]:"))

cost_1 = (route_1 / 100) * burning * price
cost_round_1 = round(cost_1, 2)

print("Koszt wyprawy to :", cost_round_1, "zł.")
