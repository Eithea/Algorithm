def makeTR(tree, list, node, start, end) : 
    if start == end : 
        tree[node] = list[start-1]
        return
    center = (start + end) // 2
    makeTR(tree, list, 2*node, start, center)
    makeTR(tree, list, 2*node+1, center+1, end)
    tree[node] = tree[2*node] + tree[2*node+1]

def SGTR_LZ(list) : 
    n = len(list)
    size = n * 4
    tree = [0 for i in range(size)]
    makeTR(tree, list, 1, 1, n)
    lazy = [0 for i in range(size)]
    return tree, lazy

def update_lazy(node, start, end, tree, lazy) : 
    if lazy[node] : 
        tree[node] = tree[node] + lazy[node] * (end - start + 1)
        if start != end : 
            lazy[2*node] = lazy[2*node] + lazy[node]
            lazy[2*node+1] = lazy[2*node+1] + lazy[node]
        lazy[node] = 0

def update_tree(node, start, end, left, right, value, tree, lazy) : 
    update_lazy(node, start, end, tree, lazy)
    if end < left or right < start : 
        return
    if left <= start and end <= right : 
        tree[node] = tree[node] + value * (end - start + 1)
        if start != end : 
            lazy[2*node] = lazy[2*node] + value
            lazy[2*node+1] = lazy[2*node+1] + value
        return
    center = (start + end) // 2
    update_tree(2*node, start, center, left, right, value, tree, lazy)
    update_tree(2*node+1, center+1, end, left, right, value, tree, lazy)
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

n = int(input())
l = list(map(int, input().split()))
tree, lazy = SGTR_LZ(l)
m = int(input())
for i in range(m) : 
    l = list(map(int, input().split()))
    if l[0] == 1 : 
        left, right, value = l[1], l[2], l[3]
        update_tree(1, 1, n, left, right, value, tree, lazy)
    elif l[0] == 2 : 
        left = right = l[1]
        print(query(1, 1, n, left, right, tree, lazy))