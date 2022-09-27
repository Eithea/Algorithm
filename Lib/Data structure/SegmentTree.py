class SegmentTree : 
    def __init__(self, arr, operator = max) : 
        self.op = operator
        self.leng = len(arr)
        self.tree = [0 for _ in range(4* self.leng)]
        self._createTree(arr, 1, 0, self.leng-1)

    def _createTree(self, arr, node, start, end) : 
        if start == end : 
            self.tree[node] = arr[start]
            return self.tree[node]
        center = (start + end) // 2
        a = self._createTree(arr, 2*node, start, center)
        b = self._createTree(arr, 2*node+1, center+1, end)
        self.tree[node] = self.op(a, b)
        return self.tree[node]
    
    def _search(self, node, start, end, left, right) : 
        if left > end or right < start : 
            return 0
        if left <= start and right >= end : 
            return self.tree[node]
        center = (start + end) // 2
        a = self._search(2*node, start, center, left, right)
        b = self._search(2*node+1, center+1, end, left, right)
        return self.op(a, b)
    
    def _update(self, node, start, end, left, right, value) : 
        if end < left or right < start : 
            return
        if left <= start and end <= right : 
            self.tree[node] = self.tree[node] + value * (end - start + 1)
            return
        center = (start + end) // 2
        self._update(2*node, start, center, left, right, value)
        self._update(2*node+1, center+1, end, left, right, value)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    def Query(self, left, right) : 
        return self._search(1, 0, self.leng-1, left, right)
    
    def Update(self, idx, delta) : 
        self._update(1, 0, self.leng-1, idx, idx, delta)
    
    def UpdateRange(self, left, right, delta) : 
        self._update(1, 0, self.leng-1, left, right, delta)