import random

def randomcase_decorator(txt):
    def change_letters():
        tekst = txt()
        tekst1 = ''
        pattern = [1, 2]
        b = random.choice(pattern)
        for i in range(len(tekst)):
            b = random.choice(pattern)
            if b == 1:
                a = tekst[i]
                a = a.lower()
                tekst1 += a

            elif b == 2:
                a = tekst[i]
                a = a.upper()
                tekst1 += a
        return tekst1
    return change_letters

@randomcase_decorator
def new_sentence():
    return 'lorem ipsum dolor sit amet'
print(new_sentence())



# tekst ='abdsdsdsdc'
# tekst1 = ''
# pattern = [1, 2]
# b = random.choice(pattern)
#
# print(b)
# for i in range(len(tekst)):
#     b = random.choice(pattern)
#     if b == 1:
#         a = tekst[i]
#         a = a.lower()
#         tekst1 += a
#
#     elif b == 2:
#         a = tekst[i]
#         a = a.upper()
#         tekst1 += a
# print(tekst1)


