testcase = 9
max = 0
check = 0
for i in range(testcase) : 
    a = int(input())
    if max < a : 
        max = a
        check = i+1
print(max)
print(check)