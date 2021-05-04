class Country:
    def description(self, name):
        print(f'{name} - the country area takes {self.area}, its populace counts {self.populace} citizens, '
              f'the officail language is {self.language} and the capital is situated in {self.capital}.')

        # print('%s - the country area takes %s, its populace counts %s citizens, '
        #       f'the officail language is %s and the capital is situated in %s.' % (name, self.area, self.populace,
        #                                                                            self.language, self.capital))

Poland = Country()
Poland.area = '312 696 km2'
Poland.populace = 37672367
Poland.language = 'Polish'
Poland.capital = 'Warsaw'

Germany = Country()
Germany.area = '357 022 km2'
Germany.populace = 83000000
Germany.language = 'German'
Germany.capital = 'Berlin'

France = Country()
France.area = '643 801 km2'
France.populace = 67400000
France.language = 'French'
France.capital = 'Paris'

Poland.description('Poland')
Germany.description('Germany')
France.description('France')

