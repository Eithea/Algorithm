import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
p = 1000000007
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
    tree[i] = makeTR(tree, list, 2*i, start, center) * makeTR(tree, list, 2*i+1, center+1, end) % p
    return tree[i]

def SGsubprod(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return 1
    if left <= start and right >= end : 
        return tree[i]
    center = (start + end) // 2
    return SGsubprod(tree, 2*i, start, center, left, right) * SGsubprod(tree, 2*i+1, center+1, end, left, right) % p

def SGupdate(tree, i, start, end, index, before, after) : 
    if index < start or index > end : 
        return
    if start < end : 
        center = (start + end) // 2
        SGupdate(tree, 2*i, start, center, index, before, after)
        SGupdate(tree, 2*i+1, center+1, end, index, before, after)
    if start == end : 
        if before == 0 : 
            tree[i] = after % p
        else : 
            tree[i] = tree[i] * after // before % p
    else : 
        tree[i] = tree[2*i] * tree[2*i+1] % p

n, m, k = map(int, input().split())

l = []
for i in range(n) : 
    x = int(input())
    l.append(x)

T = SGTR(l)

for i in range(m + k) : 
    a, b, c = map(int, input().split())
    if a == 1 : 
        before = l[b-1]
        l[b-1] = c
        SGupdate(T, 1, 0, n-1, b-1, before, c)
    elif a == 2 : 
        print(SGsubprod(T, 1, 0, n-1, b-1, c-1))
