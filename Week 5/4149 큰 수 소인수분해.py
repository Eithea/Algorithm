import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from math import gcd
from random import randrange

def MillerRabin(n) : 
    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in alist : 
        return True
    if n < 2 or n % 2 == 0 : 
        return False
    if n < 1373653 : 
        alist = [2, 3]
    elif n < 9080191 : 
        alist = [31, 73]
    elif n < 4759123141 : 
        alist = [2, 7, 61]
    elif n < 2152302898747 : 
        alist = [2, 3, 5, 7, 11]
    elif n < 3474749660383 : 
        alist = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321 : 
        alist = [2, 3, 5, 7, 11, 13, 17]
    
    d = n - 1
    s = 0
    while d % 2 == 0 : 
        d = d // 2
        s = s + 1
    for a in alist : 
        x = pow(a, d, n)
        if x == 1 : 
            continue
        stest = False
        for i in range(s) : 
            if x == n - 1 : 
                stest = True
                break
            x = pow(x, 2, n)
        if not stest : 
            return False
    return True

def f(x, c, n) : 
    return (x * x + c) % n

def PollardRho(n) : 
    if n ==  1 : 
        return 1
    if n % 2 == 0 : 
        return 2
    if MillerRabin(n) : 
        return n
    x = randrange(2, n)
    y = x
    c = randrange(1, n)
    g = 1
    while g == 1 : 
        x = f(x, c, n)
        y = f(f(y, c, n), c, n)
        g = gcd(x - y, n)
        if g == n : 
            return PollardRho(n)
    if MillerRabin(g) : 
        return g
    else : 
        return PollardRho(g)

n = int(input())
factor = []
while n != 1 : 
    p = PollardRho(n)
    n = n // p
    factor.append(p)
factor.sort()
for i in factor : 
    print(i)