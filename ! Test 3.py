A = input()
B = input()
l = A + '1' + B
lenl = len(l)
rank = [ord(x) for x in l]
def order(i) : 
    if i >= lenl : 
        return -1
    return rank[i]

suffix = [i for i in range(lenl)]
t = 1
newrank = [0 for i in range(lenl)]
while t <= lenl : 
    suffix.sort(key=lambda x: (order(x), order(x + t)))
    i, group = 0, 1
    newrank[suffix[i]] = group
    for i in range(1, lenl) : 
        if order(suffix[i]) != order(suffix[i-1])  or order(suffix[i] + t) != order(suffix[i-1] + t) : 
            group = group + 1
        newrank[suffix[i]] = group
    rank = newrank[:]
    t = t * 2
for i in range(lenl) : 
    rank[suffix[i]] = i

maxlength = 0
maxindex = 0
center = suffix[0]
for i in range(1, lenl - 1) : 
    if suffix[i+1] < center < suffix[i] or suffix[i] < center < suffix[i+1] : 
        length = 0
        a = min(suffix[i], suffix[i+1])
        b = max(suffix[i], suffix[i+1])
        while b + length < lenl and l[a+length] == l[b+length] : 
            length = length + 1
        if length > maxlength : 
            maxlength = length
            maxindex = a
print(maxlength)
print(l[maxindex : maxindex + maxlength])