import sys
input = sys.stdin.readline

coprime = [0 for i in range(10001)]
for n in range(1, 10001) : 
    m = n
    count = n
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 : 
            while n % i == 0 : 
                n = n // i
            count = count * (i - 1) // i
    if n != 1 : 
        count = count * (n - 1) // n
    coprime[m] = coprime[m-1] + count

testcase = int(input())
for t in range(testcase) : 
    n = int(input())
    print(coprime[n] + 1)