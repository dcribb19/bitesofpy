from itertools import count


class Animal:
    new_id = count(10001)
    animals = []

    def __init__(self, name: str):
        self.name = name.title()
        self.id = next(Animal.new_id)
        Animal.animals.append(str(self))

    def __str__(self):
        return f'{self.id}. {self.name}'

    @classmethod
    def zoo(cls):
        return cls.animals
