l = input()
lenl = len(l)
rank = [ord(x) for x in l]
def order(i) : 
    if i >= lenl : 
        return 0
    return rank[i]

suffix = [i for i in range(lenl)]
pow2 = 1
newrank = [0 for i in range(lenl)]
while pow2 <= lenl : 
    suffix.sort(key=lambda x: (order(x), order(x + pow2)))
    i, group = 0, 1
    newrank[suffix[i]] = group
    for i in range(1, lenl) : 
        if order(suffix[i]) != order(suffix[i-1])  or order(suffix[i] + pow2) != order(suffix[i-1] + pow2) : 
            group = group + 1
        newrank[suffix[i]] = group
    rank = newrank[:]
    pow2 = pow2 * 2

print(*suffix)