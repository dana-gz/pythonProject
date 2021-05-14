class Dogs:
    min_speed = 40

    def __init__(self, name, age,  speed):
        self.name = name
        self.age = age
        self.speed = speed

    def run_race(self):
        if self.age >= 10 and self.speed <= self.min_speed:
           print(f'{self.name} - dog runs too slow and is too old for the race.')
        elif self.age >= 10 and self.speed > self.min_speed:
           print(f'{self.name} - dog is too old for the race.')
        elif self.age < 10 and self.speed <= self.min_speed:
           print(f'{self.name} - dog runs too slow for the race.')
        else:
            print(f'{self.name} - dog can run in the race.')

    @classmethod
    def set_min_speed(cls, new_min_speed):
        cls.min_speed = new_min_speed

# @staticmethod
#     def weather(temperature):
#         if temperature <= 10:
#             return False
#         else:
#             print('good conditions for run')
#             return True



dog1 = Dogs('Rufus', 4, 46)
dog1.run_race()

dog2 = Dogs('Domi', 14, 26)
dog2.run_race()

dog3 = Dogs('Basalt', 14, 42)
dog3.run_race()

dog4 = Dogs('Lawa', 8, 32)
dog4.run_race()


Dogs.set_min_speed(42)

print ('---------')
print(f'Change of speed condition. New minimum speed - {Dogs.min_speed} km/h.')

dog3 = Dogs('Basalt', 14, 42)
dog3.run_race()



