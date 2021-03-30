# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

lift_h = 250
lift_w = 140
lift_d = 140

lift_h_m = lift_h / 100
lift_w_m = lift_w / 100
lift_d_m = lift_d / 100

lift_volume = lift_h_m * lift_w_m * lift_d_m
lift_floor_space = lift_w_m * lift_d_m

fridge_h = 200
fridge_w = 60
fridge_d = 75

fridge_h_m = fridge_h / 100
fridge_w_m = fridge_w / 100
fridge_d_m = fridge_d / 100

fridge_volume = fridge_h_m * fridge_w_m * fridge_d_m
fridge_floor_space = fridge_w_m * fridge_d_m

volume_left = lift_volume - fridge_volume
volume_left_rounded = round(volume_left, 2)
floor_space_left = lift_floor_space - fridge_floor_space
floor_space_left_rounded = round(floor_space_left, 2)

print()
print("Jeśli do windy o  wymiarach: wysokość :", lift_h, "cm, szerokość:", lift_w, "cm, głębokość:", lift_d, "cm")
print("wstawimy lodówkę o wymiarach: wysokość:", fridge_h, "cm, szerokość:", fridge_w, "cm, głębokość:", fridge_d, "cm")
print("wówczas pozostanie:", floor_space_left_rounded, "metrów kwadratowych powierzchni podłogi oraz", volume_left_rounded, "metrów sześciennych.")

print()
print()