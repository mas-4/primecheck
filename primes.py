from typing import List
from ctypes import ARRAY, c_byte, c_int, cdll
from math import prod
import os

import numpy as np

path = os.path.dirname(__file__)
lib = cdll.LoadLibrary('./primelib.so')

lib.isprime.restype = c_int
lib.isprime.argtypes = [c_int]
lib.erat.argtype = c_int


def isprime(n: int) -> bool:
    res = lib.isprime(n)
    return bool(res)


def erat(n: int) -> List[int]:
    """Sieve of Eratosthones: produces a list of prime numbers from 1 to n."""
    # Marshal the return type as an array of length n+1
    lib.erat.restype = ARRAY(c_byte, n+1)
    res = lib.erat(n)
    return [n for n, i in enumerate(res) if i==1]


def π(n: int) -> int:
    """Prime counting function for n"""
    return len(erat(n))


def primorial(n):
    """Primorial function of n"""
    return prod(erat(n))


def pgap(n):
    p = erat(n)
    gaps = []
    i = p[0]
    for j in p[1:]:
        gaps.append(j-i)
        i = j
    return gaps
