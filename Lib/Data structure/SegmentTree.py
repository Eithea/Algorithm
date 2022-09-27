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
    
    def _update(self, node, start, end, index, delta) : 
        if index < start or index > end : 
            return
        self.tree[node] = self.op(self.tree[node], delta)
        if start < end : 
            center = (start + end) // 2
            self._update(2*node, start, center, index, delta)
            self._update(2*node+1, center+1, end, index, delta)
    
    def rangeQuery(self, left, right) : 
        return self._search(1, 0, self.leng-1, left, right)
    
    def updateByDelta(self, idx, delta) : 
        self._update(1, 0, self.leng-1, idx, delta)
