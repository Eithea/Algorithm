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
            else  :
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
        ret = []
        for letter in TARGET  :
            while now is not self.head and letter not in now :
                now = now.fail
            if letter in now :
                now = now[letter]           
            if now.final :
                ret.extend(list(now.out))
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

P = []
np = int(input())
for i in range(np) : 
    P.append(input().rstrip())
ACtrie = AC(P)

nt = int(input())
for i in range(nt) : 
    target = input().rstrip()
    ans = ACtrie.search(target)
    if ans : 
        print('YES')
    else : 
        print('NO')