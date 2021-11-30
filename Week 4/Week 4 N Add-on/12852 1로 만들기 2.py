n = int(input())
DP = [[0, [1]] for i in range(n + 1)]

for i in range(2, n + 1) : 
    DP[i][0] = DP[i-1][0] + 1
    DP[i][1] = DP[i-1][1] + [i]
    if i%3 == 0 and DP[i][0] > DP[i//3][0] : 
        DP[i][0] = DP[i//3][0] + 1
        DP[i][1] = DP[i//3][1] + [i]
    if i%2 == 0 and DP[i][0] > DP[i//2][0] : 
        DP[i][0] = DP[i//2][0] + 1
        DP[i][1] = DP[i//2][1] + [i]
print(DP[-1][0])
for i in range(len(DP[-1][1])) : 
    print(DP[-1][1][-1-i], end = ' ')