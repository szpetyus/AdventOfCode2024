import numpy as np
i = np.fromfile("input01.txt", dtype=int, sep=' ').reshape(-1, 2)
i.sort(axis=0)
j = np.abs(i[:, 1]-i[:, 0])
print("Part 1", sum(j))

hist = {}
v = 0
key = 0
for x in i[:, 1]:
    if x == key:
        v += 1
    else:
        hist[key] = v
        v = 1
        key = x

part2 = 0
for x in i[:, 0]:
    if x in hist:
        part2 += x * hist[x]
        print(x, hist[x], x * hist[x])
print("part 2", part2)
