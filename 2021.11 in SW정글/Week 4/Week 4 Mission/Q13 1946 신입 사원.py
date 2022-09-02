import sys
input = sys.stdin.readline

testcase = int(input())
for t in range(testcase) : 
    n = int(input())
    l = []
    for i in range(n) : 
        l.append(list(map(int, input().split())))
    l.sort()
    top = sys.maxsize
    count = 0
    for a, b in l : 
        if b < top : 
            count = count + 1
            top = b
    print(count)