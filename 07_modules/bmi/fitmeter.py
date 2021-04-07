import bmi

def open_advice(filename):
    filename = filename + ".txt"
    # ... rty except
    with open(filename) as file:
        advice = file.read()
    return advice

if __name__ == "__main__":
    m = 86
    h = 1.6
    result = bmi.calculate_BMI(m, h)
    print(result)
    print(open_advice(result))