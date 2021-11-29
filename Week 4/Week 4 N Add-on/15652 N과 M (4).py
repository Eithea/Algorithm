n, m = map(int, input().split())
out = []

def f(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, n):
        out.append(i+1)
        f(depth+1, i, n, m)
        out.pop()
f(0, 0, n, m)