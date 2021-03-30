filename = 'tekst.txt'

with open(filename, 'r') as file:
    content = file.readlines()
    print(content)

