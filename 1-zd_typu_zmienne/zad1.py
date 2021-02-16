# Zadanie 1
year = 365
year_i = 366
day = 24
hour = 60

n_minute = year * day * hour
n1_minute = year_i * day * hour

year_j = 365.25
n2_minute = year_j * day * hour

print("------------------ Ile minut ma rok? ------------------")
print("Rok ma", n_minute, "minut.\nCo cztery lata wypada rok przestępny, który ma", n1_minute, "minut.")
print("Natomiast, stosowany w astronomii i naukach ścisłych - rok juliański ma", n2_minute, "minut.")