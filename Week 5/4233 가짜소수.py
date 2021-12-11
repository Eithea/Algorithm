import sys
input = sys.stdin.readline

n = 1000000
eratos = [1 for i in range(n + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(n ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, n + 1, i) : 
            eratos[j] = 0
prime = []
for i in range(len(eratos)) : 
    if eratos[i] == 1 : 
        prime.append(i)

while True : 
    p, a = map(int, input().split())
    if p == a == 0 : 
        break
    if pow(a, p, p) != a : 
        print('no')
        continue
    pr = True
    i = 0
    while i < len(prime) and prime[i] < p : 
        if p % prime[i] == 0 :
            pr = False
            break
        i = i + 1
    if pr : 
        print('no')
    else : 
        print('yes')
