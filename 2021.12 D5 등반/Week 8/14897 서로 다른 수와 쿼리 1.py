import sys
input = sys.stdin.readline

def range_in(x) : 
    global count
    Distrib[x] = Distrib[x] + 1
    if Distrib[x] == 1 : 
        count = count + 1

def range_out(x) : 
    global count
    Distrib[x] = Distrib[x] - 1
    if Distrib[x] == 0 : 
        count = count - 1

n = int(input())
l = list(map(int, input().split()))
m = int(input())
Q = []
for i in range(m) : 
    q = list(map(int, input().split()))
    Q.append(q + [i])
sq = int(n**0.5)
Q.sort(key = lambda x : x[0])
Q.sort(key = lambda x : x[1] //sq)
A = [None for i in range(m)]

Distrib = {}
for x in l : 
    Distrib[x] = 0

count = 0
prevleft = Q[0][0]
prevright = Q[0][0] - 1
for q in Q : 
    left, right, order = q[0], q[1], q[2]
    while prevleft < left : 
        range_out(l[prevleft-1])
        prevleft = prevleft + 1
    while left < prevleft : 
        prevleft = prevleft - 1
        range_in(l[prevleft-1])
    while right < prevright : 
        range_out(l[prevright-1])
        prevright = prevright - 1
    while prevright < right : 
        prevright = prevright + 1
        range_in(l[prevright-1])
    A[order] = count
for i in range(m) : 
    print(A[i])