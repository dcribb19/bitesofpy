from collections import deque

def rotate(string, n):
   """Rotate characters in a string.
      Expects string and n (int) for number of characters to move.
   """
   rotate_string = ''
   d = deque(string)
   if n > 0:
      d.rotate(-n)
      return rotate_string.join([x for x in d])
   if n < 0:
      d.rotate(abs(n))
      return rotate_string.join([x for x in d])

print(rotate('hello', 2))
print(rotate('hello', -2))