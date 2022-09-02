import sys
input = sys.stdin.readline
from collections import deque

class NODE(dict) :
        def __init__(self) :
            super().__init__()
            self.final = False
            self.out = 0
            self.fail = None
            
        def addout(self, out) :
            self.out = max(self.out, out)
        
        def addchild(self, alphabet) :
            self[alphabet] = NODE()

class AC() :      
    def __init__(self, PATTERN_LIST) :
        self.PATTERN_LIST = PATTERN_LIST
        self.head = NODE()      
        self.makeTrie()
        self.makeFailure()
        
    def search(self, TARGET) :
        count = 0 
        now = self.head
        for index in range(len(TARGET)) :
            letter = TARGET[index] 
            while now is not self.head and letter not in now :
                now = now.fail
            if letter in now :
                now = now[letter]           
            if now.final :
                for i in range(index+1 - now.out, index+1) : 
                    if TARGET[i] != 0 : 
                        count = count + 1
                        TARGET[i] = 0
        return count
    
    def makeTrie(self) :
        for pattern in self.PATTERN_LIST :
            now = self.head
            for letter in pattern  :
                if letter not in now :
                    now.addchild(letter)
                now = now[letter]
            now.final = True
            now.addout(len(pattern))
            
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
nt = int(input())
target = list(input().rstrip())
np = int(input())
for i in range(np) : 
    P.append(input().rstrip())

ACtrie = AC(P)
ct = ACtrie.search(target)
print(nt - ct)