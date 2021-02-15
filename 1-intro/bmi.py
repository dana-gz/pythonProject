# BMI = masa (kg) / (wzrost (m))²
masa = 63
wzrost = 1.7
bmi = masa / (wzrost ** 2)          # to inny zapis dla równania:  bmi = masa / (wzrost*wzrost)
print("Moje BMI to:", bmi, ".")

bmi_rounded = round(bmi, 2)
print("Po zaokrągleniu, moje BMI to:", bmi_rounded, ".")
print()

waga = int(input('Podaj swoją wagę w [kg]:'))
wzrost_cm = int(input('Podaj swój wzrost w [cm]:'))
wzrost_m = wzrost_cm / 100
twoje_bmi = waga / (wzrost_m ** 2)
twoje_bmi_rounded = round(twoje_bmi, 2)
print('Twoje BMI to:', twoje_bmi, '.')
print('Twoje BMI po zaokrągleniu to:', twoje_bmi_rounded, '.')
