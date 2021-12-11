import sys
input = sys.stdin.readline

p = 1000000007
F = [1 for i in range(2000001)]
for i in range(1, 2000001) : 
    F[i] = F[i-1] * i % p
   
testcase = int(input())
for t in range(testcase) : 
    n = int(input())
    print(F[2*n] * pow(F[n] * F[n+1] % p, p-2, p) % p)