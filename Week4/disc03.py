def is_prime(n):
  """

  >>> is_prime(7)
  True
  >>> is_prime(10)
  False
  >>> is_prime(1)
  False
  """
  def prime_helper(k):
    if k == 1:
      return True
    elif n == 1 or n % k == 0:
      return False
    else:
      return prime_helper(k - 1)
  return prime_helper(n - 1)

def make_func_repeater(f, x):
  """

  >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
  >>> incr_1(2) #same as f(f(x))
  3
  >>> incr_1(5)
  6
  """
  def repeat(n):
    if n <= 0:
      return x
    else:
      return f(repeat(n - 1))
  return repeat

def count_stair_ways(n):
  if n == 0:
    return 1
  elif n < 0:
    return 0
  else:
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
  """
  >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
  4
  >>> count_k(4, 4)
  8
  >>> count_k(10, 3)
  274
  >>> count_k(300, 1) # Only one step at a time
  1
  """
  if n == 0:
    return 1
  elif n < 0 or k <= 0:
    return 0
  else:
    i = 1
    result = 0
    while i <= k:
      result += count_k(n - i, k)
      i += 1
    return result

def pascal(row, column):
  """
  >>> pascal(4, 2)
  6
  >>> pascal(4, 4)
  1
  >>> pascal(5, 3)
  10
  >>> pascal(300, 1) # Only one step at a time
  300
  """
  if column < 0 or row < 0 or column > row:
    return 0
  elif column == 0:
    return 1
  else:
    return pascal(row - 1, column) + pascal(row - 1, column - 1)

    