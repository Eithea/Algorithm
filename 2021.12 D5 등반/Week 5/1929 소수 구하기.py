n = 1000000
eratos = [1 for i in range(n + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(n ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, n + 1, i) : 
            eratos[j] = 0

m, n = map(int, input().split())
for i in range(m, n + 1) : 
    if eratos[i] == 1 : 
        print(i)