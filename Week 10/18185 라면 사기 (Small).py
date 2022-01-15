n = int(input())
L = list(map(int, input().split())) + [0] *2
cost = 0
for i in range(n):
    if L[i + 1] > L[i + 2]:
        k = min(L[i], L[i+1] - L[i+2])
        L[i] = L[i] - k
        L[i+1] = L[i+1] - k
        cost = cost +  k*5
        k = min(L[i], L[i+1], L[i+2])
        L[i] = L[i] - k
        L[i+1] = L[i+1] - k
        L[i+2] = L[i+2] - k
        cost = cost +  k*7
    else:
        k = min(L[i], L[i+1], L[i+2])
        L[i] = L[i] - k
        L[i+1] = L[i+1] - k
        L[i+2] = L[i+2] - k
        cost = cost +  k*7
        k = min(L[i], L[i+1])
        L[i] = L[i] - k
        L[i+1] = L[i+1] - k
        cost = cost +  k*5
    k = L[i]
    cost = cost +  k*3
print(cost)