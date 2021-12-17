# 에라토스테네스의 체
n = 10000000
eratos = [1 for i in range(n + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(n ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, n + 1, i) : 
            eratos[j] = 0

#밀러 라빈 소수판별법
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

# 폴라드 로
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
    return (x**2 + c) % n

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
    if not p in factor : 
        factor.append(p)

# 팩토리얼
F = [1 for i in range(4000001)]
for i in range(1, 4000001) : 
    F[i] = F[i-1] * i % 1000000007

# a^b%p
def power(a, b, p):
    if b == 0:
        return 1
    if b % 2 :
        return (power(a, b // 2, p) ** 2 * a) % p
    else:
        return (power(a, b // 2, p) ** 2) % p

# 행렬 제곱
n, b = map(int, input().split())
A = []
for i in range(n) : 
    A.append(list(map(int, input().split())))

I = [[0 for i in range(n)] for j in range(n)]
for i in range(n) : 
    I[i][i] = 1
    
for i in range(n) : 
    for j in range(n) : 
        A[i][j] = A[i][j] % 1000

def mult(A, B) : 
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            sum = 0
            for x in range(n) : 
                sum = sum + A[i][x] * B[x][j]
            C[i][j] = sum % 1000
    return C

powerlist = [0 for i in range(37)]
powerlist[0] = A
for i in range(1, 37) : 
    powerlist[i] = mult(powerlist[i-1], powerlist[i-1])

bilist = [0 for i in range(37)]
for i in range(36, -1, -1) : 
    bilist[i] = b // pow(2, i)
    b = b - bilist[i] * pow(2, i)

ans = [[] for i in range(n)]
if bilist[0] == 1 : 
    for i in range(n) : 
        ans[i] = powerlist[0][i][:]
else : 
    for i in range(n) : 
        ans[i] = I[i][:]
for i in range(1, 37) : 
    if bilist[i] == 1 : 
        ans = mult(ans, powerlist[i])
for i in range(n) : 
    for j in range(n-1) :
        print(ans[i][j] , end = ' ')
    print(ans[i][-1])


# 순열 조합 중복순열 중복조합
from itertools import permutations, combinations, product, combinations_with_replacement
