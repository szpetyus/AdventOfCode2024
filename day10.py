import numpy as np
import networkx as nx

with open("input10.txt") as ip:
    lines = [list(x.strip()) for x in ip]
    fi = np.array(lines, dtype=int)

# print(fi)
starts = np.where(fi==0)
ends = np.where(fi==9)
# print(starts)
# scores = np.zeros(starts[0].shape)
# for i in range(len(scores)):
#     p = start[0][i], start[1][i]
#     win = fi[max(0, p[0]-1):min(fi.shape[1], p[0]+2), max(0, p[1]-1):min(fi.shape[0], p[1]+2)]
#     for
paths = nx.DiGraph()
for xy, v in np.ndenumerate(fi):
    paths.add_node(xy)
    if xy[0]-1 >= 0:
        if fi[xy[0]-1, xy[1]] == v-1:
            paths.add_edge((xy[0]-1, xy[1]), xy)
        elif fi[xy[0] - 1, xy[1]] == v + 1:
            paths.add_edge(xy, (xy[0] - 1, xy[1]))
    if xy[1]-1 >= 0:
        if fi[xy[0], xy[1]-1] == v-1:
            paths.add_edge((xy[0], xy[1]-1), xy)
        elif fi[xy[0], xy[1]-1] == v + 1:
            paths.add_edge(xy, (xy[0], xy[1]-1))

part1 = 0
part2 = 0
for i in range(len(starts[0])):
    for j in range(len(ends[0])):
        z = list(nx.all_simple_paths(paths, (starts[0][i], starts[1][i]), (ends[0][j], ends[1][j])))
        # print(i, len(z))
        if len(z)>0:
            part1 += 1
        part2 += len(z)

# print(paths)
print("part 1", part1)
print("part 2", part2)

