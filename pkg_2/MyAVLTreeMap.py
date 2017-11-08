#from .MyTreeMap import MyTreeMap
from TdP_collections.tree.linked_binary_tree import LinkedBinaryTree


class MyAVLTreeMap():
    def al(self):
        return

tree = LinkedBinaryTree()

root_position = tree._add_root(56)
tree._add_left(root_position,7)
for p in tree.positions():
    print(p.element())