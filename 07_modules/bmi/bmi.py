def calculate_BMI(mass, height):
    bmi = mass / (height ** 2)
    bmi_rounded = round(bmi, 2)

    if bmi_rounded < 18:
        return 'underweight'

    elif bmi_rounded >= 18 and bmi_rounded < 25:
        return 'normal'

    elif bmi_rounded >= 25 and bmi_rounded < 30:
        return 'overweight'

    elif bmi >= 30:
        return 'obesity'

    else:
        return 'Something went wrong'



