import datetime
import holidays

class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return '{}.{}.universty.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average

    @staticmethod
    def show_sth():
        return 'Obecnie rektorem jest Jon Snow'


    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

today = datetime.date.today()
print('Czy dzisiaj są zajęcia?', Student.academic_day(today))

today = datetime.date.today()
print(today, 'zajęcia się odbywają:', Student.academic_day(today))

saturday = datetime.datetime.strptime('2019-06-22', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(saturday))

sunday = datetime.date.today() - datetime.timedelta(days=7)
print(sunday, 'zajęcia się odbywają:', Student.academic_day(sunday))

saturday = datetime.datetime.strptime('2019-01-06', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(saturday))

randomday = datetime.datetime.strptime('2019-02-06', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(randomday))

obj_anna = Student('Anna', 'Kowalska', 23, 4.7)
obj_jan = Student('Jan', 'Nowak', 22, 3.8)

print(Student.min_avg)
print(obj_anna.min_avg)
print(obj_jan.min_avg)

obj_anna.set_min_avg(4.8)
print('Min srednia dla obiektu Anna', obj_anna.min_avg)
print('Min srednia dla obiektu Jan', obj_jan.min_avg)