def Mobius(n) : 
    M = [0 for i in range(n+1)]
    M[1] = 1
    for i in range(1, n+1) : 
        for j in range(2*i, n+1, i) : 
            M[j] = M[j] - M[i]
    return M

def Mertens(n, M) : 
    count = 0
    i = 1
    while i**2 <= n : 
        count = count + M[i] * (n // i**2)
        i = i + 1
    return count

k = int(input())
M = Mobius(100000)
upper = 2 * k
lower = 0

while lower < upper - 1 : 
    center = (upper + lower) // 2
    x = Mertens(center, M)
    if x < k : 
        lower = center
    else :
        upper = center

print(upper)