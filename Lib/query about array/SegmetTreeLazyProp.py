class LazySegmentTree : 
    def __init__(self, arr, operator = max) : 
        self.op = operator
        self.leng = len(arr)
        self.tree = [0 for _ in range(4* self.leng)]
        self.lazy = [0 for _ in range(4* self.leng)]
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

    def _update_lazy(self, node, start, end) : 
        if self.lazy[node] : 
            self.tree[node] = self.tree[node] + self.lazy[node] * (end - start + 1)
            if start != end : 
                self.lazy[2*node] = self.lazy[2*node] + self.lazy[node]
                self.lazy[2*node+1] = self.lazy[2*node+1] + self.lazy[node]
            self.lazy[node] = 0

    def _update(self, node, start, end, left, right, value) : 
        self._update_lazy(self, node, start, end)
        if end < left or right < start : 
            return
        if left <= start and end <= right : 
            self.tree[node] = self.tree[node] + value * (end - start + 1)
            if start != end : 
                self.lazy[2*node] = self.lazy[2*node] + value
                self.lazy[2*node+1] = self.lazy[2*node+1] + value
            return
        center = (start + end) // 2
        self._update(2*node, start, center, left, right, value)
        self._update(2*node+1, center+1, end, left, right, value)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    def _search(self, node, start, end, left, right) : 
        self._update_lazy(self, node, start, end)
        if left > end or right < start : 
            return 0
        if left <= start and right >= end : 
            return self.tree[node]
        center = (start + end) // 2
        a = self._search(2*node, start, center, left, right)
        b = self._search(2*node+1, center+1, end, left, right)
        return self.op(a, b)
    
    def Query(self, left, right) : 
        return self._search(1, 0, self.leng-1, left, right)
    
    def Update(self, idx, delta) : 
        self._update(1, 0, self.leng-1, idx, idx, delta)
    
    def UpdateRange(self, left, right, delta) : 
        self._update(1, 0, self.leng-1, left, right, delta)
