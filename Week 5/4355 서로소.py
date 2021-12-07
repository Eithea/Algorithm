import sys
input = sys.stdin.readline
while True : 
    n = int(input())
    if n == 0 : 
        break
    count = n
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 : 
            while n % i == 0 : 
                n = n // i
            count = count * (i - 1) // i
    if n != 1 : 
        count = count * (n - 1) // n
    print(count)