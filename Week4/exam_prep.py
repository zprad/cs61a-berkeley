def print_numbers(n, k):
  """Print all numbers that (A) can be formed from the digits
  of `n` in reverse order and (B) are multiples of `k`.
  This is essentially Fall 2015 Midterm 2 #3c written to not
  depend on knowledge of lists.
  Args:
  n (int): The number that results must use digits from.
  k (int): The number that results must be multiples of.
  >>> print_numbers(97531, 5)
  135
  15
  35
  >>> print_numbers(97531, 7)
  1379
  357
  35
  >>> print_numbers(97531, 2)
  """
  def inner(n, s):
    if n == 0:
      if s % k == 0 and s > k:
        print(s)
    else:
      inner(n // 10, s * 10 + n % 10 )
      inner(n // 10, s)
  inner(n, 0)

def sixty_ones(n):
  """Return the number of times that a 1 directly follows a 6
  in the digits of `n`.
  This is essentially Fall 2014 Midterm 2 #3a written to not
  depend on knowledge of lists.
  Args:
  n (int): The number whose digits are to be examined.
  Returns:
  int: The number of occurrences.
  >>> sixty_ones(461601)
  1
  >>> sixty_ones(161461601)
  2
  """
  if n == 0:
    return 0
  elif n % 100 == 61:
    return 1 + sixty_ones(n // 10)
  else:
    return sixty_ones(n // 10)

def no_elevens(n):
  """Return the number of `n`-digit numbers whose digits
  consist of 1's and 6's and do not contain a `1` and
  then another `1` consecutively.
  This is essentially Fall 2014 Midterm 2 #3b rewritten to
  not depend on knowledge of lists.
  Args:
  n (int): The length of the numbers.
  Returns:
  int: The number of numbers.
  >>> no_elevens(2) # 66, 61, 16
  3
  >>> no_elevens(3) # 666, 661, 616, 166, 161
  5
  >>> no_elevens(4) # 6666, 6661, 6616, 6161, 6166, 1666, 1661, 1616
  8
  """
  if n == 0:
    return 1
  elif n == 1:
    return 2
  else:
    return no_elevens(n - 1) + no_elevens(n - 2)

#Guerrilla Section 2: Higher Order Functions & Recursion/Tree Recursion

def make_skipper(n):
  """
  >>> a = make_skipper(2)
  >>> a(5)
  1
  3
  5
  """
  def print_numbers(x):
    k = 0
    while k <= x:
      if k % n != 0:
        print(k)
      k += 1
  return print_numbers

def make_alternator(f, g):
  """
  >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
  >>> a(5)
  1
  6
  9
  8
  25
  >>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
  >>> b(4)
  2
  4
  6
  6
  """
  def print_numbers(x):
    k = 1
    while k <= x:
      if k % 2 == 0:
        print(g(k))
      else:
        print(f(k))
      k += 1
  return print_numbers

def mario_number(level):
  """
  Return the number of ways that Mario can traverse the level,
  where Mario can either hop by one digit or two digits each turn.
  A level is defined as being an integer with digits where a 1 is
  something Mario can step on and 0 is something Mario cannot step
  on.
  >>> mario_number(10101) # Hops each turn: (1, 2, 2)
  1
  >>> mario_number(11101) # Hops each turn: (1, 1, 1, 2), (2, 1, 2)
  2
  >>> mario_number(100101)# No way to traverse through level
  0
  """
  if level == 1:
    return 1
  elif level % 10 == 0:
    return 0
  else:
    return mario_number(level // 10) + mario_number(level // 100)

from operator import add, mul
def combine(n, f, result):
  """
  Combine the digits in n using f.
  >>> combine (3, mul, 2) # mul (3, 2)
  6
  >>> combine (43, mul, 2) # mul (4, mul (3, 2))
  24
  >>> combine (6502, add, 3) # add (6, add (5, add (0, add (2 , 3)))
  16
  >>> combine (239, pow, 0) # pow (2, pow (3, pow (9, 0)))
  8
  """
  if n == 0:
    return result
  else:
    return combine(n // 10, f, f(n % 10, result))




