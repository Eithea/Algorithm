def prt(fm, to) : 
    print(fm, 'to', to)

def rearr(n, start) : 
    if n == 3 : 
        prt(start+1, start-2)
        prt(start+4, start+1)
        prt(start+2, start-4)
    elif n == 4 : 
        prt(start+5, start-2)
        prt(start+2, start+5)
        prt(start-1, start+2)
        prt(start+6, start-1)
    elif n == 5 : 
        prt(start+7, start-2)
        prt(start+2, start+7)
        prt(start+5, start+2)
        prt(start-1, start+5)
        prt(start+8, start-1)
    elif n == 6 : 
        prt(start+9, start-2)
        prt(start+6, start+9)
        prt(start+1, start+6)
        prt(start+5, start+1)
        prt(start-1, start+5)
        prt(start+10, start-1)
    elif n == 7 : 
        prt(start+11, start-2)
        prt(start+4, start+11)
        prt(start+7, start+4)
        prt(start+2, start+7)
        prt(start+8, start+2)
        prt(start-1, start+8)
        prt(start+12, start-1)

    else : 
        prt(start+2*n-3, start-2)
        prt(start+2, start+2*n-3)
        rearr(n-4, start+4)
        prt(start-1, start+2*n-6)
        prt(start+2*n-2, start-1)

n = int(input())
rearr(n, 1)