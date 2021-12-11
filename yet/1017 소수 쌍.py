prime = [1 for i in range(2000)]
prime[0] = 0
prime[1] = 0
for i in range(2, 46) : 
    if prime[i] == 1 : 
        for j in range(2 * i, 2000, i) : 
            prime[j] = 0

n = int(input())
l = list(map(int, input().split()))
odd = []
even = []
for i in l : 
    if i % 2 == 1 : 
        odd.append[i]
    else : 
        even.append[i]
# if len(odd) != len(even) : 
#     print(-1)
# else : 
odd.sort()
even.sort()

def DFS(O, E, doneE) : 
    for e in E : 
        if e not in doneE and prime[O[0] + e] == 1 : 
            O1 = O[1:]
            DFS(O1, E, doneE + [e])