import sys

class SegmentTree : 
    def __init__(self, arr, operator = max, idt = -sys.maxsize) : 
        self.op = operator
        self.idt = idt
        self.leng = len(arr)
        self.size = 1 << (self.leng-1).bit_length()
        self.tree = [self.idt for _ in range(self.size*2)]
        self._createTree(arr)

    def _createTree(self, arr) : 
        self.tree[self.size : self.size+self.leng] = arr
        for i in range(self.size-1, -1, -1) :
            self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])
    
    def Query(self, left, right) : 
        l = left + self.size
        r = right + self.size + 1
        curl = self.idt
        curr = self.idt
        while l < r :
            if l %2 :
                curl = self.op(curl, self.tree[l])
                l += 1
            if r %2 :
                r -= 1
                curr = self.op(self.tree[r], curr)
            l //= 2
            r //= 2

        return self.op(curl, curr)
    
    def IndexOf(self, idx) : 
        return self.tree[idx + self.size]
    
    def Update(self, i, data) : 
        i += self.size
        self.tree[i] = data
        i //= 2
        while i:
            self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])
            i //= 2