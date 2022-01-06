import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
m = int(input())
ll = l[:]
rng = 100000
boxsize = 1000
B = [[] for i in range(rng // boxsize + 2)]
i = 0
while i < n : 
    B[i//boxsize].append(l[i])
    i = i + 1
for b in B : 
    b.sort()
from bisect import bisect_right
for t in range(m) : 
    q = list(map(int, input().split()))
    if q[0] == 1 : 
        i, v = q[1]-1, q[2]
        box = i //boxsize
        B[box].remove(ll[i])
        newi = bisect_right(B[box], v)
        B[box].insert(newi, v)
        ll[i] = v
    elif q[0] == 2 : 
        i, j, k = q[1]-1, q[2]-1, q[3]
        count = 0
        leftbox = i //boxsize
        rightbox = j //boxsize
        for box in range(leftbox+1, rightbox) : 
            count = count + boxsize - bisect_right(B[box], k)
        if leftbox == rightbox : 
            while i <= j : 
                if ll[i] > k : 
                    count = count + 1
                i = i + 1
        else : 
            while i < (leftbox+1) *boxsize : 
                if ll[i] > k : 
                    count = count + 1
                i = i + 1
            i = rightbox *boxsize
            while i <= j : 
                if ll[i] > k : 
                    count = count + 1
                i = i + 1
        print(count)