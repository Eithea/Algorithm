import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
W = []
for i in range(n) : 
    W.append(list(map(int, input().split())))

max = sys.maxsize
DP = [[max for i in range(1<<n)] for i in range(n)]

def DFS(start, now, gone) :
    if DP[now][gone] != max : 
        return DP[now][gone]     
    if gone == (1<<n) - 1 : 
        if W[now][start] != 0 : 
            DP[now][gone] = W[now][start]
            return DP[now][gone]
        else : 
            return max
    for next in range(n) : 
        if next != now and W[now][next] != 0 and not gone & 1<<next : 
            DP[now][gone] = min(DP[now][gone], DFS(start, next, gone | 1<<next) + W[now][next])
    return DP[now][gone]

print(DFS(0, 0, 1))