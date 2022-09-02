import sys
input = sys.stdin.readline

def SGoperator(a, b) : 
    return a + b

def SGsearchfunc(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return 0
    if left <= start and right >= end : 
        return tree[i]
    center = (start + end) // 2
    a = SGsearchfunc(tree, 2*i, start, center, left, right)
    b = SGsearchfunc(tree, 2*i+1, center+1, end, left, right)
    return SGoperator(a, b)

def SGupdate(tree, i, start, end, index) : 
    if index < start or index > end : 
        return
    if start == end : 
        tree[i] = 1
        return
    center = (start + end) // 2
    SGupdate(tree, 2*i, start, center, index)
    SGupdate(tree, 2*i+1, center+1, end, index)
    tree[i] = SGoperator(tree[2*i], tree[2*i+1])

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
V = {}
for i in range(n) : 
    V[l2[i]] = i
T = [0 for i in range(4*n)]
count = 0
for  x in l1 : 
    index = V[x]
    count = count + SGsearchfunc(T, 1, 0, n-1, index, n-1)
    SGupdate(T, 1, 0, n-1, index)
print(count)