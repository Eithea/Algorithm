import sys
input = sys.stdin.readline

C = []
n, k = map(int, input().split())
for i in range(n) : 
    C.append(int(input()))

DP = [0 for i in range(k + 1)]
DP[0] = 1
for coin in C : 
    for now in range(1, k + 1) :
        if coin <= now :
            DP[now] = DP[now] + DP[now - coin]
print(DP[k])