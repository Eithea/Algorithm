from bisect import bisect_left

pow2 = [1 for i in range(54)]
for i in range(1, 54) : 
    pow2[i] = pow2[i-1] * 2

def F(x) : 
    if x < 2 : 
        return x
    try : 
        n = pow2.index(x)
        Fn = n * 2 ** (n-1) + 1
        return Fn
    except : 
        n = bisect_left(pow2, x) - 1
        Fn = n * 2 ** (n-1) + 1
        p = x - 2 ** n
        return Fn + p + F(p)

a, b = map(int, input().split())
Fa = F(a-1)
Fb = F(b)
print(Fb - Fa)