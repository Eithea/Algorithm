import sys
input = sys.stdin.readline

testcase = int(input())
for t in range(testcase) : 
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    V = {}
    for i in range(1, n+1) : 
        V[l2[n-i]] = i
    T = [0 for i in range(n+1)]
    count = 0
    for x in l1 : 
        i = V[x] - 1
        j = i + 1
        while i > 0 : 
            count = count + T[i]
            i = i - (i&-i)
        while j < n : 
            T[j] = T[j] + 1
            j = j + (j&-j)
    print(count)