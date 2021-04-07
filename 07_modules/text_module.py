import text_generator as tg


if __name__ == '__main__':
    print('main file')

tg.signs = []
for i in range(4):
    sign = input('podaj  znak: ')
    tg.signs.append(sign)


tg.intro = tg.sequence()
print(tg.cut_sequence(tg.intro))

