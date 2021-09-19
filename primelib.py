import numpy as np
from math import prod


def erasthones(n: int) -> np.ndarray:
    """Returns all primes less than n
    >>> erasthones(5)
    array([2, 3, 5])
    """
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    lim = int(n**0.5)
    for i in range(2,lim):
        if flags[i]:
            flags[i*i::i] = False
    return np.flatnonzero(flags)


def isprime(n: int) -> bool:
    """Primality test using 6k+-1 optimization.
    From wikipedia
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= n**0.5:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def π(n: int) -> int:
    """Prime counting function for n"""
    return len(erasthones(n))


def primorial(n):
    """Primorial function of n"""
    return prod(erasthones(n))


def pgap(n):
    p = erasthones(n)
    gaps = []
    i = p[0]
    for j in p[1:]:
        gaps.append(j-i)
        i = j
    return gaps
