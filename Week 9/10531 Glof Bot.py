def FFT(f, w) : 
    n = len(f)
    if n == 1 : 
        return
    odd = [0 for i in range(n//2)]
    even = [0 for i in range(n//2)]
    for i in range(n) : 
        if i %2 : 
            odd[i //2] = f[i]
        else : 
            even[i //2] = f[i]
    FFT(odd, w*w)
    FFT(even, w*w)
    e = 1
    for i in range(n//2) : 
        f[i] = even[i] + e * odd[i]
        f[i + n//2] = even[i] - e * odd[i]
        e = e * w

from math import pi, sin, cos
def IDFT(a, b) : 
    maxl = max(len(a), len(b))
    n = 1
    while n <= maxl : 
        n = n * 2
    n = n * 2
    A = [0 for i in range(n)]
    B = [0 for i in range(n)]
    C = [0 for i in range(n)]
    for i in range(len(a)) : 
        A[i] = a[i]
    for i in range(len(b)) : 
        B[i] = b[i]
    w = complex(cos(2*pi/n), sin(2*pi/n))
    FFT(A, w)
    FFT(B, w)
    for i in range(n) : 
        C[i] = A[i] * B[i]
    FFT(C, w.conjugate())
    for i in range(n) : 
        rl = round(C[i].real /n)
        ig = round(C[i].imag /n)
        if ig : 
            C[i] = complex(rl, ig)
        else : 
            C[i] = rl
    return C

rng = 200000
distb = [0 for i in range(rng+1)]
distb[0] = 1

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n) : 
    distb[int(input())] = 1
c = IDFT(distb, distb)
m = int(input())
count = 0
for i in range(m) : 
    if c[int(input())] : 
        count = count + 1
print(count)