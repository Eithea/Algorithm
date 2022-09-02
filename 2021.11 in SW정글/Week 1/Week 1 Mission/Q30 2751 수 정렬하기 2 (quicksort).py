def qsort(list, left, right) : 
    pl = left
    pr = right
    x = list[(left + right) // 2]
    while pl <= pr : 
        while list[pl] < x : 
            pl = pl + 1
        while list[pr] > x :
            pr = pr - 1
        if pl <= pr : 
            list[pl], list[pr] = list[pr], list[pl]
            pl = pl + 1
            pr = pr - 1
    if left < pr : 
        qsort(list, left, pr)
    if right > pl : 
        qsort(list, pl, right)
        
def Qsort(list) : 
    qsort(list, 0, len(list) - 1)

n = int(input())
numset = []
for i in range(n) : 
    m = int(input())
    if m not in numset : 
        numset.append(m)

Qsort(numset)
print(numset)