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

def makeTR(tree, list, i, start, end) : 
    if start == end : 
        tree[i] = list[start]
        return tree[i]
    center = (start + end) // 2
    tree[i] = makeTR(tree, list, 2*i, start, center) + makeTR(tree, list, 2*i+1, center+1, end)
    return tree[i]

def SGsubsum(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return 0
    if left <= start and right >= end : 
        return tree[i]
    center = (start + end) // 2
    return SGsubsum(tree, 2*i, start, center, left, right) + SGsubsum(tree, 2*i+1, center+1, end, left, right)

def SGupdate(tree, i, start, end, index, delta) : 
    if index < start or index > end : 
        return
    tree[i] = tree[i] + delta
    if start < end : 
        center = (start + end) // 2
        SGupdate(tree, 2*i, start, center, index, delta)
        SGupdate(tree, 2*i+1, center+1, end, index, delta)

n, m = map(int, input().split())

l = [0 for i in range(n)]

T = [0 for i in range(3000000)]

for i in range(m) : 
    a, b, c = map(int, input().split())
    if a == 1 : 
        delta = c - l[b-1]
        l[b-1] = c
        SGupdate(T, 1, 0, n-1, b-1, delta)
    elif a == 0 : 
        B = min(b, c)
        C = max(b, c)
        print(SGsubsum(T, 1, 0, n-1, B-1, C-1))
