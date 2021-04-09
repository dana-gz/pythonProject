import random

def choose_present():
    present = random.choice(presents[0])
    id = (presents[0]).index(present)
    place = presents[1][id]
    print(f"Let's buy a {present} at {place}.")
    # return present, place

presents = [
    ['book', 'wine', 'chocolate', 'music', 'shirt', 'ticket to the cinema', 'perfume'],
    ['bookshop', 'wine shop', 'supermarket', 'on line', 'big star', 'helios', 'perfume shop']
            ]

counter = len(presents[0])

# ------ main part ----------

choose_present()