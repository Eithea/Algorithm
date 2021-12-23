import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

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
    x = [a[0]+b[0], a[1]+b[1]]
    return x

def makeTR(tree, list, i, start, end) : 
    if start == end : 
        x = [0, 0]
        x[list[start]%2] = 1
        tree[i] = x
        return tree[i]
    center = (start + end) // 2
    a = makeTR(tree, list, 2*i, start, center)
    b = makeTR(tree, list, 2*i+1, center+1, end)
    tree[i] = SGoperator(a, b)
    return tree[i]

def SGsearchfunc(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return [0, 0]
    if left <= start and right >= end : 
        return tree[i]
    center = (start + end) // 2
    a = SGsearchfunc(tree, 2*i, start, center, left, right)
    b = SGsearchfunc(tree, 2*i+1, center+1, end, left, right)
    return SGoperator(a, b)

def SGupdate(tree, i, start, end, index, delta) : 
    if index < start or index > end : 
        return
    if start == end : 
        x = [0, 0]
        x[delta%2] = 1
        tree[i] = x
        return
    center = (start + end) // 2
    SGupdate(tree, 2*i, start, center, index, delta)
    SGupdate(tree, 2*i+1, center+1, end, index, delta)
    tree[i] = SGoperator(tree[2*i], tree[2*i+1])

n = int(input())
l = list(map(int, input().split()))
m = int(input())

T = SGTR(l)
for i in range(m) : 
    a, b, c = map(int, input().split())
    if a == 1 : 
        l[b-1] = c
        SGupdate(T, 1, 0, n-1, b-1, c)
    elif a == 2 : 
        print(SGsearchfunc(T, 1, 0, n-1, b-1, c-1)[0])
    elif a == 3 : 
        print(SGsearchfunc(T, 1, 0, n-1, b-1, c-1)[1])