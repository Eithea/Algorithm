import sys
input = sys.stdin.readline

def power(a, b, p):
    if b == 0:
        return 1
    if b % 2 :
        return (power(a, b // 2, p) ** 2 * a) % p
    else:
        return (power(a, b // 2, p) ** 2) % p

F = [1 for i in range(4000001)]
for i in range(1, 4000001) : 
    F[i] = F[i-1] * i % 1000000007

testcase = 1
for t in range(testcase) : 
    n, k = map(int, input().split())
    p = 1000000007
    ans = power(F[n-k], p-2, p) * power(F[k], p-2, p) * F[n] % 1000000007
    print(ans)