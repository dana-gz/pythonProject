class Orchid:

    kingdom = 'plant kingdom'

    def __init__(self, kind, colour, flowering_time):
        self.kind = kind
        self.colour = colour
        self.flowering_time = flowering_time

    def bloom(self):
        return '{} *** {} *** {}'.format(self.colour, self.colour, self.colour)

    def blossoming(self):
        return print('{}:'.format(self.flowering_time), '\n', 5 * '<->')

    def stop_blossoming():
        return print(20 * '-', "\n")


orchid1 = Orchid("Cymbidium", "yellow", "autumn")
orchid2 = Orchid("Masdevallia", "red", "winter")
orchid3 = Orchid("Miltonia", "rose", "spring")


print(orchid1.kind)
print(orchid1.kingdom)
orchid1.blossoming()
print(orchid1.bloom())
Orchid.stop_blossoming()

print(orchid2.kind)
print(orchid2.kingdom)
orchid1.blossoming()
print(orchid2.bloom())
Orchid.stop_blossoming()

print(orchid3.kind)
print(orchid3.kingdom)
orchid1.blossoming()
print(orchid3.bloom())
Orchid.stop_blossoming()
