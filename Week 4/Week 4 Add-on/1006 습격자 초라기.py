import sys
input = sys.stdin.readline

def DP(end) : 
        for i in range(2, end+1) : 
            TF0, TF1, TF2 = False, False, False
            if l1[i-1] + l1[i] <= w : 
                TF1 = True
                OXct = 1
                OOctXO = 2
            else : 
                OXct = 2
                OOctXO = 3
            if l2[i-1] + l2[i] <= w : 
                TF2 = True
                XOct = 1
                OOctOX = 2
            else : 
                XOct = 2
                OOctOX = 3
            OOctOO = 2
            if l1[i] + l2[i] <= w : 
                OOctOO = 1
                OOctOX = 2
                OOctXO = 2

            DPOO[i] = min(DPOO[i-1] + OOctOO, DPOX[i-1] + OOctOX, DPXO[i-1] + OOctXO)
            if max(DPOO[1], DPOX[1], DPXO[1]) == 5 : 
                TF0 = True
            if TF1 and TF2 and (not TF0 or i > 2) : 
                DPOO[i] = min(DPOO[i], DPOO[i-2] + 2)
            DPOX[i] = min(DPOO[i-1] + 1, DPOX[i-1] + 2, DPXO[i-1] + OXct)
            DPXO[i] = min(DPOO[i-1] + 1, DPOX[i-1] + XOct, DPXO[i-1] + 2)

testcase = int(input())
for t in range(testcase) :
    n, w = map(int, input().split())
    l1 = [0] + list(map(int, input().split()))
    l2 = [0] + list(map(int, input().split()))
    if n == 1 : 
        if l1[1] + l2[1] <= w : 
            print(1)
        else : 
            print(2)
        continue

    DPOO = [0 for i in range(n + 1)]
    DPOX = [0 for i in range(n + 1)]
    DPXO = [0 for i in range(n + 1)]
    if l1[1] + l2[1] <= w : 
        DPOO[1] = 1
    else : 
        DPOO[1] = 2
    DPOX[1] = 1
    DPXO[1] = 1
    DP(n)
    minw = DPOO[n]

    if l1[-1] + l1[1] <= w : 
        DPOO = [0 for i in range(n + 1)]
        DPOX = [0 for i in range(n + 1)]
        DPXO = [0 for i in range(n + 1)]
        DPOO[1] = 2
        DPOX[1] = 1
        DPXO[1] = 5
        DP(n)
        minw = min(minw, DPXO[n])

    if l2[-1] + l2[1] <= w : 
        DPOO = [0 for i in range(n + 1)]
        DPOX = [0 for i in range(n + 1)]
        DPXO = [0 for i in range(n + 1)]
        DPOO[1] = 2
        DPOX[1] = 5
        DPXO[1] = 1
        DP(n)
        minw = min(minw, DPOX[n])

    if l1[-1] + l1[1] <= w and l2[-1] + l2[1] <= w : 
        DPOO = [0 for i in range(n + 1)]
        DPOX = [0 for i in range(n + 1)]
        DPXO = [0 for i in range(n + 1)]
        DPOO[1] = 2
        DPOX[1] = 5
        DPXO[1] = 5
        DP(n-1)
        minw = min(minw, DPOO[n-1])
        
    print(minw)