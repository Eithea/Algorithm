import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

n = int(input())
Q = []
for i in range(n) : 
    Q.append(list(input().split()))

for q in Q : 
    if q[0] == 'L' and left : 
        right.append(left[-1])
        del left[-1]
    elif q[0] == 'D' and right : 
        left.append(right[-1])
        del right[-1]
    elif q[0] == 'B' and left : 
        del left[-1]
    elif q[0] == 'P' : 
        left.append(q[1])

for i in range(len(left)) : 
    print(left[i], end = '')
for i in range(len(right)) : 
    print(right[len(right)-1-i], end = '')