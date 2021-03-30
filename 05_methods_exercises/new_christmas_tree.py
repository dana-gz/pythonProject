def level(width, total_width):
    for i in range(1, width+1, 2):
        print((i * sign).center(total_width))

def tree(size):
    for t in range(1, size+1, 2):
        level(t, size)


def level2(width, total_width):
    for i in range(1, width+1, 2):
        print((width * sign).center(total_width))

def tree2(size):
    for t in range(1, size + 1, 2):
        level2(t, size)



sign = input("Choose the char of the Christmas tree: ")

while sign.isdigit() == True or sign.isalpha() == True or sign.isspace() == True:
    print('The char cannot be letter, digit or space.')
    sign = input("Choose the char of the Christmas tree: ")

width = int(input("Chose size of the Christmas tree: "))



tree(width)

print("\n---------------------------------------\n")

tree2(width)
