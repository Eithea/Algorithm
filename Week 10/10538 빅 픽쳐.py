import sys
input = sys.stdin.readline
from collections import deque

class NODE(dict) :
        def __init__(self) :
            super().__init__()
            self.final = False
            self.out = set()
            self.fail = None
            
        def addout(self, out) :
            if type(out) is set :
                self.out = self.out.union(out)
            else :
                self.out.add(out)
        
        def addchild(self, alphabet, node = None) :
            self[alphabet] = NODE() if node is None else node

class AC() :      
    def __init__(self, PATTERN_LIST) :
        self.PATTERN_LIST = PATTERN_LIST
        self.head = NODE()      
        self.makeTrie()
        self.makeFailure()
        
    def search(self, TARGET) :
        now = self.head
        ret = [0 for i in range(len(TARGET))]
        for index in range(len(TARGET)) :
            letter = TARGET[index]
            while now is not self.head and letter not in now :
                now = now.fail
            if letter in now :
                now = now[letter]           
            if now.final :
                ret[index] = hash[list(now.out)[0]]
        return ret
    
    def makeTrie(self) :
        for pattern in self.PATTERN_LIST :
            now = self.head
            for letter in pattern  :
                if letter not in now :
                    now.addchild(letter)
                now = now[letter]
            now.final = True
            now.addout(pattern)
            
    def makeFailure(self) :
        que = deque()
        self.head.fail = self.head
        que.append(self.head)
        while que :
            now = que.popleft()
            for next in now :
                child = now[next]
                
                if now is self.head :
                    child.fail = self.head
                else  :
                    f = now.fail
                    while f is not self.head and next not in f :
                        f = f.fail
                    if next in f :
                        f = f[next]
                    child.fail = f                
                child.addout(child.fail.out)
                child.final |= child.fail.final     
                que.append(child)

# P = []
# np = int(input())
# for i in range(np) : 
#     P.append(input().rstrip())
# target = input().rstrip()

# P = ['ab', 'bc', 'de', 'cd']
# target = 'abcdeabcde'

# from collections import defaultdict
# hash = defaultdict(int)
# i = 1
# for p in P : 
#     hash[p] = i
#     i = i + 1

# ACtrie = AC(P)
# ans = ACtrie.search(target)
# print(ans)


hp, wp, hm, wm = map(int, input().split())


from collections import defaultdict
hash = defaultdict(int)
patnum = 0
cord = []
P = []
for i in range(hp) : 
    patrow = input().rstrip()
    if not hash[patrow] : 
        patnum = patnum + 1
        hash[patrow] = patnum
        P.append(patrow)
    cord.append(hash[patrow])

ACtrie = AC(P)
T = []
for i in range(hm) : 
    bigrow = input().rstrip()
    tablerow = ACtrie.search(bigrow)
    T.append(tablerow)

def LPS(string) :
    lps = [0 for i in range(len(string))]
    maxfix = 0
    i = 1
    while i < len(string) :
        if string[i] == string[maxfix] :
            maxfix = maxfix + 1
            lps[i] = maxfix
            i = i + 1
        elif maxfix != 0 :
            maxfix = lps[maxfix-1]
        else :
            lps[i] = 0
            i = i + 1
    return lps

def KMP(string, table) : 
    ans = []
    if len(string) > len(table) : 
        return ans
    lps = LPS(string)
    for col in range(len(table[0])) : 
        i, j = 0, 0
        while i < len(table) :
            if string[j] == table[i][col] :
                i = i + 1
                j = j + 1
            elif j != 0 :
                j = lps[j-1]
            else:
                i = i + 1
            if j == len(string) :
                ans.append([i - j, col])
                j = lps[j-1]
    return ans


print(len(KMP(cord, T)))