x = int(input())
def f(n) :
    if n == 1 :
        return 1
    else : 
        p = 1
        while n > p : 
            p = p * 2
        n = n - p//2
        return n*2
print(f(x))