import sys
input = sys.stdin.readline

C = []
n, k = map(int, input().split())
for i in range(n) : 
    C.append(int(input()))

count = [0 for i in range(k + 1)]
for now in range(1, k + 1) : 
    before = []
    for coin in C : 
        if coin <= now and count[now - coin] != -1:
            before.append(count[now - coin])
    if not before : 
        count[now] = -1
    else:
        count[now] = min(before) + 1
print(count[k])