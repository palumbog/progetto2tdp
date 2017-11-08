from TdP_collections.map import avl_tree,red_black_tree
import random
import time


num = 10000
randnum = 10000

def t():
    return time.time()

avltree = avl_tree.AVLTreeMap()
rbtree = red_black_tree.RedBlackTreeMap()
keys = []

t_insert_AVL = 0
t_insert_RB = 0

print("Random Insert")
for i in range(num):
    key = random.randint(0,randnum)
    keys.append(key)
    v = random.randint(0,randnum)
    start = t()
    avltree[key] = v
    stop = t()
    delta = stop - start
    t_insert_AVL += delta
    #print("\nkey "+str(key) + " value "+str(v))
    #print(str(i+1)+"\nInsert AVL "+str(delta))
    v = random.randint(0, randnum)
    start = t()
    rbtree[key] = v
    stop = t()
    delta = stop - start
    t_insert_RB += delta
    #print("Insert RB " + str(delta))
print("Num elementi AVL " + str(len(avltree)))
print("Num elementi RB " + str(len(rbtree)))
print("Altezza AVL "+ str(avltree.height()))
print("Altezza RB "+ str(rbtree.height()))
print("Aggiunti " + str(len(avltree)) +" elementi")
print("Tempo INSERT AVL " + str(t_insert_AVL))
print("Tempo INSERT RB  " + str(t_insert_RB))


t_search_AVL = 0
t_search_RB = 0

for key in keys:
    AVLstart = t()
    pavl = avltree.find_position(key)
    AVLstop = t()
    #print("Found " + str(pavl.value()))
    avl_part_time = AVLstop - AVLstart

    RBstart = t()
    prb = rbtree.find_position(key)
    RBstop = t()
    #print("Found " + str(pavl.value()))
    rb_part_time = RBstop - RBstart

    t_search_AVL += avl_part_time
    t_search_RB += rb_part_time

print("AVL --> "+str(t_search_AVL))
print("RB --> "+str(t_search_RB))

avltree.clear()
rbtree.clear()

print("Ordered Insert")
for i in range(num):
    key = i
    keys.append(key)
    v = random.randint(0,randnum)
    start = t()
    avltree[key] = v
    stop = t()
    delta = stop - start
    t_insert_AVL += delta
    #print("\nkey "+str(key) + " value "+str(v))
    #print(str(i+1)+"\nInsert AVL "+str(delta))
    v = random.randint(0, randnum)
    start = t()
    rbtree[key] = v
    stop = t()
    delta = stop - start
    t_insert_RB += delta
    #print("Insert RB " + str(delta))
print("Num elementi AVL " + str(len(avltree)))
print("Num elementi RB " + str(len(rbtree)))
print("Altezza AVL "+ str(avltree.height()))
print("Altezza RB "+ str(rbtree.height()))
print("Aggiunti " + str(len(avltree)) +" elementi")
print("Tempo INSERT AVL " + str(t_insert_AVL))
print("Tempo INSERT RB  " + str(t_insert_RB))