p, g = 469762049, 3
def FFT(X, inverse = False) :
    n = len(X)
    j = 0
    for i in range(1, n) :
        bit = n >> 1
        while j >= bit :
            j -= bit
            bit >>= 1
        j += bit
        if i < j :
            X[i], X[j] = X[j], X[i]

    s = 2
    while s <= n :
        ws = pow(g, p//s, p)
        if inverse : 
            ws = pow(ws, p-2, p)
        for i in range(0, n, s) :
            w = 1
            for j in range(i, i + s//2) :
                v = X[j + s//2] * w
                X[j + s//2] = (X[j] - v) %p
                X[j] = (X[j] + v) %p
                w = (w * ws) %p
        s *= 2

    if inverse :
        invn = p - (p-1) // n
        for i in range(n) :
            X[i] = (X[i] * invn)%p
    return

def IDFT(X, Y):
    s = len(X) + len(Y) -1
    n = 1 << s.bit_length()
    X += [0 for _ in range(n - len(X))]
    Y += [0 for _ in range(n - len(Y))]
    FFT(X)
    FFT(Y)
    for i in range(n):
        X[i] *= Y[i]
    FFT(X, True)
    return X

def IDFT_SQ(X) :
    s = len(X) *2 -1
    n = 1 << s.bit_length()
    X += [0 for _ in range(n - len(X))]
    FFT(X)
    for i in range(n) :
        X[i] *= X[i]
    FFT(X, True)
    return X