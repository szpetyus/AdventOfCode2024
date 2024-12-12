import numpy as np
with open("input12.txt") as ip:
    lines = [list(x.strip()) for x in ip]

nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]
umap = np.array(lines, dtype='U')
m = np.zeros(umap.shape, dtype=int)
fences = {}
faces = {}

def fillnb(umap, m, x, y, a, idx):
    m[x, y] = idx
    for (i, j) in nb:
        if 0 <= x+i < m.shape[0] and 0 <= y+j < m.shape[1]:
            if a == umap[x+i, y+j] and m[x+i, y+j] == 0:
                fillnb(umap, m, x+i, y+j, a, idx)

idx = 1
for ((x, y), a) in np.ndenumerate(umap):
    if m[x, y] == 0:
        fillnb(umap, m, x, y, a, idx)
    idx += 1
def nfences(m, x, y, a):
    res = 4
    for (i, j) in nb:
        hit = False
        if 0 <= x+i < m.shape[0] and 0 <= y+j < m.shape[1]:
            if a == m[x+i, y+j]:
                res -= 1
                hit = True
        if not hit:
            fences[a] = fences.get(a, [])
            fences[a].append((x, y, i, j))

    return res

pm = {}
for ((x, y), a) in np.ndenumerate(m):
    pm[a] = pm.get(a, 0) + nfences(m, x, y, a)

part1 = 0
for a in pm:
    # print(a, pm[a], len(m[m == a]))
    part1 += pm[a] * len(m[m == a])

print('part 1', part1)

for a in pm:
    edges = []
    for (x, y, i, j) in fences[a]:
        if i != 0:
            found = False
            for (qx, qy, qi, qj) in edges:
                if qx == x and qi == i and qj == j and y in qy:
                    found = True
            if not found:
                eleje = y
                vege = y
                for z in range(y, 0, -1):
                    if (x, z, i, j) in fences[a]:
                        eleje = z
                    else:
                        break
                for z in range(y, m.shape[1], 1):
                    if (x, z, i, j) in fences[a]:
                        vege = z
                    else:
                        break
                rng = range(eleje, vege+1)
                e = (x, rng, i, j)
                edges.append(e)
        if j != 0:
            found = False
            for (qx, qy, qi, qj) in edges:
                if y == qy and qi == i and qj == j and x in qx:
                    found = True
            if not found:
                eleje = x
                vege = x
                for z in range(x, 0, -1):
                    if (z, y, i, j) in fences[a]:
                        eleje = z
                    else:
                        break
                for z in range(x, m.shape[0], 1):
                    if (z, y, i, j) in fences[a]:
                        vege = z
                    else:
                        break
                rng = range(eleje, vege+1)
                e = (rng, y, i, j)
                edges.append(e)
    faces[a] = edges
#     print(a, len(m[m == a]),  len(edges))
# print(faces[9])
# print(m==9)

part2 = 0
for a in faces:
    # print(a, len(faces[a]), len(m[m == a]))
    part2 += len(faces[a]) * len(m[m == a])

print('part 2', part2)


