n = int(input())
DP = [0 for i in range(n + 1)]

for i in range(2, n + 1) : 
    if i%6 == 0 : 
        DP[i] = min(DP[i//2], DP[i//3], DP[i-1]) + 1
    elif i%3 == 0 : 
        DP[i] = min(DP[i//3], DP[i-1]) + 1
    elif i%2 == 0 : 
        DP[i] = min(DP[i//2], DP[i-1]) + 1
    else : 
        DP[i] = DP[i-1] + 1
print(DP[-1])