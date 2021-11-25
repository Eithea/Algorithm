def f(n, r, c) : 
    if [n, r, c] == [0, 0, 0] : 
        return 0
    x = pow(2, n-1)
    if r < x and c < x : 
        return f(n-1, r, c)
    elif r < x and c >= x : 
        return f(n, r, c-x) + pow(x, 2)
    elif r>= x and c < x : 
        return f(n, r-x, c) + 2 * pow(x, 2)
    elif r>= x and c>= x : 
        return f(n, r-x, c-x) + 3 * pow(x, 2)
n, r, c = map(int, input().split())
print(int(f(n, r ,c)))