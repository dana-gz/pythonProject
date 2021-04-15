
filename = '06r.txt'

try:
    with open(filename, 'r') as f:
        f.read()
except FileNotFoundError:
    print('File not found. Try again ;) ')

filename1 = '01w.txt'
with open(filename1, 'w') as f:

    try:
        with open(filename1, 'r') as f:
            f.read()
    except SyntaxError:
        print('Unexpected EOF', filename1.title(), ' while parsing. Try again ;) ')

try:
    with open(filename1, 'x') as f:
         f.read()
except FileExistsError:
    print('File exists:', filename1.title())



