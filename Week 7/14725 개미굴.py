import sys
input = sys.stdin.readline

n = int(input())
Q = []
for i in range(n) : 
    l = list(input().split())
    Q.append(l[1:])
Q.sort()
for i in range(len(Q[0])) : 
    print('--'*i + Q[0][i])
for i in range(1, len(Q)) : 
    now = Q[i]
    prev = Q[i-1]
    depth = 0
    while (depth < len(now) and depth < len(prev) and now[depth] == prev[depth]) : 
        depth = depth + 1
    for i in range(depth, len(now)) : 
        print('--'*i + now[i])
