from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move():
    """Randomly select a move"""
    return choice(list(defeated_by.keys()))


def _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    if computer_choice == player_choice:
        return tie
    elif defeated_by[player_choice] == computer_choice:
        return lose.format(computer_choice, player_choice)
    else:
        return win.format(player_choice, computer_choice)


def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    x = yield 'Welcome to Rock Paper Scissors'
    while True:
        if x == 'q':
            raise StopIteration
        elif x in defeated_by.keys():
            print(_get_winner(_get_computer_move(), x))
            x = yield
        else:
            print('Invalid choice')
            x = yield
