# def max_of_2(arg_1, arg_2):
#     if arg_1 > arg_2:
#         return arg_1
#     else:
#         return arg_2

# max_of_ab = max_of_2(a, b)
# if c > max_of_ab:
#     return c
# else:
#     return max_of_ab


def maximum_of_2(arg_1, arg_2):
    return arg_1 if arg_1 > arg_2 else arg_2


def maximum_of(a, b, c):
    return maximum_of_2(c, maximum_of_2(a, b))

print(maximum_of(23, 7, 65))