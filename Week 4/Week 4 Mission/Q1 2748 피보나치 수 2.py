n = int(input())
if n == 1 : 
    print(1)
else : 
    list = [0, 1, 0]
    for i in range(n-1) : 
        list[2] = list[0] + list[1]
        list[0] = list[1]
        list[1] = list[2]
    print(list[2])
