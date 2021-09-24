from typing import List
from ctypes import POINTER, c_byte, c_int, c_void_p, cdll, c_char_p, cast
from math import prod
import os

import numpy as np

path = os.path.dirname(__file__)
lib = cdll.LoadLibrary('./primelib.so')

lib.isprime.restype = c_int
lib.isprime.argtypes = [c_int]
lib.erat.argtypes = [c_int]
lib.erat.restype = c_void_p
lib.free_sieve.argtypes = [c_void_p]
lib.free_sieve.restype = c_void_p


def isprime(n: int) -> bool:
    res = lib.isprime(n)
    return bool(res)


def erat(n: int) -> List[int]:
    """Sieve of Eratosthones: produces a list of prime numbers from 1 to n."""
    # Marshal the return type as an array of length n+1
    ptr = lib.erat(n)
    output = cast(ptr, POINTER(c_byte*(n+1)))
    result = [n for n, i in enumerate(output.contents) if i==1]
    lib.free_sieve(output)
    return result



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
