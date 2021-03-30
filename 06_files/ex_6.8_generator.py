import csv
import random


def mixer():
    if input("Are You ready for the message? yes[y] / no[n]: ").lower() == "y":
        random1()
    else:
        print('OK the message is waiting for You...')
    print(' -------------------- ')

    if input("Want more? yes[y] / no[n]: ").lower() == "y":
        mixer()
    else:
        print('OK the message is waiting for You...')
    print(' -------------------- ')


def random1():
    print(random.choice(noun[1::]), random.choice(verb[1::]), random.choice(depends[1::]), random.choice(infinitive[1::]))


noun = []
verb = []
depends = []
infinitive = []


with open('abc.csv', 'r', encoding='utf-8') as csvfile:
    keys = ['n', 'v', 'd', 'i']
    reader = csv.DictReader(csvfile, fieldnames = keys)
    for col in reader:
        noun.append(col['n'])
        verb.append(col['v'])
        depends.append(col['d'])
        infinitive.append(col['i'])

print(' -------------------- ')

mixer()


