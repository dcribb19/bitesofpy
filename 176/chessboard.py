WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with the size passed in.
       Don't return anything, print the output to stdout"""
    even_line = [WHITE, BLACK] * int((size / 2))
    odd_line = [BLACK, WHITE] * int((size / 2))
    for line in range(size):
       if line % 2 == 0:
          for space in even_line:
             print(space, end='')
          print()
       else:
          for space in odd_line:
             print(space, end='')
          print()
