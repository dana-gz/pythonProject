import random

def sequence():
    sequence_len = random.randrange(len(signs)+1, 100)
    sequence = ''
    for i in range(sequence_len):
        next_sign = random.choice(signs)
        sequence += next_sign
    print(sequence)
    return sequence


def cut_sequence(intro):
    m = 1
    c = 1
    i = 0
    longest_seq = ''
    seq = ''

    for i in range(0, len(intro) - 1):
        if intro[i] == intro[i+1]:
            c = c + 1
            seq += intro[i]
        else:
            if m < c:
                longest_seq = seq + intro[i-1]
                m = c
                c = 1
                seq = ''
            else:
                seq = ''
                c = 1

    return longest_seq, m


signs = []
for i in range(4):
    sign = input('podaj  znak: ')
    signs.append(sign)




