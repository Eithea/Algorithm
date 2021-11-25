a = []
def hanoi1to2(n) : 
    if n == 1 :
        a.append('1 2')
    else : 
        hanoi1to3(n-1)
        a.append('1 2')
        hanoi3to2(n-1)
def hanoi1to3(n) : 
    if n == 1 :
        a.append('1 3')
    else : 
        hanoi1to2(n-1)
        a.append('1 3')
        hanoi2to3(n-1)
def hanoi2to1(n) : 
    if n == 1 :
        a.append('2 1')
    else : 
        hanoi2to3(n-1)
        a.append('2 1')
        hanoi3to1(n-1)
def hanoi2to3(n) : 
    if n == 1 :
        a.append('2 3')
    else : 
        hanoi2to1(n-1)
        a.append('2 3')
        hanoi1to3(n-1)
def hanoi3to1(n) : 
    if n == 1 :
        a.append('3 1')
    else : 
        hanoi3to2(n-1)
        a.append('3 1')
        hanoi2to1(n-1)
def hanoi3to2(n) : 
    if n == 1 :
        a.append('3 2')
    else : 
        hanoi3to1(n-1)
        a.append('3 2')
        hanoi1to2(n-1)

n = int(input())
if n < 21 :
    hanoi1to3(n)
    print(len(a))
    for i in a : 
        print(i)
else : 
    print(pow(2, n) - 1)