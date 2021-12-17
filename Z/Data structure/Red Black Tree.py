class NODE() :
    def __init__(self, data) : 
        self.data = data
        self.red = True
        self.parent = None
        self.left = None
        self.right = None

class RBT() : 
    def __init__(self) : 
        self.root = None
        self.input = None
    
    def searchdown(self, N, v) : 
        if N == None or N.data == v : 
            return N
        if N.data < v : 
            return self.searchdown(N.right, v)
        else : 
            return self.searchdown(N.left, v)

    def falldown(self, N, P, v) : 
        if N == None : 
            N = NODE(v)
            N.parent = P
            self.input = N
        else : 
            if v <= N.data : 
                N.left = self.falldown(N.left, N, v)
            else : 
                N.right = self.falldown(N.right, N, v)
        return N

    def grandparent(self, N) : 
        if N == None or N.parent == None : 
            return None
        return N.parent.parent

    def uncle(self, N) : 
        G = self.grandparent(N)
        if G == None : 
            return None
        if G.right == N.parent : 
            return G.left
        return G.right
    
    def bro(self, N) : 
        if N == None or N.parent == None : 
            return None
        if N == N.parent.left : 
            return N.parent.right
        return N.parent.left
    
    def child(self, N) : 
        if N.left != None : 
            C = N.left
        elif N.right != None : 
            C = N.right
        else : 
            C = NODE(None)
            C.red = False
            C.parent = N
        return C
        
    def insert(self, P, data) : 
        self.root = self.falldown(self.root, P, data)
        self.resort(self.input)

    def resort(self, N) : 
        if N.parent == None : 
            N.red = False
            return
        elif not N.parent.red : 
            return
        else : 
            self.recolor(N)
    
    def recolor(self, N) : 
        U = self.uncle(N)
        if U != None and U.red : 
            G = self.grandparent(N)
            G.red = True
            U.red = False
            N.parent.red = False
            self.resort(G)
        else : 
            self.rotation(N)
    
    def rotation(self, N) : 
        G = self.grandparent(N)
        if G.right == N.parent and N == N.parent.left : 
            self.cw(N)
            N = N.right
        elif G.left == N.parent and N == N.parent.right : 
            self.ccw(N)
            N = N.left       
        G = self.grandparent(N)
        G.red = True
        N.parent.red = False
        if N == N.parent.left : 
            self.cw(N.parent)
        else : 
            self.ccw(N.parent)

    def cw(self, N) : 
        G = self.grandparent(N)
        if G != None : 
            if G.left == N.parent : 
                G.left = N
            else : 
                G.right = N
        N.parent.parent = N
        N.parent.left = N.right
        if N.right != None : 
            N.right.parent = N.parent
        N.right = N.parent
        N.parent = G
        if G == None : 
            self.root = N
    
    def ccw(self, N) : 
        G = self.grandparent(N)
        if G != None : 
            if G.left == N.parent : 
                G.left = N
            else : 
                G.right = N
        N.parent.parent = N
        N.parent.right = N.left
        if N.left != None : 
            N.left.parent = N.parent
        N.left = N.parent
        N.parent = G
        if G == None : 
            self.root = N

    def leftest(self, N) : 
        if N.left == None : 
            return N
        return self.leftest(N.left)
    
    def rightest(self, N) : 
        if N.right == None : 
            return N
        return self.rightest(N.right)

    def delete(self, N) : 
        C = self.child(N)
        if N.parent == None : 
            if C.data == None : 
                self.root = None
            else : 
                self.root = C
                C.red = False
                C.parent = None
            return
        if N.red : 
            if N == N.parent.left : 
                N.parent.left = None
            else : 
                N.parent.right = None
            return
        if not N.red and C.red : 
            C.parent = N.parent
            C.red = False
            if N == N.parent.left : 
                N.parent.left = C
            else : 
                N.parent.right = C
            return
        else : 
            C.parent = N.parent
            if N == N.parent.left : 
                N.parent.left = C
            else : 
                N.parent.right = C
            self.rotationD(C)
            if C == C.parent.left : 
                C.parent.left = None
            else : 
                C.parent.right = None
    
    def rotationD(self, N) : 
        if N.parent == None : 
            return
        B = self.bro(N)
        if B.red : 
            B.red = False
            B.parent.red = True
            if B == B.parent.left : 
                self.cw(B)
            else : 
                self.ccw(B)
        self.rebalance(N)
    
    def rebalance(self, N) : 
        B = self.bro(N)
        if not N.parent.red and not B.red and B.left == None and B.right == None : 
                B.red = True
                self.rotationD(N.parent)
                return
        self.replace(N)

    def replace(self, N) : 
        B = self.bro(N)
        if N.parent.red and not B.red and B.left == None and B.right == None : 
            B.red = True
            N.parent.red = False
            return
        if not B.red : 
            if N == N.parent.left and B.left != None and B.left.red : 
                B.red = True
                B.left.red = False
                self.cw(B.left)
            elif N == N.parent.right and B.right != None and B.right.red : 
                B.red = True
                B.right.red = False
                self.ccw(B.right)
        B = self.bro(N)
        B.red = N.parent.red
        N.parent.red = False
        if N == N.parent.left : 
            if B.right != None : 
                B.right.red = False
            self.ccw(B)
        else : 
            if B.left != None : 
                B.left.red = False
            self.cw(B)
            
    def inorder(self, N, array, n) : 
        if N.left != None : 
            self.inorder(N.left, array, n)
        if len(array) == n : 
            return
        array.append(N.data)
        if N.right != None : 
            self.inorder(N.right, array, n)

    def tree_insert(self, key) : 
        self.insert(None, key)

    def tree_find(self, key) : 
        return self.searchdown(self.root, key)
    
    def tree_erase(self, v) : 
        N = self.searchdown(self.root, v)
        if N == None : 
            return
        if N.left != None and N.right != None : 
            D = self.rightest(N.left)
            N.data, D.data = D.data, N.data
        else : 
            D = N
        self.delete(D)
    
    def tree_min(self) : 
        return self.leftest(self.root)

    def tree_max(self) : 
        return self.rightest(self.root)

    def tree_to_array(self, array, n) : 
        self.inorder(self.root, array, n)


# 파이썬은 알아서 할당해주므로 new_tree(), delete_tree()는 C에서 따로 구현 필요