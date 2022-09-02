def FFT(f, inverse = False) : 
    p, g = 469762049, 3
    j = 0
    n = len(f)
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit = bit >> 1
        j = j + bit
        if i < j:
            f[i], f[j] = f[j], f[i]
    s = 2
    while  s <= n:
        ws = pow(g, p//s, p)
        if inverse :
            ws = pow(ws, p-2, p)
        for i in range(0, n, s):
            w = 1
            for j in range(i, i + (s >> 1)):
                v = f[j + (s >> 1)] * w
                f[j + (s >> 1)] = (f[j] - v) %p
                f[j] = (f[j] + v) %p
                w = w * ws %p
        s = s *2
    if inverse:
        inv = p - (p-1) // n
        f[:] = [x * inv %p for x in f]
    return

def IDFT(A, B) : 
    lenA = len(A)
    lenB = len(B)
    maxl = max(lenA, lenB)
    n = 1
    while n <= maxl : 
        n = n * 2
    n = n * 2
    for i in range(n - lenA) : 
        A.append(0)
    for i in range(n - lenB) : 
        B.append(0)
    C = [0 for i in range(n)]
    FFT(A)
    FFT(B)
    for i in range(n) : 
        C[i] = A[i] * B[i]
    FFT(C, True)
    return C

import sys
input = sys.stdin.readline

rng = 1000000
eratos = [1 for i in range(rng + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(rng ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, rng + 1, i) : 
            eratos[j] = 0
genf = [0 for i in range(rng//2 +1)]
for i in range(3, rng+1) : 
    if eratos[i] == 1 : 
        genf[i//2] = 1
G = IDFT(genf, genf[:])

testcase = int(input())
while testcase : 
    testcase = testcase - 1
    n = int(input())
    if n == 4 : 
        print(1)
        continue
    print((G[n//2 - 1] + 1) //2)