n = 5000000
eratos = [1 for i in range(n + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(n ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, n + 1, i) : 
            if eratos[j] == 1 : 
                eratos[j] = i

t = int(input())
l = list(map(int, input().split()))
for i in range(t) : 
    n = l[i]
    factor = []
    while eratos[n] > 1 : 
        factor.append(eratos[n])
        n = n // eratos[n]
    factor.append(n)
    print(*factor)
