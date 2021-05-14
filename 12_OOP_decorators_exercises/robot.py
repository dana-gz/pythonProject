import random

class Robot:
    def __init__(self, name, prod_year):
        self.name = name
        self.prod_year = prod_year

    def condition(self):
        cnd = 0
        for i in range(4):
            cnd += int(self.prod_year[i])
        if cnd <= 5:
            return '- seems ok!'
        elif 5 < cnd < 10:
            return'- honestly could be better'
        elif 10 <= cnd < 15:
            return'- bad choice'
        else:
            return'- cheap & weak'


    @property
    def prod_year(self):
        return self.__prod_year


    # works but makes no sense
    # @prod_year.setter
    # def prod_year(self, prod_year):
    #     if prod_year[0] == '1' or int(prod_year[3]) > 4:
    #         no1 = random.randint(0,2)
    #         no2 = random.randint(0,4)
    #         new_prod_year = f'20{no1}{no2}'
    #         self.__prod_year = new_prod_year
    #     else:
    #         self.__prod_year = prod_year

    # the setter idea is to change old robot to the newest

    @prod_year.setter
    def prod_year(self, prod_year):
        if prod_year[0] == '1' or int(prod_year[3]) > 4:
            no1 = random.randint(0,1)
            new_prod_year = f'202{no1}'
            self.__prod_year = new_prod_year
        else:
            self.__prod_year = prod_year

if __name__ == "__main__":

    e55 = Robot('E55', '1999')
    print(f'{e55.name}: {e55.prod_year} {e55.condition()}')
    e23 = Robot('E23','2015')
    print(f'{e23.name}: {e23.prod_year} {e23.condition()}')
    e22 = Robot('E22','2020')
    print(f'{e22.name}: {e22.prod_year} {e22.condition()}')






