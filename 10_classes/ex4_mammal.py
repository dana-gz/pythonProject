class Mammal:

    # # shared features
    # characteristic_1 = 'hair and fur'
    # characteristic_2 = 'mammary glands'
    # characteristic_3 = 'single boned lower jaw'
    # characteristic_4 = 'three bones in the middle ear'
    # characteristic_5 = 'warm-blooded metabolisms'
    # characteristic_6 = 'diaphragm'
    # characteristic_7 = 'four-chambered heart'

    def __init__(self, fur_colour, weight, maturity, habitat, food, feature):
        self.fur_colour = fur_colour
        self.weight = weight
        self.maturity = maturity
        self.habitat = habitat
        self.food = food
        self.feature = feature

elephant = Mammal('green-grey', 7500, 12, 'terrestrial', 'plants', 'trunk')
woolf = Mammal('yelllow-grey',  60, 3, 'terrestrial', 'animals', 'wolf pack')
dolphin = Mammal('blue-gray', 350, 3, 'aquatic', 'fish', 'sounds')


