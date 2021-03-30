def show_5():
    for i in range(5):
        quote = lines[i].split("-")
        print("*" * 70)
        print(quote[0].center(70))
        print(quote[1].strip().center(70))
        print("*" * 70)

filename = 'quotation.txt'
with open(filename, 'r') as fopen:
    lines = fopen.readlines()

print('----------------------------')

show_5()