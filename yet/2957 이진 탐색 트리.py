class NODE() :
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class RBT() : 
    def __init__(self):
        self.root = None
        self.input = None
        self.count = 0

    def falldown(self, N, P, data) : 
        self.count = self.count + 1
        if N == None : 
            N = NODE(data)
            N.parent = P
            self.input = N
        else : 
            if data < N.data : 
                N.left = self.falldown(N.left, N, data)
            elif data > N.data : 
                N.right = self.falldown(N.right, N, data)
        return N
  
    def insert(self, data) : 
        self.root = self.falldown(self.root, None, data)
        return self.count
        

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())

rbt = RBT()
for i in range(n) : 
    x = rbt.insert(int(input()))
    print(x-i-1)