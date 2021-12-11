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
    return min(a, b)

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
        return sys.maxsize
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
        SGupdate(tree, 2*i+1, center, end, index, delta)

n, m = map(int, input().split())

l = []
for i in range(n) : 
    x = int(input())
    l.append(x)

T = SGTR(l)

for i in range(m) : 
    a, b = map(int, input().split()) 
    print(SGsearchfunc(T, 1, 0, n-1, a-1, b-1))
