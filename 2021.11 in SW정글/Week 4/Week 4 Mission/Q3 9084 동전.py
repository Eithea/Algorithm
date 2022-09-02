testcase = int(input())
for t in range(testcase) : 
    n = int(input())
    C = list(map(int, input().split()))
    m = int(input())
    DP = [0 for i in range(m + C[-1] + 1)]
    DP[0] = 1
    for coin in C : 
        for i in range(1, m + 1) : 
            DP[i] = DP[i] + DP[i - coin]
    print(DP[m])