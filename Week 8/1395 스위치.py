def SGTR_LZ(list) : 
    n = len(list)
    size = n * 4
    tree = [0 for i in range(size)]
    lazy = [0 for i in range(size)]
    return tree, lazy

def update_lazy(node, start, end, tree, lazy) : 
    if lazy[node] : 
        tree[node] = (end - start + 1) - tree[node]
        if start != end : 
            lazy[2*node] = (lazy[2*node] + 1) %2
            lazy[2*node+1] = (lazy[2*node+1] + 1) %2
        lazy[node] = 0

def update_tree(node, start, end, left, right, tree, lazy) : 
    update_lazy(node, start, end, tree, lazy)
    if end < left or right < start : 
        return
    if left <= start and end <= right : 
        tree[node] = (end - start + 1) - tree[node]
        if start != end : 
            lazy[2*node] = (lazy[2*node] + 1) %2
            lazy[2*node+1] = (lazy[2*node+1] + 1) %2
        return
    center = (start + end) // 2
    update_tree(2*node, start, center, left, right, tree, lazy)
    update_tree(2*node+1, center+1, end, left, right, tree, lazy)
    tree[node] = tree[2*node] + tree[2*node+1]

def query(node, start, end, left, right, tree, lazy) : 
    update_lazy(node, start, end, tree, lazy)
    if end < left or right < start : 
        return 0
    if left <= start and end <= right : 
        return tree[node]
    center = (start + end) // 2
    a = query(2*node, start, center, left, right, tree, lazy)
    b = query(2*node+1, center+1, end, left, right, tree, lazy)
    return a + b

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [0 for i in range(n)]
tree, lazy = SGTR_LZ(l)
for i in range(m) : 
    l = list(map(int, input().split()))
    left, right = l[1], l[2]
    if l[0] == 0 : 
        update_tree(1, 1, n, left, right, tree, lazy)
    elif l[0] == 1 : 
        print(query(1, 1, n, left, right, tree, lazy))