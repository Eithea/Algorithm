import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
l = []
while True:
    try:
        l.append(int(input()))
    except:
        break

def DAC(left, right) : 
    if left > right : 
        return
    if left == right : 
        print(l[left])
        return
    i = left + 1
    if l[right] < l[left] : 
        DAC(left + 1, right)
    else : 
        while i <= right and l[i] < l[left] : 
            i = i + 1
        DAC(left + 1, i - 1)
        DAC(i, right)
    print(l[left])

DAC(0, len(l) - 1)