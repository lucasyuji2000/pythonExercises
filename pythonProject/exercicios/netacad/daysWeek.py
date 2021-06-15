class WeekDayError(Exception):
    pass


class Weeker:
    week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    dayNumber = 0

    def __init__(self, day):
        try:
            self.__aux = Weeker.week.index(day)
            Weeker.dayNumber = self.__aux
        except ValueError:
            print("Sorry, I can't serve your request.")

    def __str__(self):
        return Weeker.week[Weeker.dayNumber]

    def add_days(self, n):
        Weeker.dayNumber = (Weeker.dayNumber + n) % 7

    def subtract_days(self, n):
        Weeker.dayNumber = (Weeker.dayNumber - n) % 7


weekday = Weeker('Mon')
print(weekday)
weekday.add_days(15)
print(weekday)
weekday.subtract_days(23)
print(weekday)
weekday = Weeker('Monday')
