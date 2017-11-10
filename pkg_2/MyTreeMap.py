from TdP_collections.map.binary_search_tree import TreeMap

class MyTreeMap(TreeMap):
    # ---------------------------- override Position class ----------------------------
    class Position(TreeMap.Position):
        def __init__(self,container, node, before = None, after = None,):
            #super(Position, self, container,node).__init__()
            self._before = before
            self._after = after
            self._container = container
            self._node = node

    def after(self,p):
        self._validate(p)
        return p._after

    def before(self,p):
        self._validate(p)
        return p._before

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None


    def delete(self, p):
        """Remove the item at given Position."""
        self._validate(p)  # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):  # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())  # from LinkedBinaryTree
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)  # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)  # if root deleted, parent is None

        # --------------------- public methods for (standard) map interface ---------------------

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        """Mi serve la position dell'elemento salvato"""
        position = None
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))  # from LinkedBinaryTree

            self._set_a_b(leaf)

        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v  # replace existing item's value
                self._rebalance_access(p)  # hook for balanced tree subclasses

                self._set_a_b(p)

                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)  # inherited from LinkedBinaryTree
                    self._set_a_b(leaf)
                else:
                    leaf = self._add_left(p, item)  # inherited from LinkedBinaryTree
                    self._set_a_b(leaf)

        self._rebalance_insert(leaf)  # hook for balanced tree subclasses

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)  # rely on positional version
                return  # successful deletion complete
            self._rebalance_access(p)  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))

    def _set_a_b(self, p, a, b):
        p._before = super(MyTreeMap, self).before(p)
        p._after = super(MyTreeMap, self).after(p)


from TdP_collections.map.binary_search_tree import TreeMap
import random
import time

def t():
    return time.time()

num = 10000
randnum = 10000
mytreemap = MyTreeMap()
treemap  = TreeMap()
keys = {}

t_insert_MTM = 0
t_insert_TM = 0

print("Inserimento Disordinato")
for i in range(num):
    key = random.randint(0,randnum)
    v = random.randint(0,randnum)
    keys[key] = v
    #MyTreeMap
    start = t()
    mytreemap[key] = v
    stop = t()
    delta = stop - start
    t_insert_MTM += delta
    #TreeMap
    start = t()
    treemap[key] = v
    stop = t()
    delta = stop - start
    t_insert_TM += delta
print("Altezza MTM "+ str(mytreemap.height()))
print("Altezza TM "+ str(treemap.height()))
print("Aggiunti " + str(len(mytreemap)) +" elementi")
print("Num elementi keys " + str(len(keys)))
print("Tempo INSERT MTM " + str(t_insert_MTM))
print("Tempo INSERT TM  " + str(t_insert_TM))
