import sys
input = sys.stdin.readline
from decimal import *
getcontext().prec = 27
getcontext().rounding = ROUND_HALF_UP

a, b, c = map(Decimal,map(int,input().split()))

pi = Decimal('3.141592653589793238462643383')
def sin(x) : 
    x = x % (2 * pi)
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s
# sinx = 1 - x^2/2! + x^4/4! - ...

lower = (c - b) / a
upper = (c + b) / a
while upper - lower > Decimal('0.000000000000000000001'):
    center = (lower + upper) / 2
    if a * center + b * sin(center) < c: 
        lower = center
    else: 
        upper = center

print(upper)