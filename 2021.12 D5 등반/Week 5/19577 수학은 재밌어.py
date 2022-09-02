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

origin = int(input())
factor = []
n = origin
while n != 1 : 
    p = PollardRho(n)
    n = n // p
    if not p in factor : 
        factor.append(p)
lenf = len(factor)
maxorder = [0 for i in range(lenf)]
for p in range(lenf) : 
    n = origin
    i = 0
    while n % factor[p] == 0 : 
        n = n // factor[p]
        i = i + 1
    maxorder[p] = i

n = origin
order = [0 for i in range(lenf)]

def nextdiv() : 
    if order[0] < maxorder[0] : 
        order[0] = order[0] + 1
        return True
    i = 0
    while i < lenf and order[i] == maxorder[i] : 
        i = i + 1
    if i == lenf : 
        return False
    for ii in range(i) : 
        order[ii] = 0
    order[i] = order[i] + 1
    return True

def tailrec() : 
    x = 1
    for i in range(lenf) : 
        x = x * (factor[i]**order[i])
    if x ** 2 < n : 
        nextdiv()
        tailrec()
        return
    pi = x
    for i in range(lenf) : 
        if order[i] != 0 : 
            pi = pi * (factor[i] - 1) // factor[i]
    if x * pi == n : 
        print(x)
        exit(0)
    if nextdiv() : 
        tailrec()
    return

tailrec()
print(-1)