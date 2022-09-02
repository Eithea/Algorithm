l1 = input()
l2 = input()
l3 = input()

DP = [[[0 for i in range(len(l3) + 1)] for i in range(len(l2) + 1)] for i in range(len(l1) + 1)]
for i in range(len(l1)) : 
    for j in range(len(l2)) : 
        for k in range(len(l3)) : 
            if l1[i] == l2[j] == l3[k] : 
                DP[i][j][k] = DP[i-1][j-1][k-1] + 1
            else : 
                DP[i][j][k] = max(DP[i-1][j][k], DP[i][j-1][k], DP[i][j][k-1])
print(DP[-2][-2][-2])