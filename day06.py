import numpy as np

with open("input06.txt") as ip:
    lines = [list(x.strip()) for x in ip]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

f = np.array(lines)

origo = np.where(f == '^')
(x, y) = origo
x = x[0]
y = y[0]
g = np.zeros(f.shape, dtype=int)
g[f == '#'] = -1
g[f == '^'] = 1
di = 0
print(x, y, f[x,y])

walk = True
while walk:
    a = dir[di]
    if 0 <= x+a[0] < g.shape[0] and 0 <= y+a[1] < g.shape[1]:
        while 0 <= x+a[0] < g.shape[0] and 0 <= y+a[1] < g.shape[1] and g[x+a[0], y+a[1]] == -1:
            di = (di+1) % 4
            a = dir[di]
        x = x+a[0]
        y = y+a[1]
        g[x, y] += 1
    else:
        walk = False
p1 = np.zeros(f.shape)
p1[g>0] = 1
print('PART 1', int(np.sum(p1)))
options = np.where(g>0)
print(options[0].shape)
part2 = 0

for i, x in enumerate(options[0]):
    f = np.array(lines)
    g = np.zeros(f.shape, dtype=int)
    g[f=='#'] = -1
    g[f=='^'] = 1
    obstacle_x = options[0][i]
    obstacle_y = options[1][i]
    g[obstacle_x, obstacle_y] = -1

    di = 0
    walk = True
    x = origo[0][0]
    y = origo[1][0]
    while walk:
        a = dir[di]
        if 0 <= x + a[0] < g.shape[0] and 0 <= y + a[1] < g.shape[1]:
            while 0 <= x + a[0] < g.shape[0] and 0 <= y + a[1] < g.shape[1] and g[x + a[0], y + a[1]] == -1:
                di = (di + 1) % 4
                a = dir[di]
            x = x + a[0]
            y = y + a[1]
            if 0 <= x < g.shape[0] and 0 <= y < g.shape[1]:
                g[x, y] += 1
                if g[x, y] > 4:
                    part2 += 1
                    # print(i, part2)
                    walk = False
            else:
                walk = False
        else:
            walk = False

print('PART2', part2)
