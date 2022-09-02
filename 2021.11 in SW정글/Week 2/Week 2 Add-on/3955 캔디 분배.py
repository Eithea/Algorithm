def euc(a, b) : 
    x0, x1, y0, y1 = 1, 0, 0, 1
    A = a
    # a = bq0 + r1
    # b = r1q1 + r2
    # r1 = r2q2 + r3
    # ...
    while b != 0 : 
        q = a // b
        r = a % b
        a = b
        b = r
        x0, x1 = x1, x0 - q*x1
        y0, y1 = y1, y0 - q*y1
    if a != 1 or y0 > 10**9 : 
        return 'IMPOSSIBLE'
    if y0 < 0 : 
        y0 = y0 + A
    return y0

n = int(input())
for i in range(n) : 
    k, c = map(int, input().split())
    if c == 1 : 
        if k < 10**9 : 
            print(k + 1)
        else : 
            print('IMPOSSIBLE')
        continue
    if k == 1 : 
        print(1)
        continue
    print(euc(k, c))