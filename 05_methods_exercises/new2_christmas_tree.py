def tr(width,size):
    for i in range(0, width):
        print(('/' + i * ' ' + '|' + i * ' ' + '\\').center(3 + 2 * size))
    print(('/' + width * '_' + '|' + width * '_' + '\\').center(3 + 2 * size))

def tree(size):
    print(('*').center(3 + 2 * width))
    for t in range(1, size+1):
        tr(t, size)
    print(('|').center(3 + 2 * width))


width = int(input("Chose size of the Christmas tree: "))

tree(width)



