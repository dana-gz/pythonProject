def calculate_BMI(BMI):
    def BMI(mass, height):
        bmi = mass / (height ** 2)
        bmi_rounded = round(bmi, 2)

        if bmi_rounded < 18:
            return print(mass, '- underweight')

        elif 18 <= bmi_rounded < 25:
            return print(mass,'- normal')

        elif 25 <= bmi_rounded < 30:
            return print(mass,'- overweight')

        elif bmi >= 30:
            return print(mass,'- obesity')

        else:
            return 'Something went wrong'
    return BMI



@calculate_BMI
def myBMI(mass, height):
    myBMI = mass / (height ** 2)
    print(myBMI)

if __name__ == "__main__":
    myBMI(66, 1.7)

    myBMI(46, 1.7)

    myBMI(86, 1.7)
