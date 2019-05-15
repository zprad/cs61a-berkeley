""" Optional problems for lab02 """

from lab02 import *

# Higher Order Functions

def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    def test_with(x):
        v1 = compose1(f, g)(x)
        v2 = compose1(g, f)(x)
        return v1 == v2
    return test_with

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def count_with(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return count_with

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    # 参考答案
    # def ret_fn(n):
    #     def ret(x):
    #         i = 0
    #         while i < n:
    #             if i % 3 == 0:
    #                 x = f1(x)
    #             elif i % 3 == 1:
    #                 x = f2(x)
    #             else:
    #                 x = f3(x)
    #             i += 1
    #         return x
    #     return ret
    # return ret_fn
    def cycle_times_of(n):
        def call_with(x):
            result = x
            k = n
            while k > 0:
                if k >= 3:
                    result = f3(f2(f1(result)))
                else:
                    if k == 1:
                        result = f1(result)
                    else:
                        result = f2(f1(result))
                k -= 3
            return result
        return call_with
    return cycle_times_of

def longest_increasing_suffix(n):
    """Return the longest increasing suffix of a positive integer n

    >>> longest_increasing_suffix(63134)
    134
    >>> longest_increasing_suffix(233)
    3
    >>> longest_increasing_suffix(5689)
    5689
    >>> longest_increasing_suffix(568901) # 01 is the suffix, displayed as 1
    1
    """

    m, suffix, k = 10, 0, 1
    while n:
        n, last = n // 10, n % 10
        if last < m:
            m, suffix, k = last, suffix + k * last , 10 * k
        else:
            return suffix
    return suffix

def sandwich(n):
    """Return True if n contains a sandwich and False otherwise

    >>> sandwich(416263)  # 626
    True
    >>> sandwich(5050)    # 505 or 050
    True
    >>> sandwich(4441)    # 444
    True
    >>> sandwich(1231)
    False
    >>> sandwich(55)
    False
    >>> sandwich(4456)
    False
    """

    tens, ones = n % 100 // 10, n % 10
    n = n // 100
    while n > 0:
        if n % 10 == ones:
            return True
        else:
            tens, ones = n % 10, tens
            n = n // 10
    return False

def luhn_sum(n):
    """Return the Luhn sum n

    >>> luhn_sum(135)     # 1 + 6 + 5
    12
    >>> luhn_sum(185)     # 1 + (1 + 6) + 5
    13
    >>> luhn_sum(138743)  # 2 + 3 + (1 + 6) + 7 + 8 + 3
    30
    """

    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + x % 10
    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total += luhn_digit(last)
        multiplier = 3 - multiplier
    return total
