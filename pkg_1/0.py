from TdP_collections.map.binary_search_tree import TreeMap
import random
import time
tree = TreeMap()
n = 1000
r = 1000000

keys = []
start = time.time()
for i in range(n):
    k = random.randint(0,r)
    keys.append(k)
    v = random.randint(0,r)
    tree[k] = v
stop = time.time()

j = 0
for e in tree:
    j += 1
print(j)
print(stop-start)