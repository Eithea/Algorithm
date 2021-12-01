n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
out = []

from collections import defaultdict

def f(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        out.append(l[i])
        f(depth+1, n, m)
        out.pop()
f(0, n, m)