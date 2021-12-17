# graph dict
Vn, En = map(int, input().split())
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v2].append(v1)

# topological sorting
parent = [0 for i in range(Vn + 1)]
parent[v1] = parent[v1] + 1
child = [0 for i in range(Vn + 1)]
child[v2] = child[v2] + 1