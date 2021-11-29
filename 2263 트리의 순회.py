import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
ino = list(map(int, input().split()))
posto = list(map(int, input().split()))
ans = []
def DAC(pleft, ileft, len) : 
    root = posto[pleft + len - 1]
    print(root, end = ' ')
    if len > 1 : 
        for i in range(len) : 
            if ino[ileft + i] == root : 
                break
        if i != 0 : 
            DAC(pleft, ileft, i)
        if len - i - 1 != 0 : 
            DAC(pleft + i, ileft + i + 1, len - i - 1)    
DAC(0, 0, n)