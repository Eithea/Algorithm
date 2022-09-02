rng = 11
l = [0 for i in range(rng+1)]
l[0] = 0
l[1] = 1
l[2] = 2
l[3] = 4
for i in range(4, rng+1) : 
    l[i] = l[i-3] + l[i-2] + l[i-1]

t = int(input())
while t : 
    t = t - 1
    n = int(input())
    print(l[n])