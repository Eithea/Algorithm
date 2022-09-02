def msort(a) : 
    n= len(a)
    buff = [None] * n
    def m(a, left, right) : 
        if left < right : 
            center = (left + right) // 2
            m(a, left, center)
            m(a, center + 1, right)

            p = j = 0
            i = k = left
            while i <= center : 
                buff[p] = a[i]
                p = p + 1
                i = i + 1
            while i <= right and j < p : 
                if buff[j] <= a[i] : 
                    a[k] = buff[j]
                    j = j + 1
                else : 
                    a[k] = a[i]
                    i = i + 1
                k = k + 1
            while j < p : 
                a[k] = buff[j]
                k = k + 1
                j = j + 1
    m(a, 0, n-1)
    del buff

n = int(input())
a = []
for i in range(n) : 
    a.append(int(input()))
msort(a)
for i in range(n) : 
    print(a[i])