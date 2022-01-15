n2 = int(input())
if n2 %2 : 
    print(0)
    exit(0)
n = n2 //2
DP = [0 for i in range(n+1)]
DP[0] = 1
DP[1] = 3
for i in range(2, n+1) : 
    DP[i] = 4*DP[i-1] - DP[i-2]
print(DP[n])