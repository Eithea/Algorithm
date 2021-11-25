n = int(input())

star = ['*']
size = 1
while size != n : 
    next = ['' for i in range(size * 3)]
    for i in range(size) : 
        next[i] = star[i] * 3
        next[size + i] = star[i] + ' '*size + star[i]
        next[size *2 + i] = star[i] * 3
    star = next[:]
    size = size * 3
for i in range(size) : 
    print(star[i])