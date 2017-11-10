from TdP_collections.map import avl_tree,red_black_tree
import random
import time


"""1) Ricerca più efficiente in AVL rispetto ai RB sempre
   2) Hp: dati in input ordinati o quasi ordinati
      Th: costo complessivo degli inserimenti minore in  AVL"""

num = 1000
randnum = 10000

def t():
    return time.time()

avltree = avl_tree.AVLTreeMap()
rbtree = red_black_tree.RedBlackTreeMap()
keys = {}

def flush():
    avltree.clear()
    rbtree.clear()
    keys.clear()



t_insert_random_AVL = 0
t_insert_random_RB = 0

print("Inserimento Disordinato")
for i in range(num):
    key = random.randint(0,randnum)
    v = random.randint(0,randnum)
    keys[key] = v
    start = t()
    avltree[key] = v
    stop = t()
    delta = stop - start
    t_insert_random_AVL += delta
    #print("\nkey "+str(key) + " value "+str(v))
    #print(str(i+1)+"\nInsert AVL "+str(delta))
    start = t()
    rbtree[key] = v
    stop = t()
    delta = stop - start
    t_insert_random_RB += delta
    #print("Insert RB " + str(delta))
print("Altezza AVL "+ str(avltree.height()))
print("Altezza RB "+ str(rbtree.height()))
print("Aggiunti " + str(len(avltree)) +" elementi")
print("Num elementi keys " + str(len(keys)))
print("Tempo INSERT AVL " + str(t_insert_random_AVL))
print("Tempo INSERT RB  " + str(t_insert_random_RB))


t_search_random_AVL = 0
t_search_random_RB = 0

print("\nRicerca inserimenti disordinati")
for key in keys:
    AVLstart = t()
    avltree.find_position(key)
    AVLstop = t()

    #print("Found " + str(pavl.value()))
    avl_part_time = AVLstop - AVLstart

    RBstart = t()
    rbtree.find_position(key)
    RBstop = t()

    #print("Found " + str(pavl.value()))
    rb_part_time = RBstop - RBstart

    t_search_random_AVL += avl_part_time
    t_search_random_RB += rb_part_time

delta_search_random = t_search_random_AVL - t_search_random_RB

print("Tempo SEARCH AVL --> "+str(t_search_random_AVL))
print("Tempo SEARCH RB  --> "+str(t_search_random_RB))



flush()
t_insert_ordinato_AVL = 0
t_insert_ordinato_RB = 0



print("\nInserimento ordinato")
for i in range(num):
    key = i
    v = random.randint(0,randnum)
    keys[key] = v
    start = t()
    avltree[key] = v
    stop = t()
    delta = stop - start
    t_insert_ordinato_AVL += delta
    #print("\nkey "+str(key) + " value "+str(v))
    #print(str(i+1)+"\nInsert AVL "+str(delta))
    v = random.randint(0, randnum)
    start = t()
    rbtree[key] = v
    stop = t()
    delta = stop - start
    t_insert_ordinato_RB += delta
    #print("Insert RB " + str(delta))
print("Altezza AVL "+ str(avltree.height()))
print("Altezza RB "+ str(rbtree.height()))
print("Aggiunti " + str(len(avltree)) +" elementi")
print("Num elementi keys " + str(len(keys)))
print("Tempo INSERT AVL " + str(t_insert_ordinato_AVL))
print("Tempo INSERT RB  " + str(t_insert_ordinato_RB))


t_search_ordinato_AVL = 0
t_search_ordinato_RB = 0

print("\nRicerca inserimenti ordinati")
for key in keys:
    AVLstart = t()
    avltree.find_position(key)
    AVLstop = t()
    #print("Found " + str(pavl.value()))
    avl_part_time = AVLstop - AVLstart

    RBstart = t()
    rbtree.find_position(key)
    RBstop = t()
    #print("Found " + str(pavl.value()))
    rb_part_time = RBstop - RBstart

    t_search_ordinato_AVL += avl_part_time
    t_search_ordinato_RB += rb_part_time

delta_search_ordinato = t_search_random_AVL - t_search_random_RB

print("Tempo SEARCH AVL --> "+str(t_search_ordinato_AVL))
print("Tempo SEARCH RB  --> "+str(t_search_ordinato_RB))



flush()

t_insert_qordinato_AVL = 0
t_insert_qordinato_RB = 0

print("\nInserimento quasi ordinato")
key = 0
for i in range(num):
    if(i%100 == 0):
        key = random.randint(0, randnum)
    else:
        key = i
    v = random.randint(0,randnum)
    keys[key] = v
    start = t()
    avltree[key] = v
    stop = t()
    delta = stop - start
    t_insert_qordinato_AVL += delta
    #print("\nkey "+str(key) + " value "+str(v))
    #print(str(i+1)+"\nInsert AVL "+str(delta))
    v = random.randint(0, randnum)
    start = t()
    rbtree[key] = v
    stop = t()
    delta = stop - start
    t_insert_qordinato_RB += delta
    #print("Insert RB " + str(delta))
print("Altezza AVL "+ str(avltree.height()))
print("Altezza RB "+ str(rbtree.height()))
print("Aggiunti " + str(len(avltree)) +" elementi")
print("Num elementi keys " + str(len(keys)))
print("Tempo INSERT AVL " + str(t_insert_qordinato_AVL))
print("Tempo INSERT RB  " + str(t_insert_qordinato_RB))

t_search_qordinato_AVL = 0
t_search_qordinato_RB = 0

print("\nRicerca inserimenti quasi ordinati")
for key in keys:
    AVLstart = t()
    avltree.find_position(key)
    AVLstop = t()
    #print("Found " + str(pavl.value()))
    avl_part_time = AVLstop - AVLstart

    RBstart = t()
    rbtree.find_position(key)
    RBstop = t()
    #print("Found " + str(pavl.value()))
    rb_part_time = RBstop - RBstart

    t_search_qordinato_AVL += avl_part_time
    t_search_qordinato_RB += rb_part_time

delta_search_qordinato = t_search_qordinato_AVL - t_search_qordinato_RB

print("Tempo SEARCH AVL --> "+str(t_search_qordinato_AVL))
print("Tempo SEARCH RB  --> "+str(t_search_qordinato_RB))




delta_insert_random = t_insert_random_AVL - t_insert_random_RB
delta_insert_ordinato = t_insert_ordinato_AVL- t_insert_ordinato_RB
delta_insert_qordinato = t_insert_qordinato_AVL - t_insert_qordinato_RB

print("\nSe valore negativo è più veloce AVL")
print("Insert Random          " + str(delta_insert_random))
print("Insert Ordinato       " + str(delta_insert_ordinato))
print("Insert Quasi Ordinato " + str(delta_insert_qordinato))
print("Search Disordinato    " + str(delta_search_random))
print("Search Ordinato       " + str(delta_search_ordinato))
print("Search Quasi Ordinato " + str(delta_search_qordinato) + "\n")
