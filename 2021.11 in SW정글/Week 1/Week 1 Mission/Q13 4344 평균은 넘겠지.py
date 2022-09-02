testcase = int(input())
for i in range(testcase) : 
    set = list(map(int, input().split()))
    n = set[0]
    del set[0]
    avrg = sum(set) / n
    count = 0
    for score in set : 
        if score > avrg :
            count = count + 1
    percentage = '{:.3f}'.format(round((count / n), 5) * 100)
    text = str(percentage)
    print(text + '%')
    
