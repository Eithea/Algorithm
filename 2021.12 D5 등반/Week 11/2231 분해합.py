rng = 1000000
ans = [[] for i in range(rng *2)]

for n in range(rng) : 
    summ = n
    num = n
    while num : 
        summ += num %10
        num = num //10
    ans[summ].append(n)

x = int(input())
if ans[x] : 
    print(ans[x][0])
else : 
    print(0)