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
    if a[0] > b[0] : 
        return b
    else : 
        return a

def makeTR(tree, list, i, start, end) : 
    if start == end : 
        tree[i] = [list[start], start]
        return tree[i]
    center = (start + end) // 2
    a = makeTR(tree, list, 2*i, start, center)
    b = makeTR(tree, list, 2*i+1, center+1, end)
    tree[i] = SGoperator(a, b)
    return tree[i]

def SGsearchfunc(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return [sys.maxsize, sys.maxsize]
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
        tree[i][0] = delta
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
    I = list(map(int, input().split()))
    a = I[0]
    if a == 1 : 
        b, c = I[1], I[2]
        l[b-1] = c
        SGupdate(T, 1, 0, n-1, b-1, c)
    elif a == 2 : 
        print(T[1][1] + 1)