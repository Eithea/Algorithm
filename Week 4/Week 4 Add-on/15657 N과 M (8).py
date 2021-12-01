n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
out = []

def f(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, n):
        out.append(l[i])
        f(depth+1, i, n, m)
        out.pop()
f(0, 0, n, m)