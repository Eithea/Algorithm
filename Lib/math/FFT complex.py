from math import pi, sin, cos

def FFT(X, w) : 
    n = len(X)
    if n == 1 : 
        return
    odd = [0 for i in range(n//2)]
    even = [0 for i in range(n//2)]
    for i in range(n) : 
        if i %2 : 
            odd[i //2] = X[i]
        else : 
            even[i //2] = X[i]
    FFT(odd, w*w)
    FFT(even, w*w)
    e = 1
    for i in range(n//2) : 
        X[i] = even[i] + e * odd[i]
        X[i + n//2] = even[i] - e * odd[i]
        e = e * w

def IDFT(X, Y) : 
    s = len(X) + len(Y) -1
    n = 1 << s.bit_length()
    X += [0 for _ in range(n - len(X))]
    Y += [0 for _ in range(n - len(Y))]
    w = complex(cos(2*pi/n), sin(2*pi/n))
    FFT(X, w)
    FFT(Y, w)
    for i in range(n) :
        X[i] *= Y[i]
    FFT(X, w.conjugate())
    for i in range(n) : 
        rl = round(X[i].real /n)
        ig = round(X[i].imag /n)
        if ig : 
            X[i] = complex(rl, ig)
        else : 
            X[i] = rl
    return X

def IDFT_SQ(X) : 
    s = len(X) *2 -1
    n = 1 << s.bit_length()
    X += [0 for _ in range(n - len(X))]
    w = complex(cos(2*pi/n), sin(2*pi/n))
    FFT(X, w)
    for i in range(n) :
        X[i] *= X[i]
    FFT(X, w.conjugate())
    for i in range(n) : 
        rl = round(X[i].real /n)
        ig = round(X[i].imag /n)
        if ig : 
            X[i] = complex(rl, ig)
        else : 
            X[i] = rl
    return X

a = [0,1,1,1]
b = [0,1,1,1]
c = [0,1,1,1]

print(IDFT(a, b))
print(IDFT_SQ(c))