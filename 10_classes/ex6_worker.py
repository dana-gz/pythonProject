class Worker:
    employer = 'Best Company'
    mail_suffix = employer = employer.replace(' ', '').lower()

    def __init__(self, name, surname, position, wage, practice, student):
        self.position = position
        self.wage = wage
        self.name = name
        self.surname = surname
        self.practice = practice
        self.student = student

    def tax(self):
        tax = self.wage * 0.17
        tax = round(tax, 2)
        return 'Miesięczna zaliczka na podatek wynosi {} zł.'.format(tax)

    def zus(self):
        zus = 0
        if self.student is False:
            zus = self.wage * 0.09
        return 'Miesięczna składka na ubezpieczenie zdrowotne wynosi {} zł.'.format(zus)

    def rise(self):
        if self.practice < 5:
            rise = self.wage * 0.10
        elif self.practice >= 5:
            rise = self.wage * 0.20
        return 'Pracownik otrzymał roczną podwyżkę {} zł.'.format(rise)

    def mail_prefix(self):
        vowel = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
        prefix = ''
        for i in ((self.name + self.surname).lower()):
            if i not in vowel:
                prefix += i
        return prefix

    def mail(self):
        return '{}@{}.com'.format(self.mail_prefix(), self.mail_suffix)


worker_01 = Worker('Michał', 'Ochmann', 'kasjer', 3000, 2, False)
print(worker_01.name, worker_01.surname, ' - ', worker_01.position)
print('Miesięczne w minionym roku:', worker_01.wage, 'zł.')
print(worker_01.tax())
print(worker_01.zus())
print(worker_01.rise())
print(worker_01.mail())
