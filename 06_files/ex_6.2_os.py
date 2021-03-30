import os

def new_file(filename, text):
    with open(filename, 'a') as fp:
        fp.write(text + '\n')

def get_details(new_file):
    print(os.path.getsize(new_file))
    print(os.path.getmtime(new_file))

print('---------------------')

text = "Python" * 1000
new_file("new.txt", text)
get_details("new.txt")


