class Pen:
    def __init__(self):
        print('is long')


class Pineapple:
    def scream(self):
        print('is sweat!!!')


class PenPineapple(Pen, Pineapple):
    def __init__(self):
        print('is amazing')
        super().__init__()
        super().scream()

if __name__ == '__main__':
    penpineapple1 = PenPineapple()

