import numpy as np

with open("input06.txt") as ip:
    lines = [list(x.strip()) for x in ip]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

f = np.array(lines)

(x, y) = np.where(f == '^')
x = x[0]
y = y[0]
f[x,y] = 'X'
di = 0
print(x, y, f[x,y])

walk = True
while walk:
    a = dir[di]
    if 0 <= x+a[0] < f.shape[0] and 0 <= y+a[1] < f.shape[1]:
        while 0 <= x+a[0] < f.shape[0] and 0 <= y+a[1] < f.shape[1] and f[x+a[0], y+a[1]] == '#':
            di = (di+1) % 4
            a = dir[di]
        f[x, y] = 'X'
        x = x+a[0]
        y = y+a[1]
        f[x, y] = 'X'
    else:
        walk = False
p1 = np.zeros(f.shape)
p1[f=='X'] = 1
print(f)
print(p1)
print(np.sum(p1))
