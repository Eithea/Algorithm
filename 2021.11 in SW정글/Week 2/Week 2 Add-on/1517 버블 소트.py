def msort(l, start, end) : 
    global count
    if start < end : 
        center = (start + end) // 2
        msort(l, start, center)
        msort(l, center + 1, end)

        pl, pr = start, center + 1
        rec = []
        while pl <= center and pr <= end : 
            if l[pl] <= l[pr] : 
                rec.append(l[pl])
                pl = pl + 1
            else:
                rec.append(l[pr])
                pr = pr + 1
                count = count + center + 1 - pl
        if pl <= center : 
            rec = rec + l[pl:center + 1]
        if pr <= end : 
            rec = rec + l[pr:end + 1]
        for i in range(len(rec)) : 
            l[start + i] = rec[i]

n = int(input())
l = list(map(int, input().split()))
count = 0
msort(l, 0, n-1)
print(count)