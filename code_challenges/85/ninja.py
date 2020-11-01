scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for level in scores:
            if new_score >= level:
                self.belt_check = BELTS[level]
        return self.belt_check

    def _get_score(self):
        return self._score

    def _set_score(self, new_score: int):
        if not isinstance(new_score, int):
            raise ValueError('Score takes an int')
        if new_score < self._get_score():
            raise ValueError('Cannot lower score')

        self._score = new_score

        if self._get_belt(self._get_score()) != self._last_earned_belt:
            print((f'Congrats, you earned {self._get_score()} points '
                   f'obtaining the PyBites Ninja '
                   f'{self._get_belt(self._score).title()} Belt'))
        else:
            print(f'Set new score to {self._get_score()}')
        self._last_earned_belt = self._get_belt(self._get_score())

    score = property(_get_score, _set_score)
