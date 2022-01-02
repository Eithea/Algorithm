import sys
input = sys.stdin.readline

def FWTR(list) : 
    n = len(list)
    tree = [0 for i in range(n+1)]
    for i in range(1, n+1) : 
        input_FW(i, list[i-1], tree)
    return tree

def input_FW(index, value, tree) : 
    n = len(tree)
    while index < n : 
        tree[index] = tree[index] + value
        index = index + (index & -index)

def subsumfrom1_FW(right, tree) : 
    sbs = 0
    while right >= 1 : 
        sbs = sbs + tree[right]
        right = right - (right & -right)
    return sbs

def subsum_FW(left, right, tree) : 
    return subsumfrom1_FW(right, tree) - subsumfrom1_FW(left-1, tree)
