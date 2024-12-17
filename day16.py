import numpy as np
import networkx as nx
from collections import deque

with open("input16.txt") as ip:
    lines = [list(x.strip()) for x in ip]

rmap = np.array(lines, dtype='U')
# print(rmap)
dirs = deque([[0, 1], [-1, 0], [0, -1], [1, 0]])
prices = [1,1001,2001,1001]
paths = nx.Graph()

start = np.where(rmap == 'S')
start = (start[0][0], start[1][0])
print("start", start)
paths.add_node((start, 0))
pos = start
stack = deque([(pos, 0)])

while len(stack)>0:
    xdirs = dirs.copy()
    pos, xdir = stack.pop()
    if rmap[pos] == 'E':
        end = pos
        endx = xdir
        continue
    xdirs.rotate(-xdir)
    for w, x in enumerate(xdirs):
        posx = tuple(np.array(pos) + np.array(x))
        if rmap[posx] in '.SE' and (posx, (xdir+w) % 4) not in paths.nodes:
            stack.append((posx, (xdir+w) % 4))
        if rmap[posx] in '.SE':
            paths.add_edge((pos, xdir), (posx, (xdir + w) % 4), weight=prices[w])
# print(paths)

for i in range(4):
    if i != endx:
        paths.add_edge((end, endx), (end, i), weight=0)
    # if i != 0:
    #     paths.add_edge((start, 0), (start, i), weight=0)

# print(paths)
# 586748 too high
# 576728 ?
print("part1", nx.path_weight(paths, nx.dijkstra_path(paths, (start, 0), (end, 0), 'weight'), 'weight'))
tiles = set()
for p in nx.all_shortest_paths(paths, (start, 0), (end, 0), weight='weight', method='dijkstra'):
    for ((x,y),_) in p:
        tiles.add((x,y))

print("part2", len(tiles))
# nx.dijkstra_path(paths, (start, 0), (end, endx), 'weight')
