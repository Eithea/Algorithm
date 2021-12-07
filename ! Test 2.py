import sys
input = sys.stdin.readline
from itertools import count
from math import gcd

n = int(input())
PF = []

for cycle in count(1):
    y = x
    for i in range(2 ** cycle):
        x = (x * x + 1) % n
        f = gcd(x - y, n)
        if f > 1:
            PF.append(f)
            break