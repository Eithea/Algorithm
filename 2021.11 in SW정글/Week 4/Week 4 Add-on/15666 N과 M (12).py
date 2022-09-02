n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
out = []

from collections import defaultdict
U = defaultdict(int)
def f(depth, idx, n, m):
    if depth == m:
        if U[tuple(out)] == 0 :
            print(' '.join(map(str, out)))
            U[tuple(out)] = 1
        return
    for i in range(idx, n):
        out.append(l[i])
        f(depth+1, i, n, m)
        out.pop()
f(0, 0, n, m)