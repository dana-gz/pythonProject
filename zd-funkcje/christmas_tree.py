#
# def branch(n):
#     for i in range(1, n+1):
#         print('*' * i)
#
#
# for i in range(2, 10):
#     branch(i)
#
# print('------------------------------------')
#
#
# def segment(n):
#     for i in range(1, n+1, 2):
#         print((i * '*').center(n))
#
#
# for i in range(2, 10):
#     segment(i)
#
# print('------------------------------------')


def segment(width, total_width):
    for i in range(1, width+1, 2):
        print((i * '*').center(total_width))


def tree(size):
    for t in range(3, size+1, 2):
        segment(t, size)

width = int(input("Chose size of the Christmas tree: "))

tree(width)
