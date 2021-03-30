filename = 'tekst.txt'

with open(filename, 'r', encoding='utf-8') as file:
    content = file.readlines()

print("--------------------------------")

for index, line in enumerate(content):

    print(index, '-->', line)

