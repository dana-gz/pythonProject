from abc import ABC, abstractmethod

class Vehicles(ABC):

    @abstractmethod
    def licence(self):
        pass

    @abstractmethod
    def vehicle(self):
        pass

class Car(Vehicles):
    def __init__(self):
        print('car - a vehicle with an engine, four wheels, and seats for a small number of passengers')

    licence_cat = 'B category'
    vehicle_type = 'car'

    def licence(self):
        print(self.licence_cat)

    def vehicle(self):
        print(self.vehicle_type)


class Bus(Vehicles):
    def __init__(self):
        print('bus - a large vehicle that carries passengers by road, usually along a fixed route')

    licence_cat = 'D category'
    vehicle_type = 'bus'

    def licence(self):
        print(self.licence_cat)

    def vehicle(self):
        print(self.vehicle_type)


class Truck(Vehicles):
    def __init__(self):
        print('truck - a large road vehicle for carrying goods from place to place')

    licence_cat = 'C category, CE category'
    vehicle_type = 'truck'

    def licence(self):
        print(self.licence_cat)

    def vehicle(self):
        print(self.vehicle_type)



class Bike(Vehicles):
    def __init__(self):
        print('bicycle - a vehicle with two wheels that you sit on and move by turning the two pedals '
              '(= parts you press with your feet)')

    licence_cat = 'no'
    vehicle_type = 'bike'

    def licence(self):
        print(self.licence_cat)

    def vehicle(self):
        print(self.vehicle_type)



audi = Car()

#print(f'You need {audi.licence_cat} to drive a {audi.vehicle_type}')

print('You need {} to drive a {}.'.format(audi.licence_cat, audi.vehicle_type))