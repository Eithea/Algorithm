import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

testcase = int(input())
for i in range(testcase) : 
    Vn, En = map(int, input().split())
    B = [0] + list(map(int, input().split()))
    V = {}
    child = [0 for i in range(Vn + 1)]
    for i in range(1, Vn + 1) : 
        V[i] = []
    for i in range(En) : 
        v1, v2 = map(int, input().split())
        V[v2].append(v1)
        child[v2] = child[v2] + 1
    start = int(input())

    D = [0 for i in range(Vn + 1)]
    def DFS(now) : 
        for next in V[now] : 
            if child[next] == 0 : 
                child[now] = child[now] - 1
                D[now] = max(D[now], D[next] + B[next])
            else : 
                child[now] = child[now] - 1
                DFS(next)
        for next in V[now] : 
            D[now] = max(D[now], D[next] + B[next])
    DFS(start)
    print(D[start] + B[start])