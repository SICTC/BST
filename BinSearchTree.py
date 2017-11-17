class BinarySearchTree(object):
    
    class node(object):
        
        def __init__(self, key, value):
            self._key = key
            self._value = value
            self._left = None
            self._right = None
    
    def __init__(self):
        self.make_empty()
        
    def make_empty(self):
        self._root = None
        self._count = 0
        self._removed = None
        self._order = "pre"
    
    def _insert(self, r, k, v):
        #found where new value goes, so insert it
        if not r:
            t = BinarySearchTree.node(k,v)
            return t
        if k < r._key:
            r._left = self._insert(r._left, k, v)
        else: #k >= r._key
            r._right = self._insert(r._right, k, v)
        return r
        
    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)
        self._count += 1    
        
    def _lookup(self, r, k):
        if not r:
            return None
        #found it, so return it
        if k == r._key:
            return r._value
        #search left branch
        if k < r._key:
            return self._lookup(r._left, k)
        #search right branch
        else:
            return self._lookup(r._right, k)
    
    def lookup(self, key):
        return self._lookup(self._root, key)
    
    def _remove(self, r, k):
        if not r:
            return None
        #found it
        if k == r._key:
            #3 cases for removal
            #0 children:
            if not r._left and not r._right:
                self._removed = r._value
                self._count -= 1
                return None
            #1 child:
            if not r._right:
                self._removed = r._value
                self._count -= 1
                return r._left
            if not r._left:
                self._removed = r._value
                self._count -= 1
                return r._right
            #2 children:
            mn = self._minimum(r._right)
            saved = r._value
            r._key = mn._key
            r._value = mn._value
            r._right = self._remove(r._right, mn._key)
            self._removed = saved
            return r
        if k < r._key:
            r._left = self._remove(r._left, k)
        else:
            r._right = self._remove(r._right, k)
        return r
    
    def remove(self, key):
        self._removed = None
        self._root = self._remove(self._root, key)
        return self._removed
    
    def preorder(self):
        self._order = "pre"
        return self
    
    def inorder(self):
        self._order = "in"
        return self
    
    def postorder(self):
        self._order = "post"
        return self
        
    def __iter__(self):
        return self._traverse(self._root)
    
    #if preorder: print r
    #traverse r.left
    #if inorder: print r
    #traverse r.right
    #if postorder: print r
    def _traverse(self, r):
        if self._order == "pre":
            yield r._value
        if r._left:
            for el in self._traverse(r._left):
                yield el
        if self._order == "in":
            yield r._value
        if r._right:
            for el in self._traverse(r._right):
                yield el
        if self._order == "post":
            yield r._value
           
    def __len__(self):
        return self._count
