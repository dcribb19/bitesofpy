from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit):
        self.limit = limit
        self.x = 1


    def __next__(self):
        if self.x > self.limit:
            raise StopIteration
        else:
            self.x += 1
            return choice(COLORS) + ' egg'

    
    def __iter__(self):
        return self
