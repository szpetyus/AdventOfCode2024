import numpy as np
with open("input12a.txt") as ip:
    lines = [list(x.strip()) for x in ip]

nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]
umap = np.array(lines, dtype='U')
m = np.zeros(umap.shape, dtype=int)

def fillnb(umap, m, x, y, a, idx):
    m[x, y] = idx
    for (i, j) in nb:
        if 0 <= x+i < m.shape[0] and 0 <= y+j < m.shape[1]:
            if a == umap[x+i, y+j] and m[x+i, y+j] == 0:
                fillnb(umap, m, x+i, y+j, a, idx)
                hit = True

idx = 1
for ((x, y), a) in np.ndenumerate(umap):
    if m[x, y] == 0:
        fillnb(umap, m, x, y, a, idx)
    idx += 1
def nfences(m, x, y, a):
    res = 4
    for (i, j) in nb:
        if 0 <= x+i < m.shape[0] and 0 <= y+j < m.shape[1]:
            if a == m[x+i, y+j]:
                res -= 1
    return res

pm = {}
for ((x, y), a) in np.ndenumerate(m):
    pm[a] = pm.get(a, 0) + nfences(m, x, y, a)

part1 = 0
for a in pm:
    # print(a, pm[a], len(m[m == a]))
    part1 += pm[a] * len(m[m == a])

print('part 1', part1)



