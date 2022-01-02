p = 1000000007
def makeTR(tree, list, node, start, end) : 
    if start == end : 
        tree[node] = list[start-1]
        return
    center = (start + end) // 2
    makeTR(tree, list, 2*node, start, center)
    makeTR(tree, list, 2*node+1, center+1, end)
    tree[node] = (tree[2*node] + tree[2*node+1]) %p

def SGTR_LZ(list) : 
    n = len(list)
    size = n * 4
    tree = [0 for i in range(size)]
    makeTR(tree, list, 1, 1, n)
    lazy = [[0, 1, None] for i in range(size)]
    return tree, lazy

def update_lazy(node, start, end, tree, lazy) : 
    if lazy[node][0] : 
        tree[node] = (tree[node] + lazy[node][0] * (end - start + 1)) %p
        if start != end : 
            lazy[2*node][0] = (lazy[2*node][0] + lazy[node][0]) %p
            lazy[2*node+1][0] = (lazy[2*node+1][0] + lazy[node][0]) %p
    if lazy[node][1] != 1 : 
        tree[node] = tree[node] * pow(lazy[node][1], end - start + 1, p) %p
        if start != end : 
            lazy[2*node][1] = lazy[2*node][1] * lazy[node][1] %p
            lazy[2*node+1][1] = lazy[2*node+1][1] * lazy[node][1] %p
    if lazy[node][2] != None : 
        tree[node] = lazy[node][2]
        if start != end : 
            lazy[2*node][2] = lazy[node][2]
            lazy[2*node+1][2] = lazy[node][2]
    lazy[node] = [0, 1, None]

def update_tree_sum(node, start, end, left, right, value, tree, lazy) : 
    update_lazy(node, start, end, tree, lazy)
    if end < left or right < start : 
        return
    if left <= start and end <= right : 
        tree[node] = tree[node] + value * (end - start + 1)
        if start != end : 
            lazy[2*node][0] = (lazy[2*node][0] + value) %p
            lazy[2*node+1][0] = (lazy[2*node+1][0] + value) %p
        return
    center = (start + end) // 2
    update_tree_sum(2*node, start, center, left, right, value, tree, lazy)
    update_tree_sum(2*node+1, center+1, end, left, right, value, tree, lazy)
    tree[node] = (tree[2*node] + tree[2*node+1]) %p

def update_tree_product(node, start, end, left, right, value, tree, lazy) : 
    update_lazy(node, start, end, tree, lazy)
    if end < left or right < start : 
        return
    if left <= start and end <= right : 
        tree[node] = tree[node] * value %p
        if start != end : 
            lazy[2*node][1] = (lazy[2*node][1] * value) %p
            lazy[2*node+1][1] = (lazy[2*node+1][1] * value) %p
        return
    center = (start + end) // 2
    update_tree_product(2*node, start, center, left, right, value, tree, lazy)
    update_tree_product(2*node+1, center+1, end, left, right, value, tree, lazy)
    tree[node] = (tree[2*node] + tree[2*node+1]) %p

def update_tree_reset(node, start, end, left, right, value, tree, lazy) : 
    update_lazy(node, start, end, tree, lazy)
    if end < left or right < start : 
        return
    if left <= start and end <= right : 
        tree[node] = value * (end - start + 1)
        if start != end : 
            lazy[2*node][2] = value
            lazy[2*node+1][2] = value
        return
    center = (start + end) // 2
    update_tree_reset(2*node, start, center, left, right, value, tree, lazy)
    update_tree_reset(2*node+1, center+1, end, left, right, value, tree, lazy)
    tree[node] = (tree[2*node] + tree[2*node+1]) %p

def query(node, start, end, left, right, tree, lazy) : 
    update_lazy(node, start, end, tree, lazy)
    if end < left or right < start : 
        return 0
    if left <= start and end <= right : 
        return tree[node]
    center = (start + end) // 2
    a = query(2*node, start, center, left, right, tree, lazy)
    b = query(2*node+1, center+1, end, left, right, tree, lazy)
    return (a + b) %p
    
import sys
input = sys.stdin.readline

n = int(input())
ll = list(map(int, input().split()))
m = int(input())
tree, lazy = SGTR_LZ(ll)

for i in range(m) : 
    l = list(map(int, input().split()))
    if l[0] == 1 : 
        left, right, value = l[1], l[2], l[3]
        update_tree_sum(1, 1, n, left, right, value, tree, lazy)
    elif l[0] == 2 : 
        left, right, value = l[1], l[2], l[3]
        update_tree_product(1, 1, n, left, right, value, tree, lazy)
    elif l[0] == 3 : 
        left, right, value = l[1], l[2], l[3]
        update_tree_reset(1, 1, n, left, right, value, tree, lazy)
    elif l[0] == 4 : 
        left, right = l[1], l[2]
        print(query(1, 1, n, left, right, tree, lazy))