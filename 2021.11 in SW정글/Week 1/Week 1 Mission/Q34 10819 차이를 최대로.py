n = int(input())
testset = list(map(int, input().split()))

rearrlist = [[] for i in range(n)]

# 원소 1개의 rearrlist 생성
for i in range(n) : 
    rearrlist[0].append([testset[i]])


# 원소 x개의 rearrlist를 참고하여 원소 x+1개의 rearrlist를 작성
# 원소 n개가 될때까지
for x in range (0, n-1) : 
    for list in rearrlist[x] : 
        remainder = testset[:]
        for e in list : 
            remainder.remove(e)
        for element in testset : 
            if element in remainder : 
                rearrlist[x+1].append(list + [element])


max = 0
for list in rearrlist[n-1] : 
    abssum = 0
    for i in range(len(list) - 1) : 
        abssum = abssum + abs(list[i]-list[i+1])
    if abssum > max : 
        max = abssum

print(max)