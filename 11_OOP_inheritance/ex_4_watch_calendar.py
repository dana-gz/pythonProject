from datetime import date
import calendar
import time
from datetime import tzinfo, timedelta, datetime


class Calendar:

    def the_cal(self):
        current_year = date.today().year
        current_month = date.today().month
        cal = calendar.month(current_year,current_month,5,1)
        return cal


class Watch:
    def __init__(self):
        the_time = time.strftime("%d.%B %Y %H:%M:%S")
        # print(time.strftime("%H:%M:%S"))
        print(f'Today is {the_time}.')




class Watch_Calendar(Calendar, Watch):
    def __init__(self):
        super().__init__()
        super().the_cal()


if __name__ == '__main__':

    w = Watch_Calendar()

    m = Watch_Calendar.the_cal(0)
    print(m)



