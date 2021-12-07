import sys
input = sys.stdin.readline
from itertools import count
from math import gcd

n = int(input())
num = n
if n == 1 : 
    print(1)
    exit(0)
PF = []
if n % 2 == 0 : 
    while n % 2 == 0 : 
        n = n // 2
    PF.append(2)

while n != 1 : 
    x = 2
    done = False
    for cycle in count(1):
        y = x
        for i in range(2 ** cycle):
            x = (x * x + 1) % n
            f = gcd(x - y, n)
            if f > 1:
                while n % f == 0 : 
                    n = n // f
                PF.append(f)
                done = True
                break
        if done : 
            break

for i in PF : 
    num = num * (i-1) // i
print(num)