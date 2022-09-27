class SegmentTree : 
    def __init__(self, arr, operator = max) : 
        self.op = operator
        self.leng = len(arr)
        self.tree = [0 for i in range(self._fitSize(self.leng))]
        self._createTree(arr, 1, 0, self.leng-1)

    def _fitSize(n) : 
        while size < 2*n : 
            size *= 2
        return size

    def _createTree(self, arr, i, start, end) : 
        if start == end : 
            self.tree[i] = arr[start]
            return self.tree[i]
        center = (start + end) // 2
        a = self._createTree(self.tree, arr, 2*i, start, center)
        b = self._createTree(self.tree, arr, 2*i+1, center+1, end)
        self.tree[i] = self.op(a, b)
        return self.tree[i]
    
    def _search(self, i, start, end, left, right) : 
        if left > end or right < start : 
            return 0
        if left <= start and right >= end : 
            return self.tree[i]
        center = (start + end) // 2
        a = self._search(2*i, start, center, left, right)
        b = self._search(2*i+1, center+1, end, left, right)
        return self.op(a, b)
    
    def _update(self, i, start, end, index, delta) : 
        if index < start or index > end : 
            return
        if start == end : 
            self.tree[i] = delta
            return
        center = (start + end) // 2
        self._update(2*i, start, center, index, delta)
        self._update(2*i+1, center+1, end, index, delta)
        self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])
    
    def rangeQuery(self, left, right) : 
        return self._search(1, 0, self.leng-1, left, right)
    
    def updateByDelta(self, idx, delta) : 
        self._update(1, 0, self.leng-1, idx, delta)
