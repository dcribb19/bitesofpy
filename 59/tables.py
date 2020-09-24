class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.x = length
        self.y = length
        self._table = self.x * self.y

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self._table

    def __str__(self):
        """Returns a string representation of the table"""
        table_string = ''
        values = [x * y for x in range(1, self.x + 1)
                  for y in range(1, self.y + 1)
                  ]
        for value in range(1, len(values) + 1):
            if value % self.x == 0:
                table_string += f'{values[value - 1]}\n'
            else:
                table_string += f'{values[value - 1]} | '
        return table_string

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if x > self.x or y > self.y:
            raise IndexError
        return x * y
