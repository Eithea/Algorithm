import sys
input = sys.stdin.readline
from math import gcd

lcm = 2
c = 7
lcm = lcm * c // gcd(lcm, c)
print(lcm)