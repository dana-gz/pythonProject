import bmi

def open_advice(filename):
    filename = filename + ".txt"
    # ... rty except
    with open(filename) as file:
        advice = file.read()
    return advice

if __name__ == "__main__":import bmi

def open_advice(filename):
    filename = filename + ".txt"
    # ... rty except

    try:
    with open(filename) as file:
        advice = file.read()

    except FileNotFoundError:
        advice
    return advice

if __name__ == "__main__":


    m = get_weight()
    h = get_height()
    result = bmi.calculate_BMI(m, h)
    print(result)
    print(open_advice(result))

def get_weight():
    while True:
        try:
            m = int(input('Podaj wagę w kg: '))
        except (ValueError, TypeError):
            print('To nie jets prawidłowa wartość! Spróbuj jeszcze raz')
            continue

        if m > 30:
            break

        else:
            print('Twoja masa jest nieprawdopodonie niska. Podaj wagę jeszcze raz.')

def get_height():

    while True:
        try:
            h = int(input('Podaj wzrost w m: '))
        except (ValueError, TypeError):
            print('To nie jets prawidłowa wartość! Spróbuj jeszcze raz')
            continue

        if  1.1 < h < 2.5
            break

        else:
            print('Podaj wzrost jeszcze raz.')

    result = bmi.calculate_BMI(m, h)
    print(result)
    print(open_advice(result))