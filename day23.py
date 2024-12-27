import networkx as nx

with open("input23.txt") as ip:
    lines = [x.strip().split("-") for x in ip]

g = nx.Graph()
tees = []
for a, b in lines:
    g.add_edge(a, b)
    if a.startswith("t"):
        tees.append(a)
    if b.startswith("t"):
        tees.append(b)


tris = []
trs = nx.cluster.triangles(g, tees)
for x in trs:
    for y in nx.neighbors(g, x):
        for z in nx.neighbors(g, y):
            if x != z and x in nx.neighbors(g, z):
                if not (x,y,z) in tris and not (x,z,y) in tris and not (z,x,y) in tris and not (z,y,x) in tris and not (y,z,x) in tris and not (y,x,z) in tris:
                    tris.append((x,y,z))
                    # print((x,y,z))
print("PART 1", len(tris))

lgc = dict(nx.cluster.clustering(g))
max_cl = max(lgc.values())
members = [x for x in lgc if lgc[x]==max_cl]
print("PART 2", ",".join(sorted(members)))