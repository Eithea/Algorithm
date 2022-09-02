import sys
input = sys.stdin.readline

def range_in(x) : 
    global count
    x = x + 100000
    if Distrib[x] != 0 : 
        Distrib_of_Distrib[Distrib[x]] = Distrib_of_Distrib[Distrib[x]] - 1
    Distrib[x] = Distrib[x] + 1
    Distrib_of_Distrib[Distrib[x]] = Distrib_of_Distrib[Distrib[x]] + 1
    if count < Distrib[x] : 
        count = Distrib[x]

def range_out(x) : 
    global count
    x = x + 100000
    Distrib_of_Distrib[Distrib[x]] = Distrib_of_Distrib[Distrib[x]] - 1
    Distrib[x] = Distrib[x] - 1
    Distrib_of_Distrib[Distrib[x]] = Distrib_of_Distrib[Distrib[x]] + 1
    if Distrib[x] == count - 1 and Distrib_of_Distrib[Distrib[x]+1] == 0 : 
        count = Distrib[x]

n, m = map(int, input().split())
l = [None] + list(map(int, input().split()))
Q = []
for i in range(m) : 
    q = list(map(int, input().split()))
    Q.append(q + [i])
sq = int(n**0.5)
Q.sort(key = lambda x : x[0])
Q.sort(key = lambda x : x[1] //sq)
A = [None for i in range(m)]

rng = 200000
Distrib = [0 for i in range(rng+1)]
Distrib_of_Distrib = [0 for i in range(rng+1)]
count = 0
prevleft = Q[0][0]
prevright = Q[0][0] - 1
for q in Q : 
    left, right, order = q[0], q[1], q[2]
    while prevleft < left : 
        range_out(l[prevleft])
        prevleft = prevleft + 1
    while left < prevleft : 
        prevleft = prevleft - 1
        range_in(l[prevleft])
    while right < prevright : 
        range_out(l[prevright])
        prevright = prevright - 1
    while prevright < right : 
        prevright = prevright + 1
        range_in(l[prevright])
    A[order] = count
for i in range(m) : 
    print(A[i])