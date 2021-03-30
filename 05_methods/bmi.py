# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.
# BMI = masa (kg) / (wzrost (m))²


def bmi_count():
    weigh = int(input('Podaj wagę w [kg]:'))
    height_cm = int(input('Podaj wzrost w [cm]:'))
    height_m = height_cm / 100
    bmi = weigh / (height_m ** 2)
    bmi_rounded = round(bmi, 2)
    return bmi_rounded


def your_bmi_means(bmi):
    bmi_means = ""
    if bmi < 18.5:
        bmi_means = 'niedowaga'

    elif bmi >= 18.5 and bmi < 24.99:
        bmi_means = 'waga prawidłowa'

    elif bmi >= 25 and bmi < 29.99:
        bmi_means = 'nadwaga'

    elif bmi >= 30:
        bmi_means = 'otyłość'

    return bmi_means


def main():
    bmi = 0
    bmi = bmi_count()
    print("Twoje BMI to: ", bmi, "- oznacza to -", your_bmi_means(bmi), ".")


main()



