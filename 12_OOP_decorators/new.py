from datetime import date

import holidays

us_holidays = holidays.UnitedStates()
print(us_holidays.get('2014-01-01'))
print(us_holidays.get('2014-11-11'))