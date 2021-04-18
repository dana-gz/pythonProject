import math


def delta_type(a, b, c):
    delta = b*b-4*a*c
    return delta


def sqrt_count(a, b, c):
    d = delta_type(a, b, c)

    if d > 0:
        x1 = (-b-math.sqrt(d))/2/a
        x2 = (-b+math.sqrt(d))/2/a
        root = [x1, x2]

    elif d == 0:
        x1 = -b/2/a
        root = [x1]

    else:
        root = []

    return root


def count_roots(a, b, c):
    roots = sqrt_count(a, b, c)

    if len(roots) == 2:
        print(f'For the numbers:{a}, {b}, {c} there are two square roots {roots[0]} {roots[1]}.')

    elif len(roots) == 1:
        print(f'For the numbers:{a}, {b}, {c} there is one square root {roots[0]}.')

    else:
        print(f'For the numbers: {a}, {b}, {c}  there is no square root.')
