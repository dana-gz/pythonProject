class Father:
    def __init__(self):
        print("I'm your father")

    def do_taxing(self):
        print('Do taxing')

class Mother:
    def __init__(self):
        print("I'm your mom")


    def learn_coding(self):
        print('Learn Python!')

class Child(Father, Mother):
    pass

baby = Child()
print(baby)
baby.learn_coding()
baby.do_taxing()