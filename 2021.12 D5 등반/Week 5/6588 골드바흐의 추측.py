import sys
input = sys.stdin.readline

n = 10000000
if n == 1 : 
    print(0)
    exit(0)
eratos = [1 for i in range(n + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(n ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, n + 1, i) : 
            eratos[j] = 0
 
while True : 
    n = int(input())
    if n == 0 : 
        break
    a = 3
    b = n - a
    while a <= b : 
        if eratos[a] + eratos[b] == 2 :
            print(f'{n} = {a} + {b}')
            break
        a = a + 1
        b = n - a