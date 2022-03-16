n1, n2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

i1, i2, n = 0, 0, 0
l = []
while n < n1 + n2 : 
    if i1 == n1 or i2 == n2 : 
        break
    if l1[i1] < l2[i2] : 
        l.append(l1[i1])
        i1 += 1
    else : 
        l.append(l2[i2])
        i2 += 1
    n += 1

while i1 < n1 : 
    l.append(l1[i1])
    i1 += 1
while i2 < n2 : 
    l.append(l2[i2])
    i2 += 1
print(*l)