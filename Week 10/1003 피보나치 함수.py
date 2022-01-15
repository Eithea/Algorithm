rng = 41
l = [0 for i in range(rng)]
l[0] = 0
l[1] = 1
for i in range(2, rng) : 
    l[i] = l[i-2] + l[i-1]


t = int(input())
while t : 
    t = t - 1
    n = int(input())
    if n : 
        print(l[n-1], l[n])
    else : 
        print(1, 0)