class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.scores = []

    def __call__(self, n):
        self.scores.append(n)
        return max(self.scores)
