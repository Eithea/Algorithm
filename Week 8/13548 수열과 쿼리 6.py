import sys
input = sys.stdin.readline

def range_in(x) : 
    Distrib[x] = Distrib[x] + 1

def range_out(x) : 
    Distrib[x] = Distrib[x] - 1

n = int(input())
l = [None] + list(map(int, input().split()))
m = int(input())
Q = []
for i in range(m) : 
    q = list(map(int, input().split()))
    Q.append(q + [i])
sq = int(n**0.5)
Q.sort(key = lambda x : x[0])
Q.sort(key = lambda x : x[1] //sq)
A = [None for i in range(m)]

rng = 100000
Distrib = [0 for i in range(rng+1)]
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
    A[order] = max(Distrib)
for i in range(m) : 
    print(A[i])