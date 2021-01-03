from dataclasses import dataclass, field
import random
from typing import Set

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)

@dataclass
class Game:
    """Number guess class, make it callable to initiate game"""
    _guesses: Set[int] = field(default_factory=set)
    _answer: int = get_random_number()
    _win: bool = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        num = input(f'Guess a number between {START} and {END}:')

        while not isinstance(num, int):
            if not num:
                print('Please enter a number')
                num = input(f'Guess a number between {START} and {END}:')
            else:
                try:
                    num = int(num)
                except ValueError:
                    print('Should be a number')
                    num = input(f'Guess a number between {START} and {END}:')

        if not START <= num <= END:
            print('Number not in range')
        elif num in self._guesses:
            print('Already guessed')
        else:
            self._guesses.add(num)
            return num

    def _validate_guess(self, guess: int) -> bool:
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f'{guess} is correct!')
            self._win = True
            return self._win
        elif guess < self._answer:
            print(f'{guess} is too low')
            return self._win
        else:  # guess > self._answer
            print(f'{guess} is too high')
            return self._win

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while True:
            guess = None
            while not guess:
                guess = self.guess()
            self._validate_guess(guess)

            if self._win:
                print(f'It took you {len(self._guesses)} guesses')
                break
            elif len(self._guesses) == MAX_GUESSES:
                print((f'Guessed {MAX_GUESSES} times, '
                       f'answer was {self._answer}'))
                break
            else:
                pass


if __name__ == '__main__':
    game = Game()
    game()
