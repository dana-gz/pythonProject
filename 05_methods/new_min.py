
def minimum_of_2(arg_1, arg_2):
    return arg_1 if arg_1 < arg_2 else arg_2


def minimum_of(a, b, c):
    return minimum_of_2(c, minimum_of_2(a, b))

print(minimum_of(23, 7, 65))