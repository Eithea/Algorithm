eratos = [1 for i in range(1002001)]
eratos[0] = 0
eratos[1] = 0
prime = []
for i in range(2, 1002) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, 1002001, i) : 
            eratos[j] = 0
for i in range(1002001) : 
    if eratos[i] == 1 : 
        prime.append(i)

minr, maxr = map(int, input().split())
table = [1 for i in range(maxr - minr + 1)]
i = 0
while prime[i] ** 2 <= maxr : 
    pp = prime[i] ** 2
    q = minr // pp + 1
    if minr % pp == 0 : 
        q = q - 1
    while pp * q <= maxr : 
        table[pp * q - minr] = 0
        q = q + 1
    i = i + 1
print(sum(table))