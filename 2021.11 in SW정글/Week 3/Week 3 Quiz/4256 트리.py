import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

testcase = int(input())
for x in range(testcase) : 
    n = int(input())
    preo = list(map(int, input().split()))
    ino = list(map(int, input().split()))
    ans = []
    def DAC(pleft, ileft, len) : 
        if len == 1 : 
            ans.append(preo[pleft])
        else : 
            root = preo[pleft]
            for i in range(len) : 
                if ino[ileft + i] == root : 
                    break
            if i != 0 : 
                DAC(pleft + 1, ileft, i)
            if len - i - 1 != 0 : 
                DAC(pleft + i + 1, ileft + i + 1, len - i - 1)
            ans.append(root)
    DAC(0, 0, n)
    print(*ans)