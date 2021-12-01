n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
out = []

from collections import defaultdict
V = defaultdict(int)
U = defaultdict(int)
def f(depth, idx, n, m):
    if depth == m:
        if U[tuple(out)] == 0 :
            print(' '.join(map(str, out)))
            U[tuple(out)] = 1
        return
    for i in range(idx, n):
        if V[i] != 1 : 
            V[i] = 1
            out.append(l[i])
            f(depth+1, i, n, m)
            out.pop()
            V[i] = 0
f(0, 0, n, m)