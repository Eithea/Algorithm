n, x = map(int, input().split())
numset = list(map(int, input().split()))
for i in range(n) :
    if x > numset[i] : 
        print(numset[i], end = ' ')