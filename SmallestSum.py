import math
from functools import reduce


def smallest_possible_sum(arr):
    def compute_gcd(list_numbers):
        return reduce(math.gcd, list_numbers)

    if not arr:
        return 0

    current_gcd = compute_gcd(arr)
    return current_gcd * len(arr)

from math import gcd

def solution(a):
    return gcd(*a) * len(a)

def solution2(a):
    a_len = len(a)
    a = set(a)
    while len(a) != 1:
        b = max(a)
        a.remove(b)
        a.add(b-max(a))
    return max(a) * a_len

print(solution([5, 5, 10]))
#import numpy as np

#def solution3(a):
   # return np.gcd.reduce(a) * len(a)