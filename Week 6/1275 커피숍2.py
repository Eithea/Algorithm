import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def SGTR(list) : 
    n = len(list)
    size = 1
    while size < n : 
        size = size * 2
    size = size * 2
    segTR = [0 for i in range(size)]
    makeTR(segTR, list, 1, 0, n-1)
    return segTR

def SGoperator(a, b) : 
    return a + b

def makeTR(tree, list, i, start, end) : 
    if start == end : 
        tree[i] = list[start]
        return tree[i]
    center = (start + end) // 2
    a = makeTR(tree, list, 2*i, start, center)
    b = makeTR(tree, list, 2*i+1, center+1, end)
    tree[i] = SGoperator(a, b)
    return tree[i]

def SGsearchfunc(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return 0
    if left <= start and right >= end : 
        return tree[i]
    center = (start + end) // 2
    a = SGsearchfunc(tree, 2*i, start, center, left, right)
    b = SGsearchfunc(tree, 2*i+1, center+1, end, left, right)
    return SGoperator(a, b)

def SGupdate(tree, i, start, end, index, delta) : 
    if index < start or index > end : 
        return
    tree[i] = SGoperator(tree[i], delta)
    if start < end : 
        center = (start + end) // 2
        SGupdate(tree, 2*i, start, center, index, delta)
        SGupdate(tree, 2*i+1, center+1, end, index, delta)

n, q = map(int, input().split())
l = list(map(int, input().split()))
T = SGTR(l)

for i in range(q) : 
    X, Y, a, b = map(int, input().split())
    x = min(X, Y)
    y = max(X, Y)
    print(SGsearchfunc(T, 1, 0, n-1, x-1, y-1))
    delta = b - l[a-1]
    l[a-1] = b
    SGupdate(T, 1, 0, n-1, a-1, delta)