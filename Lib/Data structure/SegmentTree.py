import sys

class SegmentTree : 
    def __init__(self, arr, operator = max, idt = -sys.maxsize) : 
        self.op = operator
        self.idt = idt
        self.leng = len(arr)
        self.size = 1 << (self.leng - 1).bit_length()
        self.tree = [self.idt for _ in range(self.size*2)]
        self._createTree(arr)

    def _createTree(self, arr) : 
        self.tree[self.size : self.size+self.leng] = arr
        for i in reversed(range(self.size)) :
            self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])
    
    def Query(self, left, right) : 
        left += self.size
        right += self.size+1

        curl = self.idt
        curr = self.idt
        while left < right:
            if left %2:
                curl = self.op(curl, self.tree[left])
                left += 1
            if right %2:
                right -= 1
                curr = self.op(self.tree[right], curr)
            left //= 2
            right //= 2

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