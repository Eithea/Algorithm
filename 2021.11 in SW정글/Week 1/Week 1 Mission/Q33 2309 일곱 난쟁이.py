list = []
pick = []
breakcheck = 0
for i in range(9) : 
    list.append(int(input()))
for i in range(9) : 
    for j in range(i+1, 9) : 
        pick = sorted(list)
        pick[j] = 0
        pick[i] = 0
        if sum(pick) == 100 : 
            pick.remove(0)
            pick.remove(0)
            breakcheck = 1
            for i in pick : 
                print(i)
            break
    if breakcheck == 1 :
        break