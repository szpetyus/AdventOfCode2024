from collections import deque
import numpy as np

lines = deque([])
in_locks = deque([])
in_keys = deque([])
proc = None
with open("input25.txt") as ip:
    for i, l in enumerate(ip):
        if l == '\n':
            proc = None
        else:
            x = l.strip()
            if proc is None:
                if x == '.....':
                    proc = in_keys
                elif x == '#####':
                    proc = in_locks
            x = x.replace('.', '0').replace('#', '1')
            proc.append(list(x))

keys = np.reshape(np.array(in_keys, dtype='int'), (-1, 7, 5))
locks = np.reshape(np.array(in_locks, dtype='int'), (-1, 7, 5))
keys = np.sum(keys, axis=1)
locks = np.sum(locks, axis=1)

print(locks.shape, keys.shape)
part1 = 0
for l in locks:
    for k in keys:
        z = np.max(k+l)
        if z < 8:
            part1 += 1
        # print(l, k, z)

print("PART1", part1)