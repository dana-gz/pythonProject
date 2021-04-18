from random import choice


def select_quote(qq):
    quote = choice(qq)
    return quote


def reformat(quote):
    quote_and_author = quote.split(' - ')
    return quote_and_author


def show(quote):
    print("*" * 90)
    print(quote[0].center(90))
    print(quote[1].strip().center(90))
    print("*" * 90)


def quotation(n):
    for i in range(n):
        quote = select_quote(lines)
        quote = reformat(quote)
        show(quote)


filename = "quotation.txt"
with open(filename, 'r') as fopen:
    lines = fopen.readlines()

print('-' * 90)

quotation(3)
