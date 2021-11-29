l1 = input()
l2 = input()

DP = [[0 for i in range(len(l2) + 1)] for i in range(len(l1) + 1)]
for i in range(len(l1)) : 
    for j in range(len(l2)) : 
        if l1[i] == l2[j] : 
            DP[i][j] = DP[i-1][j-1] + 1
        else : 
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print(DP[-2][-2])