n = int(input())
if n == 1 : 
    print(0)
    exit(0)
eratos = [1 for i in range(n + 1)]
eratos[0] = 0
eratos[1] = 0
prime = []
for i in range(2, int(n ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, n + 1, i) : 
            eratos[j] = 0
for i in range(n + 1) : 
    if eratos[i] == 1 : 
        prime.append(i)

sump = 0
start = 0
end = 0
count = 0
while sump < n : 
    sump = sump + prime[end]
    end = end + 1
end = end - 1
finish = len(prime)
while end < finish : 
    if sump == n : 
            count = count + 1
            if end != finish - 1 :
                sump = sump - prime[start] + prime[end+1]
            start = start + 1
            end = end + 1
            continue
    if sump > n : 
        sump = sump - prime[start]
        start = start + 1     
        continue
    if sump < n : 
        if end != finish - 1 :
            sump = sump + prime[end + 1]
        end = end + 1
print(count)