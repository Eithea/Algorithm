import sys
input = sys.stdin.readline

def makeTR(tree, list, node, start, end) : 
    if start == end : 
        tree[node] = [list[start-1]]
        return
    center = (start + end) // 2
    makeTR(tree, list, 2*node, start, center)
    makeTR(tree, list, 2*node+1, center+1, end)
    len1 = len(tree[2*node])
    len2 = len(tree[2*node+1])
    tree[node] = [None for i in range(len1 + len2)]
    i, j, now = 0, 0, 0
    while i + j < len1 + len2 : 
        if i == len1 : 
            tree[node][now] = tree[2*node+1][j]
            j = j + 1
            now = now + 1
            continue
        if j == len2 : 
            tree[node][now] = tree[2*node][i]
            i = i + 1
            now = now + 1
            continue
        if tree[2*node][i] <= tree[2*node+1][j] : 
            tree[node][now] = tree[2*node][i]
            i = i + 1
            now = now + 1
        else : 
            tree[node][now] = tree[2*node+1][j]
            j = j + 1
            now = now + 1

def MSTR(list) : 
    n = len(list)
    size = n * 4
    tree = [[] for i in range(size)]
    makeTR(tree, list, 1, 1, n)
    return tree

from bisect import bisect_right
def query(node, start, end, left, right, cutline, tree) : 
    if end < left or right < start : 
        return 0
    if left <= start and end <= right : 
        return bisect_right(tree[node], cutline)
    center = (start + end) // 2
    a = query(2*node, start, center, left, right, cutline, tree)
    b = query(2*node+1, center+1, end, left, right, cutline, tree)
    return a + b

n, m = map(int, input().split())
ll = list(map(int, input().split()))

tree = MSTR(ll)
for i in range(m) : 
    left, right, k = map(int, input().split())
    upper = 1000000000
    lower = -upper
    while lower < upper - 1 : 
        center = (upper + lower) // 2
        x = query(1, 1, n, left, right, center, tree)
        if x < k : 
            lower = center
        else :
            upper = center
    print(upper)