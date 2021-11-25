m = int(input())
k = 0
leng = 3
while leng < m : 
    k = k + 1
    leng = 2 * leng + 3 + k
def DAC(x, l, n) : 
    if x == 0 : 
        if n == 1 : 
            return 'm'
        else : 
            return 'o'
    l = (l - 3 - x) // 2
    x = x - 1
    if n <= l : 
        return DAC(x, l, n)
    elif n == l + 1 : 
        return 'm'
    elif n > l + x + 4 : 
        return DAC(x, l, n - l - x - 4)
    else : 
        return 'o'
print(DAC(k, leng, m))