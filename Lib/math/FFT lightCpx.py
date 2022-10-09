from math import pi, sin, cos

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def pro(x, y):
    return (x[0]*y[0] - x[1]*y[1], x[1]*y[0] + x[0]*y[1])

def FFT(X, w) : 
    n = len(X)
    if n == 1 : 
        return
    odd = [(0, 0) for i in range(n//2)]
    even = [(0, 0) for i in range(n//2)]
    for i in range(n) : 
        if i %2 : 
            odd[i //2] = X[i]
        else : 
            even[i //2] = X[i]
    ww = pro(w, w)
    FFT(odd, ww)
    FFT(even, ww)
    e = (1, 0)
    for i in range(n//2) : 
        X[i] = add(even[i], pro(e, odd[i]))
        X[i + n//2] = add(even[i], pro((-e[0], -e[1]), odd[i]))
        e = pro(e, w)

def IDFT(X, Y) : 
    n = 1 << (len(X) + len(Y) -1).bit_length()
    X = [(i, 0) for i in X]
    Y = [(i, 0) for i in Y]
    X += [(0, 0) for i in range(n - len(X))]
    Y += [(0, 0) for i in range(n - len(Y))]
    w = (cos(2*pi/n), sin(2*pi/n))
    FFT(X, w)
    FFT(Y, w)
    for i in range(n) :
        X[i] = pro(X[i], Y[i])
    FFT(X, (w[0], -w[1]))
    for i in range(len(X)) :
        X[i] = round(X[i][0] /n)
    return X

def IDFT_SQ(X) : 
    n = 1 << (len(X) *2 -1).bit_length()
    X = [(i, 0) for i in X]
    X += [(0, 0) for i in range(n - len(X))]
    w = (cos(2*pi/n), sin(2*pi/n))
    FFT(X, w)
    for i in range(n) :
        X[i] = pro(X[i], X[i])
    FFT(X, (w[0], -w[1]))
    for i in range(len(X)) :
        X[i] = round(X[i][0] /n)
    return X

def power(X, k):
    if k == 1:
        return X
    if k % 2 :
        return IDFT(power(X, k-1), X)
    X = power(X, k//2)
    while X[-1] == 0:
        X.pop()
    return IDFT_SQ(X)

a = [0,1,1,1]
b = [0,1,1,1]
c = [0,1,1,1]

print(IDFT(a, b))
print(IDFT_SQ(c))