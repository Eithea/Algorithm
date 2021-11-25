def prime(n) : 
    check = 1
    if n < 2 : 
        check = 0
    for j in range(2, n//2+1) : 
        if n%j == 0 : 
            check = 0
    return check

testcase = int(input())
testset = list(map(int, input().split()))
stack = 0
for i in testset : 
    stack = stack + prime(i)
print(stack)
