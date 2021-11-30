l1 = input()
l2 = input()

DP = [['' for i in range(len(l2) + 1)] for i in range(len(l1) + 1)]
for i in range(len(l1)) : 
    for j in range(len(l2)) : 
        if l1[i] == l2[j] : 
            DP[i][j] = DP[i-1][j-1] + l1[i]
        else : 
            if len(DP[i-1][j]) > len(DP[i][j-1]) : 
                DP[i][j] = DP[i-1][j]
            else : 
                DP[i][j] = DP[i][j-1]
print(len(DP[-2][-2]))
print(DP[-2][-2])