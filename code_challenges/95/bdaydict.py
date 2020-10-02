from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """
    Override dict to print a message every time a new person is added that has
    the same birthday (day+month) as somebody already in the dict
    """
    def __setitem__(self, name, birthday):
        month_day = [(d.month, d.day) for d in self.values()]
        if (birthday.month, birthday.day) in month_day:
            print(MSG.format(name))
        super().__setitem__(name, birthday)
