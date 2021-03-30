filename = 'tekst.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()
        print(content)

except FileNotFoundError:
    print('Error - no such file')


