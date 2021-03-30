from random import choice

def select_quote(qq):
    quote = choice(qq)
    return quote

def reformat(quote):
    quote_and_author = quote.split(' - ')
    return quote_and_author

def show(quote):
    print("Quote of the day is:")
    print("*" * 100)
    print(quote[0].center(100))
    print(quote[1].strip().center(100))
    print("*" * 100)

filename = "quotation.txt"
with open(filename, 'r') as fopen:
    lines = fopen.readlines()

quote = select_quote(lines)
quote = reformat(quote)
show(quote)