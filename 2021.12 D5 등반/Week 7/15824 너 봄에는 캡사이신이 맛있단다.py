n = int(input())
l = list(map(int, input().split()))
l.sort()

p = 1000000007
pow2 = [1 for i in range(n-1)]
for i in range(1, n-1) : 
    pow2[i] = pow2[i-1] * 2 %p
sump2 = sum(pow2) %p

count = 0
i = 0
while (i <= n-2-i) : 
    subct = (((l[-1-i] - l[i])%p) * sump2) %p
    count = (count + subct) %p
    sump2 = sump2 - pow2[i] - pow2[-1-i]
    i = i + 1
print(count)